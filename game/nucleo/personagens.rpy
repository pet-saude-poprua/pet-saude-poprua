## nucleo/personagens.rpy — Personagens comuns, cenários, sprites e transforms
## Personagens próprios de uma história ficam na pasta dela
## (ex.: game/historias/renato/dados.rpy define Renato).
## Regra do roteiro: a narração não marca o gênero do profissional jogável;
## os nomes exibidos usam a forma "(a)".

init -5 python:
    ## A arte da caixa (1280x170) vira Frame para acompanhar gui.textbox_height:
    ## como Image de tamanho fixo, falas de 4 linhas vazavam para fora da caixa
    ## no celular, onde a fonte é maior.
    def textbox_frame():
        return Frame("gui/textbox.webp", 120, 45)

    def textbox_tinted(accent):
        ## Caixa de diálogo aquarela com uma pincelada fina na cor do personagem
        ## sob a área do nome.
        return Fixed(
            textbox_frame(),
            Transform(Solid(accent + "cc"), xysize=(150, 3), xpos=110, ypos=50),
        )

## Narrador (sem nome, itálico)
define narr   = Character(None, what_italic=True, what_color="#dddddd",
                          window_background=textbox_frame())

## Perspectivas jogáveis ("você")
define recep  = Character("Recepcionista (você)",
                          color="#A9C7E8",
                          window_background=textbox_tinted("#4A7FB5"))
define enf    = Character("Enfermeiro(a) (você)",
                          color="#A8D8AE",
                          window_background=textbox_tinted("#5E8C61"))
define med    = Character("Médico(a) (você)",
                          color="#D87E7E",
                          window_background=textbox_tinted("#A55858"))
define tec    = Character("Técnico(a) de Enfermagem (você)",
                          color="#A8D8AE",
                          window_background=textbox_tinted("#7CA982"))
define assist_voce = Character("Assistente Social (você)",
                          color="#D9B080",
                          window_background=textbox_tinted("#B38B59"))

## Equipe (não jogável)
define assist     = Character("Assistente Social",
                              color="#D9B080",
                              window_background=textbox_tinted("#B38B59"))
define colega_enf = Character("Colega da enfermagem",
                              color="#C8D8B0",
                              window_background=textbox_tinted("#7F9A5E"))

## ── Backgrounds aquarela (padrão visual aprovado em 01/07) ───────────────────
image bg aqua_fachada     = "bg/aqua_fachada.jpg"
image bg aqua_recepcao    = "bg/aqua_recepcao.jpg"
image bg aqua_espera      = "bg/aqua_espera.jpg"
image bg aqua_balcao      = "bg/aqua_balcao.jpg"
image bg aqua_consultorio = "bg/aqua_consultorio.jpg"
image bg aqua_box         = "bg/aqua_box.jpg"
image bg aqua_corredor    = "bg/aqua_corredor.jpg"
image bg aqua_saida       = "bg/aqua_saida.jpg"
image bg neutro_cor       = "bg/neutro_cor.webp"
image bg neutro_quente    = "bg/neutro_quente.webp"
image bg neutro_frio      = "bg/neutro_frio.webp"

## Fundos provisórios até existir arte própria (Apêndice B-j do roteiro v4)
image bg aqua_classificacao  = "bg/aqua_consultorio.jpg"
image bg aqua_observacao     = "bg/aqua_box.jpg"
image bg aqua_servico_social = "bg/aqua_consultorio.jpg"

## Overlay do e-SUS (tela de registro)
image esus = "bg/aqua_esus.jpg"

## ── Sprites de Renato (2816x1536, recorte com alpha) ─────────────────────────
image renato normal     = "chars/renato_normal.webp"
image renato hesitante  = "chars/renato_hesitante.webp"
image renato aberto     = "chars/renato_aberto.webp"
image renato despedida  = "chars/renato_despedida.webp"

## ── Sprites da equipe e NPCs ─────────────────────────────────────────────────
image assistente     = "chars/assistente_social.webp"
image senhora        = "chars/senhora.webp"

## Médico de plantão da UPA (meio-corpo, 747x1232 — recorte já sem margens)
image medico_upa     = "chars/medico_upa.webp"

## ── Objetos das cenas (recorte com alpha) ────────────────────────────────────
image caderno  = "obj/caderno_renato.webp"
image receita  = "obj/obj_receita_medica.webp"

## ── Fundo de cor sólida (encerramento) ───────────────────────────────────────
image bg_preto    = Solid("#080808")

## ── Transforms de posicionamento ─────────────────────────────────────────────
## Os sprites 2816x1536 têm margens transparentes largas com a figura no centro
## do canvas — por isso ancoramos pelo CENTRO da imagem (xanchor 0.5) e
## posicionamos com xpos, para a figura cair onde se espera.
## zoom 0.35 → figura com ~505px de altura na tela (referência: Renato).
transform left:
    xanchor 0.5
    xpos 0.16
    yalign 1.0
    zoom 0.35

transform center:
    xanchor 0.5
    xpos 0.5
    yalign 1.0
    zoom 0.35

transform right:
    xanchor 0.5
    xpos 0.82
    yalign 1.0
    zoom 0.35

## Sprite de meio-corpo (medico_upa, 747x1232): a figura já vem sem margens e é
## cortada na altura da coxa — fica em primeiro plano, no centro da tela,
## encostando na borda inferior. zoom 0.42 → ~517px de altura.
transform primeiro_plano_centro:
    xanchor 0.5
    xpos 0.5
    yalign 1.0
    zoom 0.42

## Sprites novos 1024x1536 (figura ocupa o canvas inteiro): zoom calibrado para
## ficarem um pouco MENORES que o Renato (504px) — senhora 0.31≈465px,
## outro paciente 0.33≈494px.
transform left_np(z=0.32):
    xanchor 0.5
    xpos 0.16
    yalign 1.0
    zoom z

## Objeto em destaque (1024x1024)
transform obj_dir:
    xalign 0.68
    yalign 0.45
    zoom 0.36

## overlay e-SUS (1600x900 sobre 1280x720): zoom 0.8 cobre a tela exatamente.
## Opaco de propósito — com alpha < 1 os sprites atrás vazam como fantasma
## por cima da ficha.
transform overlay_esus:
    xalign 0.5
    yalign 0.5
    zoom 0.8


## ─────────────────────────────────────────────────────────────────────────────
## Arte sem uso no roteiro v4 — mantida até a revisão de arte com a equipe.
## Os arquivos continuam em game/images; apagar só depois dessa decisão.
## ─────────────────────────────────────────────────────────────────────────────
image bg titulo           = "bg/menu_upa.jpg"
image bg neutro_corredor  = "bg/neutro_corredor.webp"
image renato emocionado = "chars/renato_emocionado.webp"
image tecnica        = "chars/tecnica.webp"
image medico         = "chars/medico.webp"
image senhora_fofoqueira = "chars/SenhoraFofoqueira.webp"
image senhor_fofoqueiro  = "chars/SenhorFofoqueiro.webp"
image renato_fofocado    = "chars/RenatoFofocado.webp"
image recepcionista_chamando_renato = "chars/RecepcionistaChamandoRenato.webp"
image outro_paciente = "chars/outro_paciente.webp"
image consulta_medico_renato = "chars/consulta_medico_renato.webp"
image carteira = "obj/obj_carteira_trabalho.webp"
image cartao   = "obj/obj_cartao_sus.webp"

## Ilustração de cena (1536x1024) ocupando a altura da tela, centralizada.
## zoom 0.7031 → 1080x720; o fundo aparece nas laterais.
transform ilustracao_centro:
    xalign 0.5
    yalign 1.0
    zoom 0.7031

transform right_np(z=0.32):
    xanchor 0.5
    xpos 0.84
    yalign 1.0
    zoom z

transform obj_centro:
    xalign 0.5
    yalign 0.42
    zoom 0.45

transform obj_esq:
    xalign 0.32
    yalign 0.42
    zoom 0.42
