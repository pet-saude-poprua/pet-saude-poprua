## telas_menu.rpy — Telas de menu: Casos, Progresso, Materiais,
## Redes de apoio e Sobre o jogo (estrutura de docs/estrutura-telas.md).
## Conteúdo de Materiais/Redes é provisório — validar textos com o grupo.

## O progresso fica em persistent.progresso (ver game/nucleo/estado.rpy):
## {id_da_historia: {"desfecho", "barras", "nos", "vezes"}}.


## ─────────────────────────────────────────────────────────────────────────────
## CASOS — uma ficha por história registrada (game/historias/<nome>/dados.rpy).
## O identificador interno da screen (`capitulos`) foi mantido para não quebrar
## ShowMenu("capitulos") na navegação.
## ─────────────────────────────────────────────────────────────────────────────

screen capitulos():

    tag menu

    use game_menu(_("Casos"), scroll="viewport"):

        vbox:
            spacing 18

            for h in historias_em_ordem():
                $ prog = (persistent.progresso or {}).get(h["id"])

                if h["jogavel"]:
                    frame:
                        background "#0d1f2dee"
                        padding (24, 18)
                        xfill True

                        has vbox
                        spacing 6

                        hbox:
                            spacing 12
                            text h["subtitulo"].upper() size 15 color "#3E7CB1" bold True
                            if prog:
                                text ("concluída — desfecho " + prog["desfecho"]) size 13 color "#8FD0C6" italic True yalign 0.5
                            else:
                                text "não iniciada" size 13 color "#8899aa" italic True yalign 0.5

                        text h["titulo"] font gui.titulo_font size 26 color "#f0f0f0"
                        text h["sinopse"] size 15 color "#b8c4ce"

                        null height 6
                        textbutton _("Jogar esta história  ›") action Start(h["label"]) text_size 17

                else:
                    frame:
                        background "#101820aa"
                        padding (24, 14)
                        xfill True

                        has vbox
                        spacing 3

                        hbox:
                            spacing 10
                            text (h["subtitulo"] + " — " + h["titulo"]) size 17 color "#5a6773" bold True
                            text "em desenvolvimento" size 12 color "#4a555e" italic True yalign 0.5
                        text h["sinopse"] size 13 color "#4a555e" italic True


## ─────────────────────────────────────────────────────────────────────────────
## PROGRESSO (persistente entre sessões)
## ─────────────────────────────────────────────────────────────────────────────

screen perfil():

    tag menu

    $ progresso = persistent.progresso or {}

    use game_menu(_("Progresso"), scroll="viewport"):

        vbox:
            spacing 16

            text "Histórias" font gui.titulo_font size 26 color "#f0f0f0"

            hbox:
                spacing 12
                box_wrap True
                for h in historias_em_ordem():
                    $ feita = h["id"] in progresso
                    frame:
                        background ("#14524A" if feita else "#1a2229")
                        padding (14, 10)
                        text h["titulo"] size 15 color ("#B8EDE4" if feita else "#5a6773") bold True

            if progresso:

                for h in historias_em_ordem():
                    if h["id"] in progresso:
                        $ p = progresso[h["id"]]

                        null height 8
                        text (h["titulo"] + " — última jogada (desfecho " + p["desfecho"] + ")") size 17 color "#c8d4de" bold True

                        vbox:
                            spacing 8
                            for chave, nome in DIMENSOES:
                                $ valor = p["barras"].get(chave, 0)
                                hbox:
                                    spacing 12
                                    text nome size 14 color "#b8c4ce" min_width 300
                                    bar:
                                        value StaticValue(valor, 100)
                                        xsize 300
                                        ysize 12
                                        yalign 0.5
                                        left_bar Solid("#3E7CB1")
                                        right_bar Solid("#1a2229")

                        null height 4
                        text "Rede" size 15 color "#8FD0C6" bold True
                        hbox:
                            spacing 8
                            box_wrap True
                            for nome, estado in p["nos"].items():
                                frame:
                                    background (Solid("#14524A") if estado == "aceso" else Solid("#1a2229"))
                                    padding (8, 6)
                                    text nome size 12 color ("#B8EDE4" if estado == "aceso" else ("#8FD0C6" if estado == "contorno" else "#4a555e"))

                null height 10
                textbutton _("Apagar progresso") action Confirm("Apagar todo o progresso salvo?", yes=SetField(persistent, "progresso", {})) text_size 14

            else:
                text "Você ainda não concluiu nenhuma história. As dimensões do cuidado da sua jogada aparecem aqui ao final de cada dia." size 15 color "#8899aa" italic True


## ─────────────────────────────────────────────────────────────────────────────
## MATERIAIS (conteúdo provisório — validar com o grupo)
## ─────────────────────────────────────────────────────────────────────────────

screen materiais():

    tag menu

    use game_menu(_("Materiais"), scroll="viewport"):

        vbox:
            spacing 14

            text "Conteúdos educativos sobre a população em situação de rua e o atendimento em saúde. {i}(textos provisórios — em validação pelo grupo){/i}" size 15 color "#8899aa"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Quem é a população em situação de rua?" font gui.titulo_font size 22 color "#f0f0f0"
                text "É heterogênea: não existe um perfil único. Os motivos mais citados (dados de 2022) são problemas familiares, desemprego e uso de substâncias. A surpresa de que alguém “não parece morador de rua” é, ela mesma, um sinal de que o imaginário precisa ser revisado." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "O direito ao atendimento" font gui.titulo_font size 22 color "#f0f0f0"
                text "O SUS é universal. A Portaria GM/MS 940/2011 garante o cadastro do Cartão SUS mesmo com dados incompletos ou sem documento. Exigir endereço ou documentação para atender é uma barreira ilegal." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Registro que vira cuidado" font gui.titulo_font size 22 color "#f0f0f0"
                text "A codificação CIAP-2 e o campo de vulnerabilidade social no e-SUS fazem o caso circular pela rede: busca ativa do Consultório na Rua, vinculação à UBS de referência, prioridade nos fluxos. Texto livre é carta que não chega." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Fontes" font gui.titulo_font size 22 color "#f0f0f0"
                text "MDHC — Diagnóstico Federal 2023 · Portaria GM/MS 940/2011 · PNAB 2017 · Decreto 7053/2009 (Política Nacional para a PSR) · Política Nacional de Humanização (HumanizaSUS)." size 14 color "#8899aa" italic True


## ─────────────────────────────────────────────────────────────────────────────
## REDES DE APOIO (conteúdo provisório)
## ─────────────────────────────────────────────────────────────────────────────

screen redes_apoio():

    tag menu

    use game_menu(_("Redes de apoio"), scroll="viewport"):

        vbox:
            spacing 12

            text "Os principais serviços de atendimento e como eles se conectam. {i}(conteúdo provisório){/i}" size 15 color "#8899aa"

            for nome, desc in [
                ("UPA — Unidade de Pronto Atendimento", "urgência e emergência 24h; a prioridade é dada pela Classificação de Risco Clínica, não pela condição de moradia."),
                ("Serviço Social", "presente na UPA; é a ponte entre o atendimento clínico e o restante da rede — CNR, CRAS, Defensoria."),
                ("CNR — Consultório na Rua", "equipe que atende na rua, com busca ativa. Funciona com nome, voz e ponto combinado."),
                ("UBS — Unidade Básica de Saúde", "referência para a continuidade do cuidado: acompanhamento, renovação de receitas, saúde mental."),
                ("CRAS — Centro de Referência de Assistência Social", "documentação, benefícios e programas sociais; recebe encaminhamentos do Serviço Social."),
                ("Farmácia da UPA", "dispensação imediata da medicação na alta — garante que o paciente saia medicado."),
                ("Defensoria Pública", "assistência jurídica gratuita: regularização documental e garantia de direitos; acionada via ofício do Serviço Social com anuência do paciente.")]:

                frame:
                    background "#0d1f2dee"
                    padding (20, 12)
                    xfill True
                    has vbox
                    spacing 3
                    text nome font gui.titulo_font size 19 color "#8FD0C6"
                    text desc size 14 color "#b8c4ce"

            null height 6
            text "Caminho típico do Dia 1:  UPA → Serviço Social → CNR → UBS → CRAS/Defensoria" size 14 color "#3E7CB1" bold True


## ─────────────────────────────────────────────────────────────────────────────
## SOBRE O JOGO
## ─────────────────────────────────────────────────────────────────────────────

screen sobre_jogo():

    tag menu

    use game_menu(_("Sobre o jogo"), scroll="viewport"):

        vbox:
            spacing 14

            text "Além da Rua" font gui.titulo_font size 30 color "#f0f0f0"
            text "Um jogo sobre acolhimento, direito e empatia." size 16 color "#b8c4ce" italic True

            null height 4

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Proposta" font gui.titulo_font size 22 color "#3E7CB1"
                text "Sensibilizar e capacitar profissionais de saúde para o cuidado à população em situação de rua (PSR), por meio de histórias interativas baseadas em situações reais de atendimento." size 15 color "#b8c4ce"

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Como funcionam as histórias" font gui.titulo_font size 22 color "#3E7CB1"
                text "Em cada história você troca de perspectiva profissional (recepção, medicina, enfermagem, serviço social) e toma decisões que movem quatro dimensões do cuidado: Direito em Saúde, Conhecimento da Rede, Empatia e Acolhimento. Nenhuma delas aparece durante o jogo — todas são reveladas no epílogo, junto com o mapa da rede." size 15 color "#b8c4ce"
                text "O jogo não avalia certo ou errado: as escolhas abrem reflexões sobre o cuidado, e as dimensões aparecem só no fim de cada dia." size 13 color "#8899aa" italic True

            frame:
                background "#0d1f2dee"
                padding (22, 16)
                xfill True
                has vbox
                spacing 6
                text "Quem faz" font gui.titulo_font size 22 color "#3E7CB1"
                text "PET-Saúde · Grupo Tutorial 6 — Pop Rua · Universidade Federal da Paraíba (UFPB), em parceria com a rede de saúde do território." size 15 color "#b8c4ce"
