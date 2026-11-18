## historias/renato/dados.rpy — Dia 1: Renato (roteiro v4, revisão de 19/11/2026)
## Registro da história, tabela de decisões (Apêndice D, Quadro D1),
## regras de desfecho (Quadro D3), nós do mapa (Quadro D4) e caderno (Quadro D5).
## Roteiro: Google Doc "ROTEIRO-VISUAL-NOVEL-v4 – Renato (corrigido + decisões)".

define renato = Character("Renato",
                          color="#9BC5E0",
                          window_background=textbox_tinted("#5C8FB3"))

init python:

    ## BEGIN DECISOES_RENATO (lido por scripts/simular_historia.py)
    DECISOES_RENATO = {
        1: {"A": ((1, 1, 1, 1), []),
            "B": ((-1, 0, -1, 0), ["exposto_recepcao"]),
            "C": ((-2, 0, -1, -1), ["barreira_doc"])},
        2: {"A": ((-1, 0, 1, 0), ["fura_protocolo"]),
            "B": ((2, 0, 1, 2), []),
            "C": ((0, 0, -1, -2), ["sem_orientacao"])},
        3: {"A": ((-1, 0, -1, -1), ["sem_reavaliacao"]),
            "B": ((-2, -1, 0, -1), ["liberado_espera"]),
            "C": ((2, 0, 1, 2), [])},
        4: {"A": ((0, -1, -1, -1), ["sem_saude_mental"]),
            "B": ((0, 0, 1, -1), ["sedativo", "sem_saude_mental"]),
            "C": ((1, 1, 2, 2), [])},
        5: {"A": ((0, 1, 1, 2), []),
            "B": ((0, -1, -1, -1), ["sem_repasse"])},
        6: {"A": ((-1, 0, 1, 0), ["exposto_obs"]),
            "B": ((1, 0, 2, 1), []),
            "C": ((-1, 0, -2, -1), ["exposto_obs"])},
        7: {"A": ((1, -2, 0, -1), ["sem_ss"]),
            "B": ((1, 3, 0, 2), []),
            "C": ((0, 1, -1, -2), ["ss_sem_renato"])},
        8: {"A": ((2, 2, 1, 0), []),
            "B": ((0, -2, 0, -1), ["sem_registro"])},
        9: {"A": ((1, 0, 0, 1), []),
            "B": ((-2, 1, -1, -1), ["renato_sem_saber"]),
            "C": ((2, 3, 1, 2), [])},
        10: {"A": ((2, 2, 0, 1), []),
             "B": ((1, -1, 0, -1), ["sem_encaminhamento"]),
             "C": ((0, -1, 0, 0), ["adiado_cnar"])},
        11: {"A": ((0, -1, 1, -1), ["sem_plano_b"]),
             "B": ((0, 2, 1, 2), []),
             "C": ((0, -1, 1, 1), ["plano_b_upa"])},
    }
    CANONICA_RENATO = {1: "A", 2: "B", 3: "C", 4: "C", 5: "A", 6: "B",
                       7: "B", 8: "A", 9: "C", 10: "A", 11: "B"}
    ## END DECISOES_RENATO

    NOS_RENATO = [
        "UPA",
        "Serviço Social da UPA",
        "Consultório na Rua",
        "Centro POP",
        "Casa de acolhimento",
        "UBS de referência",
    ]

    registrar_historia(
        "renato",
        ordem=1,
        titulo="Renato",
        subtitulo="Dia 1 · UPA",
        sinopse="Renato, 54 anos, chega à UPA com dor de cabeça forte e o coração disparado. Da recepção ao Serviço Social, você acompanha o atendimento pelo olhar de cinco profissionais.",
        label="renato",
        decisoes=DECISOES_RENATO,
        nos=NOS_RENATO,
    )

    ## Histórias seguintes: aparecem em "Casos" como em desenvolvimento.
    registrar_historia("cleide", ordem=2, titulo="Cleide", subtitulo="Dia 2 · UBS",
                       sinopse="Em validação com a equipe de saúde.", jogavel=False)
    registrar_historia("historia3", ordem=3, titulo="História 3", subtitulo="Dia 3",
                       sinopse="Roteiro em elaboração.", jogavel=False)
    registrar_historia("historia4", ordem=4, titulo="História 4", subtitulo="Dia 4",
                       sinopse="Roteiro em elaboração.", jogavel=False)
    registrar_historia("historia5", ordem=5, titulo="História 5", subtitulo="Dia 5",
                       sinopse="Roteiro em elaboração.", jogavel=False)

    def renato_desfecho():
        """Quadro D3 (regras em ordem). O Desfecho C é decidido na Cena 3."""
        if tem("sem_ss", "ss_sem_renato"):
            return "B"
        if tem("renato_sem_saber") and escolhas.get(10) != "A" and escolhas.get(11) != "B":
            return "B"
        return "A"

    def renato_nos(desfecho_final):
        """Quadro D4 — estado final de cada nó no mapa."""
        acender("UPA")
        if desfecho_final == "C":
            return
        if escolhas.get(7) in ("B", "C"):
            acender("Serviço Social da UPA", "Consultório na Rua")
        if escolhas.get(10) in ("A", "B"):
            acender("Centro POP")
        elif desfecho_final == "A":
            contornar("Centro POP")
        if escolhas.get(10) == "A":
            acender("Casa de acolhimento")
        elif desfecho_final == "A":
            contornar("Casa de acolhimento")
        if desfecho_final == "A":
            contornar("UBS de referência")

    def renato_caderno(desfecho_final):
        """Quadro D5 — página do caderno de Renato conforme o caminho."""
        L = ["Quarta-feira. UPA."]
        L.append("Pressão 182 por 120. " + ("Pulseira laranja." if tem("fura_protocolo") else "Pulseira amarela."))
        if desfecho_final == "C":
            L.append("Muita gente. Fui embora.")
            L.append("Segunda-feira. UPA de novo.")
            return L
        if tem("sem_reavaliacao"):
            L.append("Pensei em ir embora. Mandaram esperar. Esperei.")
        else:
            L.append("Pensei em ir embora. Mediram de novo. Explicaram a demora. Fiquei.")
        if not tem("sem_saude_mental"):
            L.append("Contei pro médico que não durmo.")
            L.append("Remédio pra depressão tem no SUS.")
        if tem("sedativo"):
            L.append("Remédio pra dormir.")
        L.append("11h40: 172 por 106. 12h10: 164 por 100.")
        L.append("12h40: 160 por 98. 13h10: 156 por 96. 13h40: 150 por 94. 14h10: 148 por 92.")
        if tem("sem_repasse"):
            L.append("Remédio da pressão: de graça no posto.")
        else:
            L.append("Remédio da pressão: de graça no posto. Ver quem guarda a cartela.")
        if tem("sem_ss"):
            L.append("Procurar o posto mais perto.")
            return L
        if tem("ss_sem_renato"):
            L.append("A assistente social vai me procurar.")
            return L
        if not tem("renato_sem_saber"):
            L.append("Consultório na Rua. Marcos. Amanhã de manhã, coreto. Levar receita.")
        if tem("adiado_cnar"):
            L.append("Documento: ver com a equipe.")
        elif tem("sem_encaminhamento"):
            L.append("Centro POP: Rua Treze de Maio, até as 5.")
        else:
            L.append("Centro POP hoje, até as 5. Levar o encaminhamento.")
        if tem("plano_b_upa"):
            L.append("Se não der certo: voltar na UPA.")
        elif not tem("sem_plano_b"):
            L.append("Se não encontrar a equipe: Centro POP.")
        return L


## ── Atalhos para o teste de usabilidade (Apêndice B-l) ──────────────────────
## Começam a história numa cena com as escolhas canônicas anteriores já
## aplicadas. Aparecem em Casos enquanto MOSTRAR_ATALHOS_TESTE for True.

define MOSTRAR_ATALHOS_TESTE = True
define RENATO_ATALHOS = [("Cena 4", "renato_atalho_cena4"),
                         ("Cena 6", "renato_atalho_cena6"),
                         ("Cena 7", "renato_atalho_cena7")]

init python:
    def renato_preparar_atalho(ate_decisao):
        iniciar_historia("renato")
        for n in range(1, ate_decisao + 1):
            escolher(n, CANONICA_RENATO[n])

label renato_atalho_cena4:
    $ renato_preparar_atalho(3)
    show screen seu_olhar
    play music "audio/music/ambiente_upa.ogg" fadein 2.0
    jump renato_cena4

label renato_atalho_cena6:
    $ renato_preparar_atalho(6)
    show screen seu_olhar
    play music "audio/music/ambiente_upa.ogg" fadein 2.0
    jump renato_cena6

label renato_atalho_cena7:
    $ renato_preparar_atalho(8)
    show screen seu_olhar
    play music "audio/music/ambiente_upa.ogg" fadein 2.0
    jump renato_cena7
