## Teste automático do jogo (Ren'Py 8.5, comando "test"). NÃO fica em game/:
## copie para game/ de um build extraído (ver scripts/teste_jogo/README.md).
## Percorre caminhos do Renato escolhendo opções por posição (A=0, B=1, C=2),
## grava capturas das telas e uma transcrição em tests/<caminho>.txt.

## Não usar a pasta de saves real do jogo (~/.renpy/petsaude-pop-rua): só a
## que vier em --savedir.
init 1000 python:
    config.save_directory = None

init python:
    import os, time, json

    class _Teste(object):
        caminho = ""
        escolhas = []
        i = 0
        n = 0
        ult = 0.0
        ult_chave = None
        repet = 0
        falas = 0
        log = None
        fim = False
        saiba_mais = False
        iniciado = False
        aguardando = None

    T = _Teste()

    def teste_dir():
        d = os.path.join(config.basedir, "tests", "screenshots", T.caminho)
        if not os.path.isdir(d):
            os.makedirs(d)
        return d

    def teste_log(s):
        with open(os.path.join(config.basedir, "tests", T.caminho + ".txt"), "a", encoding="utf-8") as f:
            f.write(s + "\n")

    def teste_shot(tipo):
        T.n += 1
        renpy.screenshot(os.path.join(teste_dir(), "%03d_%s.png" % (T.n, tipo)))

    def teste_iniciar(caminho, letras, label):
        T.caminho = caminho
        T.escolhas = list(letras)
        T.i = 0
        T.n = 0
        T.falas = 0
        T.fim = False
        T.saiba_mais = False
        T.iniciado = False
        T.ult_chave = None
        T.aguardando = None
        T.repet = 0
        p = os.path.join(config.basedir, "tests", caminho + ".txt")
        if os.path.exists(p):
            os.remove(p)
        teste_log("# caminho %s: %s (início: %s)" % (caminho, " ".join(letras), label))
        _preferences.transitions = 0
        _preferences.text_cps = 0
        _preferences.afm_enable = False

    class Passo(Action):
        def __call__(self):
            agora = time.time()
            if agora - T.ult < 0.35:
                return
            T.ult = agora

            if renpy.get_screen("main_menu"):
                if T.iniciado:
                    T.fim = True
                return
            T.iniciado = True

            ch = renpy.get_screen("choice")
            if ch:
                itens = ch.scope["items"]
                caps = [it.caption for it in itens]
                chave = ("choice", tuple(caps))
                if not self.estavel(chave):
                    return
                teste_shot("escolha")
                if T.i >= len(T.escolhas):
                    teste_log("!! ACABARAM AS ESCOLHAS diante de: %s" % caps)
                    T.fim = True
                    return
                letra = T.escolhas[T.i]
                T.i += 1
                idx = "ABC".index(letra)
                teste_log("\n>> ESCOLHA %d (%s): %s" % (T.i, letra, caps[idx]))
                for k, c in enumerate(caps):
                    teste_log("   [%s] %s" % ("ABC"[k], c))
                teste_retornar(itens[idx].action.value)
                return

            for nome in ("contexto_real_mais", "contexto_real", "card", "mensagem_celular", "pagina_caderno", "painel_final"):
                s = renpy.get_screen(nome)
                if not s:
                    continue
                chave = (nome, repr(sorted((k, repr(v)[:80]) for k, v in s.scope.items() if k in ("titulo", "linha1", "linha2", "rotulo", "texto", "linhas", "titulo_mapa"))))
                if not self.estavel(chave):
                    return
                teste_shot(nome)
                sc = s.scope
                if nome == "card":
                    teste_log("\n[%s] %s %s" % (sc.get("titulo"), sc.get("linha1"), sc.get("linha2") or ""))
                elif nome == "mensagem_celular":
                    teste_log("\n[CELULAR %s] %s" % (sc.get("rotulo"), sc.get("texto")))
                elif nome == "pagina_caderno":
                    teste_log("\n[CADERNO]\n  " + "\n  ".join(sc.get("linhas")))
                elif nome == "painel_final":
                    teste_log("\n[PAINEL] barras=%s nos=%s" % (json.dumps(teste_barras()), json.dumps(teste_nos())))
                elif nome == "contexto_real":
                    teste_log("\n[CONTEXTO REAL] blocos=%s mais=%s" % ([b[0] for b in sc.get("blocos")], [b[0] for b in (sc.get("mais") or [])]))
                    if sc.get("mais") and not T.saiba_mais:
                        T.saiba_mais = True
                        T.aguardando = chave
                        renpy.run(Show("contexto_real_mais", blocos=sc.get("mais"), fontes=sc.get("fontes")))
                        return
                if nome == "contexto_real_mais":
                    teste_log("[SAIBA MAIS aberto] blocos=%s" % [b[0] for b in sc.get("blocos")])
                    T.aguardando = chave
                    renpy.run(Hide("contexto_real_mais"))
                    return
                teste_retornar(True)
                return

            s = renpy.get_screen("say")
            if s:
                quem = s.scope.get("who") or ""
                oque = s.scope.get("what") or ""
                chave = ("say", quem, oque)
                if not self.estavel(chave):
                    return
                T.falas += 1
                teste_log("%s%s" % ((quem + ": ") if quem else "", oque))
                if T.falas % 7 == 1 or "Desfecho" in oque or "Dia concluído" in oque:
                    teste_shot("fala")
                teste_retornar(True)
                return

            # nenhuma tela conhecida: conta repetições para detectar travamento
            self.estavel(("nada",))
            if T.repet > 40:
                teste_shot("TRAVADO")
                teste_log("!! TRAVADO: nenhuma tela conhecida; telas=%s" % [x for x in ("say", "choice", "card") if renpy.get_screen(x)])
                T.fim = True

        def estavel(self, chave):
            # não age de novo na tela em que acabou de agir (o Return chega no tick seguinte)
            if chave == T.aguardando:
                return False
            T.aguardando = None
            # só age depois de ver a mesma tela em dois ticks seguidos (tela já desenhada)
            if chave != T.ult_chave:
                T.ult_chave = chave
                T.repet = 0
                return False
            T.repet += 1
            return True

        def get_sensitive(self):
            return True

    def teste_retornar(v):
        T.aguardando = T.ult_chave
        renpy.show_screen("teste_retorno", valor=v)
        renpy.restart_interaction()

    def teste_nos():
        try:
            return dict(store.nos_rede)
        except Exception as e:
            return str(e)

    def teste_barras():
        try:
            return barras()
        except Exception as e:
            return str(e)


screen teste_retorno(valor):
    zorder 999
    timer 0.05 action [Hide("teste_retorno"), Return(valor)]

testsuite global:
    testcase menu:
        pause 3.0
        screenshot "menu/01_menu_principal.png"
        run ShowMenu("casos")
        pause 2.0
        screenshot "menu/02_casos.png"
        run Return()
        pause 1.0

    testcase p1_canonica:
        $ teste_iniciar("p1_canonica", "ABCCABBACAB", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p2_c_e_retomar:
        $ teste_iniciar("p2_c_e_retomar", "ABBACCABBACAB", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p3_b_d7_e_retomar:
        $ teste_iniciar("p3_b_d7_e_retomar", "ABCCABAAABACAB", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p4_varios_desvios:
        $ teste_iniciar("p4_varios_desvios", "BACBBCBBBCA", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p5_desencontro_recuperado:
        $ teste_iniciar("p5_desencontro_recuperado", "CCCAAABABAC", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p6_c_sem_orientacao:
        $ teste_iniciar("p6_c_sem_orientacao", "ACAB", "renato")
        run Start("renato")
        run Passo() until eval T.fim timeout 900

    testcase p7_atalho_cena7:
        $ teste_iniciar("p7_atalho_cena7", "CAB", "renato_atalho_cena7")
        run Start("renato_atalho_cena7")
        run Passo() until eval T.fim timeout 900

    testcase v_menus:
        pause 3.0
        run ShowMenu("materiais")
        pause 2.0
        screenshot "verif/materiais.png"
        run ShowMenu("redes_apoio")
        pause 2.0
        screenshot "verif/redes_apoio.png"
        run Return()
        pause 1.0

    testcase zz_sair:
        exit
