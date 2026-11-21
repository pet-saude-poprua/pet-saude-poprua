## nucleo/inicio.rpy — Ponto de entrada do jogo "Além da Rua"
##
## "Jogar" no menu principal começa aqui: a abertura conceitual aparece uma vez
## e o jogo segue para a primeira história jogável. Pelo menu "Casos", cada
## história começa direto no label dela (ver iniciar_historia em estado.rpy).

default persistent.abertura_vista = False

label start:
    if not persistent.abertura_vista:
        call tela_conceitual_psr
        $ persistent.abertura_vista = True

    python:
        primeira = [h for h in historias_em_ordem() if h["jogavel"]][0]
    jump expression primeira["label"]


## ── Abertura conceitual (texto do roteiro do Renato, seção 6.1) ──────────────
label tela_conceitual_psr:
    scene bg neutro_cor with fade
    window show

    narr "{b}Antes de começar.{/b}"
    narr "A população em situação de rua é heterogênea: não existe um perfil único. Entre os motivos mais frequentemente relatados para estar em situação de rua estão os conflitos familiares, o desemprego e o uso de álcool e outras drogas, muitas vezes combinados."
    narr "Neste jogo, você acompanhará o atendimento sob diferentes perspectivas profissionais. A história vai mostrar como o olhar, a linguagem e as atitudes da equipe podem aproximar ou afastar uma pessoa do cuidado."
    narr "Ao longo do dia, observe quatro dimensões do cuidado: Direito em Saúde, Conhecimento da Rede, Empatia e Acolhimento. Entre algumas cenas, uma reflexão curta aponta o que fez diferença no atendimento e o que costuma dar errado no dia a dia dos serviços."

    window hide
    return
