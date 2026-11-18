## nucleo/telas.rpy — Telas comuns às histórias
## Cartão de reflexão e de RESULTADO, indicador "Seu olhar", mensagem de
## celular, página do caderno, contexto real e painel final (medidores + mapa).

## ─────────────────────────────────────────────────────────────────────────────
## Cartão (reflexão entre cenas e RESULTADO depois de cada escolha)
## ─────────────────────────────────────────────────────────────────────────────

screen card(titulo, linha1, linha2=""):
    zorder 130
    modal True

    add Solid("#04101a")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 920
        background Solid("#0d1f2de8")
        padding (60, 50, 60, 50)

        has vbox
        spacing 20
        xfit False

        text "[titulo]" size 15 color "#3E7CB1" bold True xalign 0.5 outlines [(1, "#000000", 0, 0)]

        add Solid("#3E7CB1", xysize=(800, 2)) xalign 0.5

        null height 6

        text "[linha1!q]" size 22 color "#eaeaea" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        if linha2:
            null height 8
            text "[linha2!q]" size 22 color "#c8d8e8" italic True xalign 0.5 textalign 0.5 layout "subtitle"

        null height 16

        textbutton "Continuar  ›" action Return() xalign 0.5 text_size 16 text_color "#3E7CB1" text_hover_color "#ffffff"


label reflexao(linha1, linha2=""):
    window hide
    call screen card("REFLEXÃO", linha1, linha2) with dissolve
    return

label resultado(texto):
    window hide
    call screen card("RESULTADO", texto) with dissolve
    return


## ─────────────────────────────────────────────────────────────────────────────
## "Seu olhar" — qual profissional o jogador acompanha agora (issue #90)
## ─────────────────────────────────────────────────────────────────────────────

screen seu_olhar():
    zorder 50

    if olhar_atual:
        frame:
            xpos 16
            ypos 14
            background Solid("#0d1f2dcc")
            padding (14, 7)
            hbox:
                spacing 8
                text "SEU OLHAR" size 12 color "#7fb3d9" bold True yalign 0.5
                text "[olhar_atual!q]" size 15 color "#f0f0f0" yalign 0.5


## ─────────────────────────────────────────────────────────────────────────────
## Mensagem no celular do serviço (sem marca de aplicativo)
## ─────────────────────────────────────────────────────────────────────────────

screen mensagem_celular(rotulo, texto):
    zorder 110
    modal True

    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.42
        xsize 520
        background Solid("#1b2630")
        padding (26, 22)

        has vbox
        spacing 12

        text "[rotulo!q]" size 13 color "#8fa6b8" bold True
        frame:
            background Solid("#2d4a5e")
            padding (18, 14)
            xfill True
            text "[texto!q]" size 19 color "#f0f0f0"
        textbutton "Continuar  ›" action Return() xalign 1.0 text_size 15 text_color "#7fb3d9" text_hover_color "#ffffff"


label mensagem(rotulo, texto):
    window hide
    call screen mensagem_celular(rotulo, texto) with dissolve
    return


## ─────────────────────────────────────────────────────────────────────────────
## Página de caderno (epílogo)
## ─────────────────────────────────────────────────────────────────────────────

screen pagina_caderno(linhas):
    zorder 120
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        background Solid("#f3ecd9")
        padding (56, 40)

        has vbox
        spacing 8

        for linha in linhas:
            text "[linha!q]" size 21 color "#2a3540" italic True

        null height 12
        textbutton "Continuar  ›" action Return() xalign 1.0 text_size 15 text_color "#3E7CB1" text_hover_color "#1d3d5c"


## ─────────────────────────────────────────────────────────────────────────────
## Contexto real — conteúdo vem da história: lista de (título, [parágrafos])
## ─────────────────────────────────────────────────────────────────────────────

screen contexto_real(titulo, subtitulo, blocos, fontes):
    zorder 130
    modal True

    add Solid("#04101a")

    viewport:
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 680
        mousewheel True
        draggable True
        scrollbars "vertical"
        pagekeys True

        frame:
            xsize 1080
            background "#00000000"
            padding (60, 40, 60, 40)
            has vbox
            spacing 12

            text "[titulo!q]" size 22 color "#3E7CB1" bold True xalign 0.5
            text "[subtitulo!q]" size 16 color "#7a9ab0" italic True xalign 0.5
            null height 4
            add Solid("#3E7CB1", xysize=(960, 2)) xalign 0.5

            for nome, paragrafos in blocos:
                null height 8
                text "[nome!q]" size 19 color "#dddddd" bold True
                for p in paragrafos:
                    text "[p!q]" size 18 color "#cccccc" layout "subtitle"

            null height 10
            add Solid("#2a3a4a", xysize=(960, 1)) xalign 0.5
            null height 6
            text "[fontes!q]" size 13 color "#5a7a8a" italic True

            null height 20
            textbutton "Continuar  ›" action Return() xalign 0.5 text_size 17 text_color "#3E7CB1" text_hover_color "#ffffff"
            null height 20


## ─────────────────────────────────────────────────────────────────────────────
## Painel final — quatro barras + mapa da rede (aceso / contorno / apagado)
## ─────────────────────────────────────────────────────────────────────────────

define COR_DIMENSAO = {
    "direito": ("#E8C97A", "#C4A55A"),
    "rede": ("#8FD0C6", "#4E9A8E"),
    "empatia": ("#D8A8B8", "#B07286"),
    "acolhimento": ("#9BC5E0", "#5C8FB3"),
}

screen painel_final(titulo_mapa):
    zorder 120
    modal True

    $ valores = barras()

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        background "#000000cc"
        padding (36, 26)

        has vbox
        spacing 14

        text "As dimensões do cuidado" size 20 bold True color "#ffffff" xalign 0.5
        text "Estas barras mostram como as condutas desta jogada moveram cada dimensão do cuidado. Não há pontuação a vencer: cada barra é um convite para olhar de novo para um momento do dia." size 14 color "#a8b8c8" italic True xalign 0.5 textalign 0.5

        null height 4

        hbox:
            spacing 26
            xalign 0.5

            for chave, nome in DIMENSOES:
                $ claro, escuro = COR_DIMENSAO[chave]
                vbox:
                    spacing 4
                    xsize 205
                    text nome.upper() size 12 color claro bold True
                    bar:
                        value StaticValue(valores[chave], 100)
                        xsize 200
                        ysize 12
                        left_bar Solid(escuro)
                        right_bar Solid("#222")

        null height 8
        add Solid("#2a3a4a", xysize=(900, 1)) xalign 0.5

        text "[titulo_mapa!q]" size 16 bold True color "#8FD0C6" xalign 0.5

        hbox:
            xalign 0.5
            spacing 10
            box_wrap True
            for nome, estado in nos_rede.items():
                if estado == "aceso":
                    frame:
                        background Solid("#14524A")
                        padding (10, 7)
                        text nome size 13 color "#B8EDE4" bold True
                elif estado == "contorno":
                    frame:
                        background Solid("#4E9A8E")
                        padding (2, 2)
                        frame:
                            background Solid("#0d1f2d")
                            padding (8, 5)
                            text nome size 13 color "#8FD0C6"
                else:
                    frame:
                        background Solid("#1a2229")
                        padding (10, 7)
                        text nome size 13 color "#4a555e"

        text "Aceso: entrou no caso hoje · contorno: entrou depois · apagado: não entrou" size 12 color "#6f8494" italic True xalign 0.5

        null height 8
        textbutton "Continuar  ›" action Return() xalign 0.5 text_size 16 text_color "#3E7CB1" text_hover_color "#ffffff"


## ─────────────────────────────────────────────────────────────────────────────
## Encerramento comum (grava o progresso e volta ao menu)
## ─────────────────────────────────────────────────────────────────────────────

label encerrar_historia(desfecho_final):
    $ concluir_historia(desfecho_final)
    hide screen seu_olhar
    scene bg_preto with fade
    centered "{color=#888888}{size=-2}Dia concluído. Obrigado por jogar esta versão de testes.{/size}{/color}"
    return
