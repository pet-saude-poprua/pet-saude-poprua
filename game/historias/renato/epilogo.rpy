## historias/renato/epilogo.rpy — Dia 1: Renato · Epílogo e desfechos (6.10)
## Sequência: contexto real → reflexão → caderno → medidores e mapa →
## desfecho (A, B ou C) → "Retomar" (saídas antecipadas) → encerramento.

define RENATO_CONTEXTO = [
    ("Quem é essa população", [
        "Em dezembro de 2022, 236,4 mil pessoas em situação de rua estavam inscritas no CadÚnico: 87% homens e 68% pessoas negras. Os motivos mais declarados para estar na rua eram problemas familiares (44%), desemprego (39%), álcool e/ou outras drogas (29%) e perda de moradia (23%), muitas vezes combinados. Em maio de 2026, o CadÚnico registrava cerca de 389 mil pessoas em situação de rua.",
        "A situação de rua não tem uma aparência única. Quando alguém diz que uma pessoa “nem parece” estar na rua, está partindo de uma imagem pronta dessa população.",
    ]),
    ("Na UPA (fluxo combinado na rede local)", [
        "A prioridade é definida pela classificação de risco, feita por profissional capacitado; na equipe de enfermagem, é atividade privativa do enfermeiro. A condição social não muda a classificação de risco. Quem relata piora, ou sinaliza que vai desistir da espera, deve ser reavaliado.",
        "A recepção da UPA não altera o endereço da pessoa em situação de rua; quem atualiza é a UBS ou a equipe do Consultório na Rua. O médico registra a situação de rua no prontuário e aciona o Serviço Social, que comunica o caso ao Consultório na Rua por mensagem, com o consentimento da pessoa.",
        "A falta de documento, de Cartão SUS ou de endereço não pode impedir o atendimento. O CPF é o número de identificação no SUS. Na UBS, a pessoa em situação de rua também não precisa comprovar endereço: o cadastro pode usar um endereço de referência, como o do Centro POP.",
    ]),
    ("Depois da alta", [
        "As farmácias das UPAs não entregam medicamentos para uso depois da alta. Os anti-hipertensivos são gratuitos na farmácia de qualquer UBS, com receita do SUS. Na Farmácia Popular também, mas lá se exigem documento com foto e CPF.",
        "O Consultório na Rua é uma equipe da atenção primária, com profissionais como enfermeiro, médico, assistente social, psicólogo e agente social. Atende a pessoa onde ela está e faz a ponte com a UBS e o restante da rede. Funciona em horário definido pelo município, em geral de dia e em dias úteis; fora dele, o Serviço Social registra o caso e faz o contato no próximo dia útil.",
        "Documentação civil, CadÚnico, orientação sobre benefícios, guarda de pertences e endereço de referência estão entre as ofertas do Centro POP, serviço da assistência social. É também por ele, pela abordagem social ou pelo Consultório na Rua que se chega às casas de acolhimento.",
    ]),
    ("Base conceitual: as quatro dimensões", [
        "Direito em Saúde: acesso universal e equânime, sem barreira de documento ou endereço; sigilo; informação; participação nas decisões. Defender esses direitos é compromisso ético-político e pede um olhar crítico sobre o que produz a situação de rua: desigualdade, racismo, machismo, heranças coloniais, uma longa história de exclusão. Para o Serviço Social, a “defesa intransigente dos direitos humanos” é princípio do Código de Ética da profissão.",
        "Conhecimento da Rede: saber o que cada serviço faz e acionar o serviço certo. UPA → Serviço Social → Consultório na Rua → UBS, com o Centro POP e o acolhimento pela assistência social.",
        "Empatia / Sensibilidade Social: reconhecer a pessoa antes do rótulo; considerar o que a situação de rua muda no cuidado, sem reduzir a pessoa a ela.",
        "Acolhimento: qualidade do encontro. Escuta, informação clara e construção do plano com a pessoa, como propõe a Política Nacional de Humanização.",
    ]),
]

define RENATO_FONTES = "Fontes: MDHC, População em situação de rua: diagnóstico com base nos dados e informações disponíveis em registros administrativos e sistemas do Governo Federal (2023); CadÚnico, maio de 2026 (análise do OBPopRua/UFMG, divulgada pela Agência Brasil em 29/05/2026); Grupo Brasileiro de Classificação de Risco; Resolução Cofen 661/2021; Portaria GM/MS 940/2011 e Portaria de Consolidação nº 1/2017, com redação da Portaria GM/MS 12.263/2026; Lei 14.534/2023; Portaria GM/MS 11.692/2026 (PNAIS-RUA); Tipificação Nacional de Serviços Socioassistenciais (Resolução CNAS 109/2009); Diretriz Brasileira de Hipertensão Arterial 2025; Decreto 7.053/2009; Código de Ética do/a Assistente Social (Resolução CFESS 273/1993); PNH/HumanizaSUS; reuniões do GT6 com o Consultório na Rua; comentários da equipe do Consultório na Rua de João Pessoa (novembro de 2026)."


## Renato foi embora na Cena 3 (Decisão 3)
label renato_saiu_na_espera:
    $ desfecho = "C"
    jump renato_epilogo_sequencia

## Fim das Cenas 6 (sem Serviço Social) ou 8
label renato_epilogo:
    $ desfecho = renato_desfecho()
    jump renato_epilogo_sequencia


label renato_epilogo_sequencia:
    $ olhar("")
    play music "audio/music/reflexao.ogg" fadein 2.0

    ## 6.10.1 Card de contexto real
    scene bg neutro_frio with fade
    call screen contexto_real("CONTEXTO REAL", "O que os dados e as normas dizem", RENATO_CONTEXTO, RENATO_FONTES) with dissolve

    ## 6.10.2 Reflexão pós-capítulo
    scene bg neutro_cor with fade
    window show
    narr "Neste dia, o que fez diferença para Renato não foi um gesto heroico, mas os detalhes da rotina: o tom de uma pergunta, o lugar de um registro, quem foi chamado e quando, e se o plano foi combinado com ele."
    if desfecho == "A":
        narr "Desta vez, a equipe tratou o atendimento dele como direito, e a rede funcionou."
    else:
        narr "Desta vez, em algum ponto do caminho, a ponte entre Renato e a rede não se formou."
    narr "A seguir, o dia contado pelo caderno de Renato, as quatro dimensões do cuidado neste atendimento e os serviços da rede que entraram no caso dele."
    window hide

    ## 6.10.3 O caderno de Renato
    scene bg neutro_quente with fade
    call screen pagina_caderno(renato_caderno(desfecho)) with dissolve

    ## 6.10.4 As dimensões do cuidado e a rede de Renato
    $ renato_nos(desfecho)
    scene bg neutro_cor with fade
    call screen painel_final("A rede de Renato") with dissolve

    if desfecho == "A":
        jump renato_desfecho_a
    elif desfecho == "B":
        jump renato_desfecho_b
    jump renato_desfecho_c


## 6.10.5 Desfecho A — Rede ativada
label renato_desfecho_a:
    scene bg neutro_quente with fade
    window show
    narr "{b}Desfecho A — Rede ativada{/b}"

    if tem("sem_encaminhamento"):
        narr "Renato chegou ao Centro POP às 16h50, sem encaminhamento, e precisou contar tudo de novo na recepção."
        narr "Não deu tempo de articular a vaga para aquela noite: ele dormiu de novo na marquise. A vaga na casa de acolhimento saiu três dias depois."
    elif tem("adiado_cnar"):
        narr "Naquela noite, Renato dormiu de novo na marquise, com o caderno debaixo da cabeça."
        if not tem("renato_sem_saber"):
            narr "Foi Marcos quem, na semana seguinte, o levou ao Centro POP."
    else:
        narr "No Centro POP, Renato entregou o encaminhamento ainda naquela tarde. A equipe de lá pediu uma vaga numa casa de acolhimento, que saiu no dia seguinte. Foi lá que o remédio passou a ficar guardado."

    if tem("renato_sem_saber"):
        narr "Na manhã seguinte, a equipe foi ao coreto, mas Renato não estava lá: ninguém tinha dito a ele que a equipe viria. Sem foto, perguntaram por ele na praça, e ninguém sabia o nome."
        narr "Dois dias depois, a equipe do Centro POP ligou para o Consultório na Rua: Renato estava lá. Marcos e a enfermeira mediram a pressão dele na sala de atendimento: 150 por 96."
        narr "Ele ainda não tinha conseguido o remédio. Naquela tarde, foram juntos à UBS."
    else:
        narr "Na manhã seguinte, ele estava no coreto quando Marcos chegou com a enfermeira do Consultório na Rua. Mediram a pressão ali mesmo, no banco da praça: 142 por 90."
        narr "De lá, foram com ele à UBS mais próxima, onde ele retirou o remédio e tomou a primeira dose."

    narr "Na mesma semana, a equipe atualizou o cadastro de Renato e o vinculou à UBS de referência, que passou a acompanhar a pressão dele."

    if tem("sem_saude_mental"):
        narr "Na evolução da UPA, não havia nada sobre o sono ou a depressão. Só um mês depois, numa conversa com a enfermeira da equipe, Renato contou que dormia duas horas por noite e que tinha parado o remédio da depressão."
    else:
        narr "O sono e a depressão também passaram a ser acompanhados."
    if tem("sedativo"):
        narr "Na primeira consulta, a equipe reavaliou a receita do remédio para dormir e conversou com Renato sobre o sono e a depressão."

    narr "Com Marcos junto, ele deu entrada na nova identidade e no Cadastro Único pelo Centro POP."
    narr "Um mês depois, numa visita da equipe, ele pediu o telefone emprestado e ligou para a filha. Falaram pouco."

    jump renato_encerramento


## 6.10.6 Desfecho B — O encontro que não aconteceu
label renato_desfecho_b:
    scene bg neutro_frio with fade
    window show
    narr "{b}Desfecho B — O encontro que não aconteceu{/b}"
    narr "Renato saiu da UPA com a receita dobrada no caderno."

    if tem("sem_ss"):
        narr "Na quinta, foi ao posto mais perto da praça. Não sabia a quem procurar, a fila era longa, e ele precisava voltar à praça antes que ocupassem o canto dele. Foi embora sem o remédio. Ninguém da rede sabia que ele existia."
    elif tem("ss_sem_renato"):
        narr "A mensagem do Serviço Social chegou ao Consultório na Rua sem foto e sem o lugar onde ele costuma ficar. A equipe perguntou por ele na rodoviária duas vezes. Ninguém conhecia um Renato."
    elif tem("renato_sem_saber"):
        narr "Na manhã seguinte, a equipe foi ao coreto, mas Renato tinha ido atrás de um bico: ninguém tinha dito a ele que a equipe viria. Sem foto, perguntaram por ele na praça, e ninguém sabia o nome."

    if tem("plano_b_upa"):
        narr "Quando a equipe não apareceu, ele pensou em voltar à UPA, como tinha combinado. Lembrou da espera e desistiu."

    narr "Duas semanas depois, Renato voltou à UPA com a dor de cabeça forte e a pressão em 190 x 118 mmHg. A receita continuava dobrada no caderno."

    if tem("sem_registro"):
        narr "Na ficha, nada sobre o que tinha acontecido da primeira vez. Ele contou tudo de novo."
    else:
        narr "Na ficha, a evolução da primeira vez dizia onde ele dormia e por que o remédio não ia funcionar sozinho. Desta vez, a equipe sabia por onde começar."

    narr "No caderno, uma página nova: “Quarta-feira. UPA. De novo.”"

    if tem("sem_ss", "ss_sem_renato"):
        menu:
            narr "As cenas do Serviço Social e da saída ficaram de fora desta jogada."
            "Retomar a partir da Decisão 7":
                $ restaurar_ponto(7)
                play music "audio/music/ambiente_upa.ogg" fadein 2.0
                jump renato_d7
            "Encerrar o dia":
                pass

    jump renato_encerramento


## 6.10.7 Desfecho C — A espera que venceu
label renato_desfecho_c:
    $ cor_pulseira = "laranja" if tem("fura_protocolo") else "amarela"
    scene bg neutro_frio with fade
    window show
    narr "{b}Desfecho C — A espera que venceu{/b}"
    narr "Renato saiu da UPA às 10h20, com a pulseira [cor_pulseira] no pulso. Quando o painel chamou o nome dele, às 11h, ninguém respondeu. Na ficha, ficou registrado: “Não respondeu ao chamado.”"
    narr "Cinco dias depois, um vendedor da praça o trouxe de volta à UPA, com a dor de cabeça mais forte que já tinha sentido e a vista embaçada. Pressão: 210 x 130 mmHg. Desta vez, a classificação foi laranja, e ele não esperou."
    narr "Na ficha da primeira vez, ninguém tinha registrado por que ele foi embora."

    menu:
        narr "Nesta jogada, Renato não chegou à consulta. As cenas da consulta, da observação, da alta e do Serviço Social ficaram de fora. Para conhecer o resto do dia, use o botão “Retomar a partir da Decisão 3”."
        "Retomar a partir da Decisão 3":
            $ restaurar_ponto(3)
            play music "audio/music/ambiente_upa.ogg" fadein 2.0
            jump renato_d3
        "Encerrar o dia":
            pass

    jump renato_encerramento


## 6.10.8 Encerramento
label renato_encerramento:
    window hide
    call encerrar_historia(desfecho)
    return
