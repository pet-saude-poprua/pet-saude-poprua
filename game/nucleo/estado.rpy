## nucleo/estado.rpy — Estado de jogo comum às cinco histórias
##
## Cada história se registra com registrar_historia() (ver
## game/historias/renato/dados.rpy) e descreve as próprias decisões numa
## tabela no formato do Apêndice D do roteiro:
##
##     DECISOES = {
##         1: {"A": ((+1, +1, +1, +1), []),
##             "B": ((-1,  0, -1,  0), ["exposto_recepcao"])},
##         ...
##     }
##
## Os números são as unidades dos medidores na ordem
## (DIREITO, REDE, EMPATIA, ACOLHIMENTO): ▲ = +1, ▲▲ = +2, ▼ = −1 etc.
## A mesma tabela é lida pelo simulador (scripts/simular_historia.py) no CI,
## para que roteiro, jogo e teste não divirjam.

init -10 python:

    DIMENSOES = (
        ("direito", "Direito em Saúde"),
        ("rede", "Conhecimento da Rede"),
        ("empatia", "Empatia / Sensibilidade Social"),
        ("acolhimento", "Acolhimento"),
    )

    HISTORIAS = {}

    def registrar_historia(id, **dados):
        """Registra uma história. Campos usados pelo núcleo:
        ordem, titulo, subtitulo, sinopse, label (início), decisoes, nos,
        atalhos (lista de (rótulo, label) para os testes de usabilidade) e
        jogavel (False = aparece em Casos como "em desenvolvimento")."""
        dados["id"] = id
        dados.setdefault("jogavel", True)
        dados.setdefault("atalhos", [])
        dados.setdefault("decisoes", {})
        dados.setdefault("nos", [])
        HISTORIAS[id] = dados

    def historias_em_ordem():
        return sorted(HISTORIAS.values(), key=lambda h: h.get("ordem", 99))

    def historia():
        return HISTORIAS[store.historia_atual]

    ## ── Início de uma história ────────────────────────────────────────────────

    def iniciar_historia(id):
        h = HISTORIAS[id]
        store.historia_atual = id
        store.medidores = {k: 0 for k, _ in DIMENSOES}
        store.flags = set()
        store.escolhas = {}
        store.nos_rede = {n: "apagado" for n in h["nos"]}
        store.pontos_retomada = {}
        store.olhar_atual = ""
        store.desfecho = ""

    ## ── Decisões e flags ──────────────────────────────────────────────────────

    def escolher(n, opcao):
        """Aplica a opção da decisão n: soma os efeitos nos medidores e grava
        as flags da tabela da história."""
        efeitos, novas_flags = historia()["decisoes"][n][opcao]
        for (k, _), v in zip(DIMENSOES, efeitos):
            store.medidores[k] += v
        store.escolhas[n] = opcao
        for f in novas_flags:
            store.flags.add(f)

    def tem(*nomes):
        """True se alguma das flags estiver gravada."""
        return any(f in store.flags for f in nomes)

    ## ── Medidores ─────────────────────────────────────────────────────────────

    def barras():
        """Barras de 0 a 100, normalizadas sobre TODAS as decisões da história
        (decisões não jogadas contam 0), como no Quadro D2 do roteiro."""
        dec = historia()["decisoes"]
        out = {}
        for i, (k, _) in enumerate(DIMENSOES):
            mn = sum(min(v[0][i] for v in d.values()) for d in dec.values())
            mx = sum(max(v[0][i] for v in d.values()) for d in dec.values())
            if mx == mn:
                out[k] = 100
            else:
                out[k] = int(round(100.0 * (store.medidores[k] - mn) / (mx - mn)))
        return out

    ## ── Mapa da rede ──────────────────────────────────────────────────────────

    def acender(*nos):
        for n in nos:
            store.nos_rede[n] = "aceso"

    def contornar(*nos):
        """Nó que entrou no caso depois do dia jogado."""
        for n in nos:
            if store.nos_rede.get(n) != "aceso":
                store.nos_rede[n] = "contorno"

    ## ── "Retomar a partir desta decisão" ──────────────────────────────────────

    def guardar_ponto(n):
        """Guarda o estado imediatamente antes da decisão n."""
        store.pontos_retomada[n] = {
            "medidores": dict(store.medidores),
            "flags": set(store.flags),
            "escolhas": dict(store.escolhas),
            "nos": dict(store.nos_rede),
        }

    def restaurar_ponto(n):
        p = store.pontos_retomada[n]
        store.medidores = dict(p["medidores"])
        store.flags = set(p["flags"])
        store.escolhas = dict(p["escolhas"])
        store.nos_rede = dict(p["nos"])

    ## ── Perspectiva ("Seu olhar", issue #90) ──────────────────────────────────

    def olhar(papel):
        store.olhar_atual = papel

    ## ── Progresso persistente ─────────────────────────────────────────────────

    def concluir_historia(desfecho):
        id = store.historia_atual
        progresso = dict(persistent.progresso or {})
        anterior = progresso.get(id, {})
        progresso[id] = {
            "desfecho": desfecho,
            "barras": barras(),
            "nos": dict(store.nos_rede),
            "vezes": anterior.get("vezes", 0) + 1,
        }
        persistent.progresso = progresso
        renpy.save_persistent()


default historia_atual = ""
default medidores = {"direito": 0, "rede": 0, "empatia": 0, "acolhimento": 0}
default flags = set()
default escolhas = {}
default nos_rede = {}
default pontos_retomada = {}
default olhar_atual = ""
default desfecho = ""

default persistent.progresso = {}

## Atalhos de teste em Casos (cada história declara os seus em registrar_historia).
## Desligar antes da versão de coleta de dados.
define MOSTRAR_ATALHOS_TESTE = True
