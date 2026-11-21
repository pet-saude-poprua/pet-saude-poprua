## telas_menu.rpy — Telas de menu: Casos, Progresso, Materiais,
## Redes de apoio e Sobre o jogo (estrutura de docs/estrutura-telas.md).
## Materiais e Redes de apoio resumem o card de contexto real do roteiro v4.

## O progresso fica em persistent.progresso (ver game/nucleo/estado.rpy):
## {id_da_historia: {"desfecho", "barras", "nos", "vezes"}}.


## ─────────────────────────────────────────────────────────────────────────────
## CASOS — uma ficha por história registrada (game/historias/<nome>/dados.rpy).
## ─────────────────────────────────────────────────────────────────────────────

screen casos():

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
                                text "não concluída" size 13 color "#8899aa" italic True yalign 0.5

                        text h["titulo"] font gui.titulo_font size 26 color "#f0f0f0"
                        text h["sinopse"] size 15 color "#b8c4ce"

                        null height 6
                        textbutton _("Jogar esta história  ›") action Start(h["label"]) text_size 17

                        if MOSTRAR_ATALHOS_TESTE and h["atalhos"]:
                            hbox:
                                spacing 14
                                text "Atalhos para teste:" size 13 color "#6f8494" italic True yalign 0.5
                                for rotulo, destino in h["atalhos"]:
                                    textbutton rotulo action Start(destino) text_size 13

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
## MATERIAIS — resumo do card de contexto real do roteiro v4 (revisão de 21/11/2026)
## ─────────────────────────────────────────────────────────────────────────────

screen materiais():

    tag menu

    use game_menu(_("Materiais"), scroll="viewport"):

        vbox:
            spacing 14

            text "Conteúdos sobre a população em situação de rua e o atendimento em saúde, os mesmos do card “Contexto real” ao fim de cada história." size 15 color "#8899aa"

            for titulo, corpo in [
                ("Quem é a população em situação de rua?", "É heterogênea: não existe um perfil único. Entre os motivos mais declarados para estar na rua estão problemas familiares, desemprego, álcool e/ou outras drogas e perda de moradia, muitas vezes combinados (CadÚnico, dezembro de 2022). Quando alguém diz que uma pessoa “nem parece” estar na rua, está partindo de uma imagem pronta dessa população."),
                ("O direito ao atendimento", "O SUS é universal. A falta de documento, de Cartão SUS ou de endereço não pode impedir o atendimento, e o CPF é o número de identificação no SUS. Na UBS, a pessoa em situação de rua não precisa comprovar endereço: o cadastro pode usar um endereço de referência, como o do Centro POP."),
                ("Registro que vira cuidado", "Registrar a situação de rua no prontuário, em linguagem objetiva e no campo certo, orienta quem atende depois sem expor a pessoa. Na UPA, o médico registra e aciona o Serviço Social, que comunica o caso ao Consultório na Rua com o consentimento da pessoa."),
                ("Fontes", "MDHC, População em situação de rua: diagnóstico com base nos dados e informações disponíveis em registros administrativos e sistemas do Governo Federal (2023) · Portaria GM/MS 940/2011 · Lei 14.534/2023 · Decreto 7.053/2009 · Tipificação Nacional de Serviços Socioassistenciais (Resolução CNAS 109/2009) · PNH/HumanizaSUS · comentários da equipe do Consultório na Rua de João Pessoa (novembro de 2026)."),
            ]:
                frame:
                    background "#0d1f2dee"
                    padding (22, 16)
                    xfill True
                    has vbox
                    spacing 6
                    text titulo font gui.titulo_font size 22 color "#f0f0f0"
                    text corpo size (14 if titulo == "Fontes" else 15) color ("#8899aa" if titulo == "Fontes" else "#b8c4ce") italic (titulo == "Fontes")


## ─────────────────────────────────────────────────────────────────────────────
## REDES DE APOIO — serviços do roteiro v4, com o fluxo de João Pessoa
## ─────────────────────────────────────────────────────────────────────────────

screen redes_apoio():

    tag menu

    use game_menu(_("Redes de apoio"), scroll="viewport"):

        vbox:
            spacing 12

            text "Os serviços que aparecem nas histórias e como eles se conectam, no fluxo da rede de João Pessoa." size 15 color "#8899aa"

            for nome, desc in [
                ("UPA — Unidade de Pronto Atendimento", "Urgência e emergência, 24 horas. A prioridade vem da classificação de risco, por critérios clínicos; a condição social não muda a cor. A farmácia da UPA não entrega remédio para depois da alta."),
                ("Serviço Social da UPA", "Faz a entrevista social, aciona o Consultório na Rua por mensagem, com o consentimento da pessoa, e encaminha por escrito à assistência social (Centro POP)."),
                ("Consultório na Rua", "Equipe da atenção primária (enfermeiro, médico, assistente social, psicólogo e agente social) que atende a pessoa onde ela está e faz a ponte com a UBS. Em João Pessoa, recebe os casos por mensagem, em dias úteis, das 8h às 19h."),
                ("UBS — Unidade Básica de Saúde", "Referência para a continuidade do cuidado: acompanhamento da pressão, receitas e saúde mental. O remédio da receita do SUS sai de graça na farmácia de qualquer UBS, sem Cartão SUS."),
                ("Centro POP", "Serviço da assistência social: documentação civil, CadÚnico, benefícios, guarda de pertences e endereço de referência. Em João Pessoa, na Rua Treze de Maio, 508, Centro, das 8h às 17h."),
                ("Casa de acolhimento", "Cama, banho e comida. Em João Pessoa, o acesso às Casas de Acolhida é pelo Centro POP, pela abordagem social ou pelo Consultório na Rua.")]:

                frame:
                    background "#0d1f2dee"
                    padding (20, 12)
                    xfill True
                    has vbox
                    spacing 3
                    text nome font gui.titulo_font size 19 color "#8FD0C6"
                    text desc size 14 color "#b8c4ce"

            null height 6
            text "Caminho do Dia 1: UPA › Serviço Social › Consultório na Rua › UBS, com o Centro POP e o acolhimento pela assistência social." size 14 color "#3E7CB1" bold True


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
