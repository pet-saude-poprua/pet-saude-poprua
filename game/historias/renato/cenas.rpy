## historias/renato/cenas.rpy — Dia 1: Renato · Cenas 1 a 8
## Texto fiel ao roteiro v4 (revisão de 19/11/2026). Cada [Se flag: …] do
## roteiro vira um if; as decisões chamam escolher(n, "letra"), que aplica os
## efeitos e as flags da tabela em dados.rpy. Falas com mais de ~220
## caracteres foram divididas em duas telas, sem mudar o texto.

default cor_pulseira = "amarela"
default sem_local_texto = ""
default plano_extra_texto = ""
default evolucao_lida = ""

label renato:
    $ iniciar_historia("renato")
    show screen seu_olhar
    play music "audio/music/ambiente_upa.ogg" fadein 2.0

    scene bg aqua_fachada with fade
    centered "{color=#f4f1ea}{b}{size=+16}DIA 1{/size}{/b}\n\n{size=+6}Renato{/size}{/color}"

    jump renato_cena1


## ═════════════════════════════════════════════════════════════════════════════
## CENA 1 — Recepção · Seu olhar: Recepcionista da UPA (função administrativa)
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena1:
    $ olhar("Recepcionista da UPA")
    scene bg aqua_recepcao with fade
    window show

    narr "Quarta-feira, dez para as nove. A UPA está cheia desde as seis: gente em pé encostada na parede, uma criança dormindo no colo da mãe, a TV ligada sem som. O painel de senhas apita de tempos em tempos."
    narr "Você está no guichê 2. A fila dá a volta na pilastra."

    scene bg aqua_balcao with dissolve
    show renato hesitante at center with dissolve
    narr "O próximo é um homem de uns cinquenta anos, camisa de botão, calça gasta nos joelhos. Antes de falar, ele põe um caderno de capa dura em cima do balcão."

    renato "Bom dia. Tô com uma dor de cabeça forte desde a madrugada. E o coração disparando."
    recep "Bom dia. O nome completo, por favor."
    narr "Ele diz o nome."
    recep "O senhor tem algum documento ou sabe informar o CPF? Se não tiver, a gente segue o fluxo de identificação do serviço."
    renato "Tenho apenas o número do CPF."

    show caderno at obj_dir with dissolve
    narr "Ele abre o caderno na contracapa, onde o número está escrito à caneta, e vira para você."
    hide caderno with dissolve

    show esus at overlay_esus with dissolve
    narr "O sistema encontra o cadastro pelo CPF: 54 anos, endereço localizado em uma rua do Conjunto Esperança, do outro lado da cidade, sem atualização há mais de dez anos. A tela fica virada para você."
    hide esus with dissolve
    narr "O guichê é aberto, e a primeira fileira de cadeiras fica a dois metros do balcão."

    menu:
        narr "O cadastro existe, mas o endereço está desatualizado, e você ainda não confirmou que é ele. Como você segue?"

        "Confirmar a identidade pela data de nascimento e pelo nome da mãe, sem perguntar pelo endereço.":
            $ escolher(1, "A")
            call resultado("Dois dados bastaram para identificar Renato, sem documento nem Cartão SUS. O endereço desatualizado não muda o atendimento de hoje: quem atualiza o cadastro é a UBS ou o Consultório na Rua.")

        "Perguntar se o endereço ainda é aquele, como você faz com todo paciente, para manter o cadastro em dia.":
            $ escolher(1, "B")
            recep "O endereço ainda é esse, no Conjunto Esperança?"
            narr "Renato demora para responder. Olha para trás, para a fila."
            renato "{i}(baixo){/i} Faz tempo que não. Eu tô sem casa."
            narr "Ele falou baixo, mas a primeira fileira está a dois metros. Uma senhora levanta os olhos do celular e cutuca o marido."
            call resultado("A pergunta é de rotina, mas, num guichê aberto, expõe mais quem não tem endereço para dar. E a resposta nem seria usada: na UPA, o endereço não se atualiza.")

        "Pedir um documento com foto antes de seguir: um número anotado num caderno não comprova que o cadastro é dele.":
            $ escolher(1, "C")
            recep "O senhor não tem nenhum documento com foto? Só o número não confirma que é o senhor."
            renato "Levaram minha mochila. Foi tudo junto."
            narr "Ele fica parado diante do balcão, com o caderno aberto. Atrás dele, alguém da fila suspira alto."
            call resultado("Conferir a identidade é trabalho da recepção, mas a falta de documento não pode atrasar o atendimento. CPF, data de nascimento e nome da mãe confirmam o cadastro.")

    window show
    recep "Data de nascimento?"
    renato "Doze de março de setenta e dois."
    recep "E o nome da sua mãe?"
    narr "Ele responde. Confere com o cadastro."
    recep "Pronto, seu Renato. Pode aguardar ali, que chamam pelo nome para a classificação. Se piorar enquanto espera, avisa aqui no guichê."

    if tem("exposto_recepcao"):
        narr "Ele agradece e vai procurar uma cadeira, com o caderno debaixo do braço."
        show senhora at left_np(0.31) with dissolve
        narr "Quando ele passa pela primeira fileira, a senhora puxa a bolsa da cadeira vazia ao lado e a acomoda no colo. Renato desvia da cadeira e vai ficar de pé no fundo da sala, encostado na parede."
        hide senhora with dissolve
    elif tem("barreira_doc"):
        narr "Ele agradece e vai procurar uma cadeira, com o caderno debaixo do braço."
    else:
        narr "Ele agradece e vai procurar uma cadeira, com o caderno debaixo do braço. Passou pelo balcão como qualquer pessoa da fila, sem precisar dizer em voz alta onde dorme."

    if tem("barreira_doc"):
        narr "Antes de sair do balcão, ele pede desculpa duas vezes pela demora."

    hide renato with dissolve
    jump renato_cena2


## ═════════════════════════════════════════════════════════════════════════════
## CENA 2 — Classificação de risco · Seu olhar: Enfermeiro(a) do acolhimento
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena2:
    $ olhar("Enfermeiro(a) do acolhimento com classificação de risco")
    scene bg aqua_classificacao with fade
    show renato hesitante at center with dissolve
    window show

    narr "Sala de classificação. Você fecha a porta."
    enf "Seu Renato? Pode sentar. O que é que o senhor tá sentindo?"
    renato "Essa dor de cabeça aqui atrás, desde a madrugada. E o coração, que dispara do nada. Hoje, quando levantei, fiquei tonto."
    narr "Você afere os sinais vitais. Pressão arterial: 182 x 120 mmHg. Frequência cardíaca: 96 bpm, regular. Saturação de oxigênio: 97%%. Temperatura: 36,4 °C. Glicemia capilar: 104 mg/dL."
    enf "De zero a dez, quanto tá essa dor?"
    renato "Uns seis."
    enf "Essa dor começou de repente, de uma vez, ou foi aumentando? Vomitou?"
    renato "Foi aumentando. Vomitar, não."
    enf "Dor no peito? Falta de ar? Algum lado do corpo fraco ou dormente? A vista escureceu?"
    renato "Não. Só isso mesmo."
    enf "Toma remédio pra pressão?"
    renato "Nunca tomei."
    enf "Veio com alguém? Tem algum contato pra gente avisar, se precisar?"
    renato "Não. {i}(pausa){/i} Eu tô sem casa. Tô na rua faz uns oito meses."
    narr "Pelo quadro clínico, Renato apresenta um pico hipertensivo e é classificado com a cor amarela: precisa de atendimento prioritário, mas pode aguardar dentro do tempo previsto no protocolo. Hoje, o amarelo está esperando mais de uma hora."
    narr "Você já viu muitas pessoas em situação de rua desistirem da espera. Para quem está na rua, a demora pode significar perder o lugar onde dorme, ficar sem a alimentação da noite ou deixar desprotegidos os pertences que guardou."

    menu:
        narr "A classificação de risco segue o protocolo. A espera de hoje, porém, pesa mais para quem está na rua. O que você faz?"

        "Classificar como laranja: um hipertenso sem tratamento que desiste da espera corre mais risco, e quem está na rua desiste mais.":
            $ escolher(2, "A")
            enf "O senhor vai ser chamado mais rápido, seu Renato. Aguarda ali."
            narr "No painel, o nome de Renato sobe para a frente de um rapaz de pulseira amarela que chegou às sete com o braço inchado."
            call resultado("A preocupação com a desistência é legítima, mas a cor segue critérios clínicos. Mudar a cor pela condição social tira o lugar de quem tem risco maior. O que reduz a desistência é informar, orientar e reavaliar.")

        "Classificar como amarelo, explicar a espera e orientar Renato a avisar se piorar.":
            $ escolher(2, "B")
            enf "Seu Renato, sua pressão tá alta, e isso pode explicar a dor de cabeça e a tontura. Pela classificação, o senhor é amarelo: precisa ser atendido, mas não tem risco imediato, então pode aguardar um pouco. Hoje a espera tá longa."
            enf "É importante que o senhor aguarde o atendimento. Se sentir qualquer piora enquanto espera, não fica esperando, não: bate aqui nesta porta. Tá certo?"
            renato "Tá certo. Obrigado."
            call resultado("A cor seguiu os critérios clínicos do protocolo, que existe para reduzir o risco de morte. E Renato sabe por que vai esperar e o que fazer se piorar: informação clara protege contra a desistência.")

        "Classificar como amarelo e chamar o próximo: há seis pessoas esperando classificação, e a pulseira já garante que ele vai ser atendido.":
            $ escolher(2, "C")
            enf "Amarelo, seu Renato. Pode aguardar lá fora, que chamam pelo painel."
            narr "Ele agradece e sai. Não perguntou quanto tempo ia demorar, e você não disse."
            call resultado("A classificação está correta, e a fila da classificação também é urgente. Mas, sem saber que a espera vai passar de uma hora nem o que fazer se piorar, quem tem mais a perder com a demora tende a ir embora.")

    window show
    if tem("fura_protocolo"):
        narr "Você coloca a pulseira laranja. No campo de observações, registra: “Refere situação de rua há cerca de 8 meses. Sem acompanhante.”"
    else:
        narr "Você coloca a pulseira amarela. No campo de observações, registra: “Refere situação de rua há cerca de 8 meses. Sem acompanhante.”"

    hide renato with dissolve
    jump renato_cena3


## ═════════════════════════════════════════════════════════════════════════════
## CENA 3 — Sala de espera · Seu olhar: Enfermeiro(a) do acolhimento
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena3:
    scene bg aqua_espera with fade
    window show

    narr "Às 9h40, o SAMU trouxe duas vítimas graves de um acidente, e os três médicos do plantão foram para a sala vermelha. O painel parou."
    if tem("fura_protocolo"):
        narr "Nem a pulseira laranja adiantou: havia quatro laranjas na frente de Renato quando o SAMU chegou, e o painel parou para todas as cores."
    narr "Na sua fila, seis pessoas esperam para ser classificadas."

    $ guardar_ponto(3)

label renato_d3:
    $ olhar("Enfermeiro(a) do acolhimento com classificação de risco")
    scene bg aqua_espera
    show renato hesitante at center with dissolve
    window show

    if tem("sem_orientacao"):
        narr "Da porta da classificação, você vê Renato se levantar, olhar para o painel parado e caminhar em direção à saída, com o caderno debaixo do braço."
        narr "Ninguém disse a ele quanto tempo ia demorar, nem que podia avisar. Você o alcança perto da porta."
        renato "Já faz mais de uma hora. Eu vou embora. Volto outro dia."
    else:
        narr "Entre uma classificação e outra, alguém bate na porta. É Renato, com o caderno debaixo do braço."
        renato "Desculpa incomodar. É que já faz mais de uma hora… Eu tava pensando em ir embora."

    if tem("exposto_recepcao"):
        narr "Ele olha de relance para a primeira fileira, onde a senhora continua com a bolsa no colo."

    menu:
        narr "A fila da classificação também é urgente. Renato está dizendo que vai desistir. O que você faz?"

        "Pedir que ele volte a sentar e aguarde: ele já foi classificado, e a fila da classificação não pode parar.":
            $ escolher(3, "A")
            enf "Seu Renato, o senhor já tá na fila do médico. Volta lá e aguarda, que já já chamam."
            renato "Tá bom."
            hide renato with dissolve
            narr "Ele volta para o fundo da sala. Você chama o próximo da classificação."
            if tem("sem_orientacao"):
                narr "Quinze minutos depois, quando o painel volta a chamar, a cadeira dele está vazia."
                call resultado("Pedir que ele aguarde não está errado: a pressão precisa ser avaliada hoje. Mas quem fala em ir embora está dizendo que a espera pesou demais. Sem nova medida nem explicação, a desistência fica mais provável.")
                call renato_reflexao1
                jump renato_saiu_na_espera
            narr "Renato espera. Sem reavaliação, a ficha que o médico vai ler tem só a pressão da chegada."
            call resultado("Pedir que ele aguarde não está errado: a pressão precisa ser avaliada hoje. Mas quem fala em ir embora está dizendo que a espera pesou demais. Sem nova medida nem explicação, a desistência fica mais provável.")

        "Dizer que, se ele precisa ir, pode voltar mais tarde ou amanhã cedo, quando a UPA costuma estar mais vazia.":
            $ escolher(3, "B")
            enf "Hoje tá complicado mesmo. Se o senhor precisar ir, volta mais tarde ou amanhã cedo, que costuma ser mais tranquilo."
            renato "Tá certo. Obrigado."
            hide renato with dissolve
            narr "Ele ajeita o caderno debaixo do braço e sai pela porta da frente."
            call resultado("A intenção foi poupá-lo da espera. Mas ele chegou com 182 x 120 mmHg e não foi reavaliado: liberá-lo é deixá-lo sair com o risco. Para quem está na rua, “voltar amanhã” pode não acontecer.")
            call renato_reflexao1
            jump renato_saiu_na_espera

        "Parar a classificação por um minuto, medir a pressão de novo e explicar por que o painel parou.":
            $ escolher(3, "C")
            if tem("sem_orientacao"):
                enf "Espera um minutinho, seu Renato. Senta aqui um minuto que eu vou medir de novo. Desde que o senhor passou aqui, a dor piorou ou melhorou? Sentiu alguma coisa diferente?"
            else:
                enf "Fez bem em vir, seu Renato. Senta aqui um minuto que eu vou medir de novo. Desde que o senhor passou aqui, a dor piorou ou melhorou? Sentiu alguma coisa diferente?"
            renato "Tá do mesmo jeito. A cabeça pesa mais com o barulho."
            narr "Pressão arterial: 178 x 108 mmHg. Nenhum sinal novo."
            enf "Tá demorando, eu sei. Chegaram dois casos graves, e os médicos tão todos na emergência. Mas a pressão do senhor continua alta, viu?"
            enf "O senhor precisa passar pelo médico hoje. Quando eles saírem de lá, a fila anda. Se piorar, é só bater aqui."
            renato "Então eu espero."
            call resultado("Um minuto bastou: a pressão continua alta, não há sinal novo, e Renato sabe por que a fila parou. Responder a quem sinaliza desistência faz parte do cuidado.")

    call renato_reflexao1
    jump renato_cena4


label renato_reflexao1:
    if tem("exposto_recepcao"):
        call reflexao("Uma pergunta de rotina, feita em voz alta no balcão, bastou para a primeira fileira saber que Renato está na rua. Depois disso, a espera ficou mais pesada para ele do que para os outros.", "Defender o direito de Renato ao atendimento é compromisso ético-político de quem trabalha no SUS. A desconfiança contra quem está na rua vem da desigualdade, do racismo e de uma longa história de exclusão, e também aparece dentro dos serviços de saúde.")
    else:
        call reflexao("Ninguém reparou em Renato na chegada nem na espera: a informação de que ele está na rua ficou só com quem precisava dela para cuidar dele. Uma pergunta em voz alta no balcão, um comentário entre colegas ou o vigilante de olho nele bastariam para que a sala de espera inteira ficasse sabendo.", "Defender o direito de Renato ao atendimento é compromisso ético-político de quem trabalha no SUS. A desconfiança contra quem está na rua vem da desigualdade, do racismo e de uma longa história de exclusão, e também aparece dentro dos serviços de saúde.")
    return


## ═════════════════════════════════════════════════════════════════════════════
## CENA 4 — Consulta · Seu olhar: Médico(a) do plantão
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena4:
    $ olhar("Médico(a) do plantão")
    scene bg aqua_consultorio with fade
    show medico_upa at primeiro_plano_centro with dissolve
    window show

    narr "Você voltou da sala vermelha há vinte minutos. Um dos pacientes do SAMU foi entubado e espera vaga na UTI."
    hide medico_upa with dissolve

    $ cor_pulseira = "laranja" if tem("fura_protocolo") else "amarela"
    show esus at overlay_esus with dissolve
    if tem("sem_reavaliacao"):
        narr "Na tela, a ficha de Renato: dor de cabeça, tontura, palpitação, pressão arterial de 182 x 120 mmHg na chegada, pulseira [cor_pulseira]."
    else:
        narr "Na tela, a ficha de Renato: dor de cabeça, tontura, palpitação, pressão arterial de 182 x 120 mmHg na chegada e de 178 x 108 mmHg na reavaliação, pulseira [cor_pulseira]."
    narr "No campo de observações: “Refere situação de rua há cerca de 8 meses. Sem acompanhante.”"
    hide esus with dissolve

    show renato hesitante at center with dissolve
    narr "O painel chama Renato. Ele cumprimenta e senta na beira da cadeira, com o caderno no colo."
    narr "A situação de rua está na ficha, e ele veio pela dor de cabeça: é por ela que a consulta começa. Você deixa a tela de lado e se vira para ele."
    med "Seu Renato, me conta o que o senhor tá sentindo."
    show renato aberto at center with dissolve
    renato "Essa dor de cabeça aqui atrás. E o coração, que dispara do nada, já faz uns dias. {i}(pausa){/i} E eu não tô dormindo, doutor. Durmo duas, três horas e acordo com qualquer barulho."
    med "Alguma dor no peito? Aperto, queimação?"
    renato "No peito, não. É só o coração acelerado."
    med "Toma ou já tomou algum remédio? E bebida, cigarro, alguma outra substância? Pergunto pra todo mundo."
    renato "Pra pressão, nunca. Bebida, nada. Tomei remédio pra depressão uns tempos. Parei quando não deu mais pra pagar."
    narr "Você examina. Coração e pulmões sem alterações, pulsos simétricos, força, fala e marcha normais. Nada sugere lesão aguda causada pela pressão. A palpitação, com essa pressão, pede um eletrocardiograma."
    med "Seu Renato, sua pressão tá alta, e pode ser isso que tá dando a dor de cabeça e a tontura. Vou passar um remédio pra dor agora. O senhor vai ficar um tempo na observação, e vou pedir um eletro, por causa do coração acelerado."
    med "Lá a enfermagem mede a pressão de meia em meia hora. Se não baixar com o repouso, dão um remédio pra ela descer aos poucos. Antes de ir embora, o senhor passa aqui de novo."
    renato "Fico até que horas?"
    med "Umas três, quatro horas. Depende da pressão."
    narr "Ele contou que dorme duas, três horas por noite. Lá fora, um paciente entubado espera vaga na UTI, e a fila do amarelo está parada desde as 9h40."

    menu:
        narr "A pressão já tem conduta. O que você faz com o que Renato disse sobre o sono?"

        "Encaminhá-lo à observação e deixar o sono para a atenção primária: a urgência precisa andar.":
            $ escolher(4, "A")
            med "O sono a gente vê depois, tá? Quem for acompanhar o senhor lá fora cuida disso."
            renato "Tá bom, doutor."
            narr "Ele pega o caderno e segue para a observação."
            call resultado("Na urgência, a consulta precisa ser objetiva, e o sono não se trata na UPA. Mas, com depressão sem tratamento, perguntar sobre o ânimo e sobre ideias de morte leva um minuto e pode mudar a alta.")

        "Perguntar há quanto tempo ele dorme mal e prescrever um remédio para dormir por alguns dias, para ele conseguir descansar.":
            $ escolher(4, "B")
            med "Desde quando o senhor dorme assim?"
            renato "Desde que eu tô na rua. Lá a gente não dorme direito, fica de olho nas coisas."
            med "Vou passar um remédio pro senhor dormir melhor nesses dias."
            narr "Renato guarda a receita no caderno sem dizer nada."
            call resultado("A queixa foi ouvida, e isso conta. Mas o remédio para dormir não trata a causa e, na rua, aumenta o risco de furto e de violência à noite. E faltou a pergunta sobre ideias de morte.")

        "Perguntar desde quando ele dorme assim, como está o ânimo e se já pensou em tirar a própria vida, e registrar para a atenção primária.":
            $ escolher(4, "C")
            med "Desde quando o senhor dorme assim?"
            renato "Desde que eu tô na rua. Lá a gente não dorme direito, fica de olho nas coisas."
            med "E o ânimo, como tá? Tem hora que o senhor pensa que não vale a pena viver? Já pensou em tirar a própria vida?"
            renato "{i}(pausa){/i} Não. Isso não."
            med "Se esse pensamento aparecer, o senhor procura a equipe que for acompanhar o senhor, ou vem aqui, a qualquer hora."
            med "Vou anotar tudo isso, pra quem for cuidar do senhor lá fora saber. Aqui na urgência a gente não tem como tratar o sono. E remédio pra depressão tem no SUS, de graça."
            renato "Eu não sabia."
            call resultado("Três perguntas couberam no tempo da urgência. Perguntar diretamente sobre ideias de morte não induz a ideia. O sono e a depressão não se tratam na UPA, mas agora estão registrados para quem vai acompanhá-lo.")

    hide renato with dissolve
    jump renato_cena5


## ═════════════════════════════════════════════════════════════════════════════
## CENA 5 — Sala de observação · Seu olhar: Técnico(a) de enfermagem
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena5:
    $ olhar("Técnico(a) de enfermagem da sala de observação")
    scene bg aqua_observacao with fade
    window show

    narr "A sala de observação tem oito poltronas e quatro macas, quase todas ocupadas. Um senhor no oxigênio, uma moça tomando soro, um rapaz com o braço imobilizado."
    show renato hesitante at center with dissolve
    narr "A enfermeira da sala distribui os pacientes, e Renato fica com você, na poltrona 6."
    narr "Você mede a pressão dele de meia em meia hora e registra na anotação de enfermagem."
    tec "Seu Renato, vou fazer o eletro agora. Depois o senhor descansa, e eu vou medindo sua pressão. O que eu for fazer, eu aviso antes."
    narr "Você leva o resultado do eletro ao consultório 2. Sem alterações: a prescrição continua a mesma, e Renato não precisa ficar no monitor, o aparelho que acompanha os batimentos e outros sinais vitais o tempo todo."
    narr "Depois do eletro, você dá o analgésico prescrito."
    narr "Às 11h40, depois de meia hora de repouso, a pressão arterial está em 172 x 106 mmHg. Você avisa a enfermeira da sala, que confirma a conduta com o consultório 2, e dá o comprimido prescrito para a pressão."
    narr "Às 12h10, 164 x 100 mmHg. Renato pede a caneta emprestada e anota os números no caderno."
    tec "O senhor anota tudo?"
    renato "Costume. Foram quase trinta anos em manutenção industrial. Era um hábito nosso."
    narr "Às 12h40, 160 x 98 mmHg. Renato pede um copo d’água e bebe devagar."
    narr "Na aferição das 13h10, o caderno está aberto no colo dele, numa página escrita até a margem, com um nome no alto. Ele fecha quando você chega."
    narr "Pressão arterial: 156 x 96 mmHg."
    show renato normal at center with dissolve
    renato "Esse remédio da pressão… vou ter que tomar todo dia?"
    tec "O médico explica na alta, mas geralmente é, sim."
    renato "É que eu não tenho onde guardar as coisas. Já levaram minha mochila uma vez, com documento e tudo. O caderno só ficou porque eu durmo com ele."
    narr "O que ele contou não é sintoma, mas decide se o tratamento vai funcionar fora da UPA: sem lugar onde guardar o comprimido, é pouco provável que ele consiga tomá-lo todo dia. Há doze pacientes na sala."

    menu:
        narr "A preocupação de Renato não é clínica, e a orientação de alta é do médico. O que você faz agora?"

        "Validar a preocupação, perguntar se há alguém de confiança para guardar a cartela, falar da assistente social e passar ao médico.":
            $ escolher(5, "A")
            tec "Essa preocupação é importante, seu Renato. O remédio ajuda o corpo a se regular, mas isso leva tempo, por isso ele precisa ser tomado todo dia."
            tec "O senhor tem alguém de confiança que possa guardar a cartela? Alguém de um posto de saúde, um comerciante, alguém perto de onde o senhor fica?"
            renato "{i}(pensa){/i} Tem o rapaz da banca, na praça. Mas não sei."
            tec "Isso não resolve tudo, eu sei. Mas tem jeito de procurar alternativas. Aqui tem assistente social, sabia? Depois de passar no médico, o senhor pode conversar com ela. Vou anotar isso e passar pro médico, tá certo?"
            renato "Tá."
            narr "Às 13h40, 150 x 94 mmHg. A dor de cabeça passou. Ele pergunta as horas duas vezes."
            narr "Na anotação de enfermagem, você registra: “13h40: PA 150 x 94 mmHg, nega cefaleia. Refere situação de rua, preocupação com local para guardar a medicação e furto dos documentos. Orientado sobre o Serviço Social.”"
            call resultado("A preocupação de Renato foi validada e registrada, e ele sabe que existe alguém na UPA para ajudar com isso. Quando a equipe fala a mesma língua, o cuidado deixa de depender da boa vontade de uma pessoa só.")

        "Dizer que o médico explica tudo na alta e seguir com as aferições.":
            $ escolher(5, "B")
            tec "Isso o médico vê com o senhor na alta, tá?"
            renato "Tá."
            narr "Ele fecha o caderno. Nas aferições seguintes, não fala mais nada."
            narr "Às 13h40, 150 x 94 mmHg. A dor de cabeça passou. Na anotação de enfermagem, você registra: “13h40: PA 150 x 94 mmHg, nega cefaleia.”"
            call resultado("A orientação de alta é mesmo do médico. Mas o que Renato contou não está na ficha e decide se o tratamento vai funcionar lá fora. Quem diz que está bem nem sempre repete a preocupação.")

    window show
    scene bg aqua_corredor with dissolve
    if tem("sem_repasse"):
        narr "Às 13h50, no posto, você atualiza a anotação de Renato. A colega ao lado lê a ficha por cima do seu ombro e gira a cadeira na sua direção."
    else:
        narr "Às 13h50, você leva a anotação ao consultório 2 e passa ao médico, em voz baixa, o que Renato contou. De volta ao posto, a colega ao lado, que leu a anotação por cima do seu ombro, gira a cadeira na sua direção."
    colega_enf "O da poltrona 6 tá na rua? Nem parece. Tá até limpinho."

    menu:
        narr "A colega falou no volume de sempre. A sala de observação fica a poucos metros do posto. Como você reage?"

        "Responder na hora, para ela entender, que isso é preconceito.":
            $ escolher(6, "A")
            tec "Isso é preconceito. Morar na rua não tem cara."
            narr "A colega fica vermelha. Na sala de observação, um senhor duas poltronas adiante se vira para olhar Renato."
            colega_enf "Precisa disso tudo, não."
            call resultado("Questionar o “nem parece” era necessário. Mas, em voz alta, a resposta confirmou para a sala que o paciente da poltrona 6 está na rua. A conversa sobre o preconceito pode ficar para depois, longe dos pacientes.")

        "Pedir que ela fale baixo, porque é informação do atendimento, e retomar o assunto mais tarde, longe dos pacientes.":
            $ escolher(6, "B")
            tec "{i}(baixo){/i} Fala baixo. Isso é do atendimento dele."
            colega_enf "Oxe, só comentei."
            tec "Eu sei. Mas tem paciente ouvindo."
            narr "Ela dá de ombros e volta para a prescrição que estava conferindo."
            narr "Mais tarde, longe dos pacientes, você retoma o “nem parece” com ela: o comentário supõe que quem está na rua tem uma aparência típica."
            call resultado("O pedido de discrição protegeu o sigilo na hora, e a conversa sobre o comentário aconteceu depois, sem plateia.")

        "Não responder: foi só um comentário, e criar clima no posto atrapalharia o plantão.":
            $ escolher(6, "C")
            narr "Você não diz nada e volta para a anotação."
            colega_enf "{i}(para a enfermeira que passa){/i} Sabia que o da 6 mora na rua? Nem parece."
            narr "A enfermeira olha para a poltrona 6. Renato está de olhos fechados, mas não está dormindo."
            call resultado("Comentários assim parecem pequenos, mas fazem a informação circular e reforçam a ideia de que quem está na rua tem uma aparência típica. Ficar em silêncio também é uma resposta.")

    window show
    if tem("sem_repasse"):
        narr "Você completa a anotação: “13h50: PA em queda, sem queixas.”"
    else:
        narr "Você completa a anotação: “13h50: comunicado ao consultório 2.”"

    scene bg aqua_observacao with dissolve
    show renato normal at center
    if tem("exposto_obs"):
        narr "Quando Renato volta do banheiro, o senhor da poltrona 5 puxa a sacola para perto dos pés. Renato percebe, senta e abre o caderno sem escrever nada."
    narr "Às 14h10, a pressão arterial está em 148 x 92 mmHg, e a frequência cardíaca, em 84 bpm. Você vai ao consultório 2 avisar, e Renato é chamado para a reavaliação."

    call reflexao("Na UPA, a consulta tem de ser rápida e objetiva. Mesmo assim, uma pergunta aberta no começo e um minuto de conversa na hora de medir a pressão cabem nesse tempo e trazem informações que a ficha não tem.", "O que o paciente conta só ajuda se chegar a quem vai cuidar dele depois. Para isso, é preciso acolher a preocupação, avisá-lo do que vai ser feito, registrar no lugar certo e não deixar o assunto virar conversa de corredor.")

    jump renato_cena6


## ═════════════════════════════════════════════════════════════════════════════
## CENA 6 — Reavaliação e alta · Seu olhar: Médico(a) do plantão
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena6:
    $ olhar("Médico(a) do plantão")
    scene bg aqua_consultorio with fade
    window show

    narr "Pressão arterial de 148 x 92 mmHg, frequência cardíaca de 84 bpm, sem dor de cabeça. Eletrocardiograma sem alterações. Clinicamente, Renato pode ter alta."
    if tem("sem_repasse"):
        narr "Na anotação de enfermagem, só as aferições. Na ficha da classificação, a linha: “Refere situação de rua há cerca de 8 meses. Sem acompanhante.”"
    else:
        narr "Na anotação de enfermagem, está registrado: preocupação com local onde guardar a medicação, documentos furtados, orientado sobre o Serviço Social, comunicado ao consultório às 13h50."
    if tem("sem_saude_mental"):
        narr "Na sua própria anotação da consulta, nada sobre o sono ou a depressão."

    show renato normal at center with dissolve
    med "Seu Renato, a pressão baixou e o eletro veio normal. O senhor tá liberado."
    med "Vou passar dois remédios pra pressão: um comprimido de cada, de manhã, todo dia, mesmo quando o senhor estiver se sentindo bem. Daqui a uma semana, no máximo, alguém precisa medir sua pressão de novo."
    med "Se a dor de cabeça voltar forte, se tiver dor no peito, falta de ar, fraqueza ou dormência num lado do corpo, ou se a vista escurecer, o senhor volta aqui na hora."
    if tem("sem_repasse"):
        renato "Tá bom, doutor. {i}(pausa){/i} Tô bem."
        narr "Ele diz que está bem, mas na ficha está escrito que ele dorme na rua."
    else:
        renato "Vou tomar como, doutor? Eu não tenho onde guardar nada."

    $ guardar_ponto(7)

label renato_d7:
    $ olhar("Médico(a) do plantão")
    scene bg aqua_consultorio
    show renato normal at center
    window show

    menu:
        narr "Renato tem alta clínica e uma receita de uso contínuo. Ele não tem casa, documento nem vínculo com uma UBS. Como você encaminha?"

        "Explicar que o remédio é de graça na farmácia da UBS, sem Cartão SUS, e orientar que ele procure o posto mais perto de onde costuma ficar.":
            $ escolher(7, "A")
            med "O remédio é de graça no posto, viu? Não precisa de cartão do SUS. Procura o posto mais perto de onde o senhor fica, leva essa receita, e lá eles acompanham a pressão."
            renato "Tá certo, doutor."
            narr "Ele dobra a receita em quatro e guarda no caderno."
            call resultado("A informação está certa: o remédio é gratuito, sem Cartão SUS. Mas, sem casa, documento ou UBS de referência, achar quem o acompanhe fica por conta de Renato. A ponte com a rede é do Serviço Social.")

        "Explicar que, antes de sair, ele vai conversar com a assistente social, e acionar o Serviço Social pessoalmente.":
            $ escolher(7, "B")
            if tem("sem_repasse"):
                med "Antes de ir, eu quero que o senhor converse com a assistente social daqui. Ela orienta o senhor sobre quem pode acompanhar a pressão e o remédio lá fora. Pode ser?"
            else:
                med "A técnica me contou dessa preocupação, e ela tem razão. Antes de ir, eu quero que o senhor converse com a assistente social daqui."
                med "Ela orienta o senhor sobre quem pode acompanhar a pressão e o remédio lá fora. Pode ser?"
            renato "Pode."
            call resultado("A alta clínica não encerra o cuidado. Com o Serviço Social, a receita deixa de ser só um papel e passa a ter um caminho na rede.")

        "Registrar na evolução um pedido de avaliação do Serviço Social e liberar Renato: a assistente social lê o caso e entra em contato com ele depois.":
            $ escolher(7, "C")
            med "Vou pedir pra assistente social ver o seu caso, tá? Ela entra em contato com o senhor."
            renato "Tá bom."
            narr "Ele não tem telefone, mas não diz nada."
            call resultado("O pedido ficou registrado, e isso é importante. Mas Renato não tem telefone nem endereço: um encaminhamento que depende de encontrá-lo depois, sem dia nem lugar combinados, dificilmente se completa.")

    window show
    show receita at obj_dir with dissolve
    if tem("sem_ss"):
        narr "A receita vai com ele. Os comprimidos são retirados de graça na farmácia da UBS, sem precisar do Cartão SUS."
    else:
        narr "A receita vai com ele. Os comprimidos são retirados de graça na farmácia da UBS, sem precisar do Cartão SUS, e a equipe do Consultório na Rua pode ajudar nisso."
    hide receita with dissolve
    hide renato with dissolve

    narr "Antes de chamar o próximo paciente, você abre a evolução."
    show esus at overlay_esus with dissolve

    menu:
        narr "A situação de rua interfere no tratamento de Renato, mas o motivo da consulta foi a pressão. O que você faz com essa informação na evolução?"

        "Registrar no campo Avaliação, em linguagem objetiva, junto com o que interfere no tratamento.":
            $ escolher(8, "A")
            python:
                sem_local_texto = "" if tem("sem_repasse") else " Sem local para guardar a medicação. Documentos furtados."
                plano_extra_texto = ""
                if not tem("sem_saude_mental"):
                    plano_extra_texto += " Acompanhamento de saúde mental na atenção primária."
                if not tem("sem_ss"):
                    plano_extra_texto += " Serviço Social para articulação com o Consultório na Rua."
            narr "No campo Avaliação, em linguagem objetiva:"
            narr "“Elevação importante da PA sem sinais de lesão aguda de órgão-alvo, em hipertenso sem tratamento prévio; PA controlada após repouso e administração de anti-hipertensivo oral.”"
            if not tem("sem_saude_mental"):
                narr "“Insônia importante e depressão diagnosticada há alguns anos, sem tratamento atual. Nega ideação suicida.”"
            narr "“Relata situação de rua há cerca de 8 meses, com impacto na adesão.[sem_local_texto]”"
            narr "No Plano: “Dois anti-hipertensivos em dose baixa, 1x/dia, pela manhã. Orientados sinais de alarme e retorno. Reavaliar PA em até 7 dias na atenção primária.[plano_extra_texto]”"
            call resultado("O registro objetivo, no prontuário, orienta quem vem depois sem expor Renato a quem não participa do cuidado dele.")

        "Não registrar a situação de rua: o motivo da consulta foi a pressão, e o registro pode virar rótulo.":
            $ escolher(8, "B")
            narr "No campo Avaliação, você escreve só o quadro clínico. A situação de rua, o lugar para guardar o remédio e os documentos ficam de fora."
            call resultado("O cuidado com o rótulo é legítimo. Mas, sem o registro, quem atender Renato depois começa do zero. Escrita de forma objetiva, no prontuário, a situação de rua é informação clínica.")

    window show
    hide esus with dissolve
    if tem("sem_ss"):
        narr "A codificação do diagnóstico entra como de rotina. É esse registro que qualquer equipe da UPA vai encontrar se Renato voltar."
    else:
        narr "A codificação do diagnóstico entra como de rotina. É esse registro que o Serviço Social lê hoje e que qualquer equipe da UPA vai encontrar se Renato voltar."

    if tem("sem_ss", "ss_sem_renato"):
        narr "Renato sai às 15h, com a receita no caderno. Você chama o próximo paciente."
    else:
        scene bg aqua_corredor with dissolve
        narr "A sala do Serviço Social fica no fim do corredor. Você vai até lá entre um paciente e outro."
        show assistente at center with dissolve
        med "Tenho uma alta do consultório 2: Renato, 54 anos, em situação de rua. Pressão controlada, começa remédio de pressão hoje. Tá tudo na evolução. Consegue ver ele antes de sair?"
        assist "Consigo, mas daqui a uns quarenta minutos. Tenho dois na frente."
        hide assistente with dissolve

    call reflexao("A pressão controlada permite a alta. A continuidade do tratamento depende do que a UPA faz antes de Renato sair: orientar, registrar no lugar certo e acionar o Serviço Social, para que a receita chegue a quem vai acompanhá-lo.", "Registrar a situação de rua no prontuário, de forma objetiva, orienta quem vem depois. Escrever rótulos em campos que toda a unidade vê expõe a pessoa e não ajuda no cuidado.")

    if tem("sem_ss", "ss_sem_renato"):
        jump renato_epilogo
    jump renato_cena7


## ═════════════════════════════════════════════════════════════════════════════
## CENA 7 — Serviço Social · Seu olhar: Assistente social da UPA
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena7:
    $ olhar("Assistente social da UPA")
    scene bg aqua_servico_social with fade
    window show

    python:
        evolucao_lida = "a situação de rua"
        if not tem("sem_saude_mental"):
            evolucao_lida += ", o sono, a depressão"
        if not tem("sem_repasse"):
            evolucao_lida += ", a preocupação com o remédio"
        evolucao_lida += ", o plano"
    if tem("sem_registro"):
        narr "O médico do consultório 2 passou aqui às 14h50 e disse que o paciente está em situação de rua. Na evolução, só a pressão. Renato vai ter de contar tudo de novo."
    else:
        narr "O médico do consultório 2 passou aqui às 14h50. Antes de falar com Renato, você lê a evolução: [evolucao_lida]. Ele não vai precisar contar tudo de novo."
    narr "A sala do Serviço Social é pequena: uma mesa, duas cadeiras e o celular do serviço. No mural, uma lista de contatos da rede, com números riscados e reescritos à caneta."

    show renato hesitante at center with dissolve
    assist_voce "Seu Renato, boa tarde. Eu sou do Serviço Social da UPA. Primeiro, eu vou fazer algumas perguntas sobre a sua situação e a sua família, pra entender como posso ajudar. Pode ser?"
    renato "Pode."
    narr "Enquanto preenche a entrevista social, você pergunta sobre trabalho, renda, família e onde ele costuma ficar."
    assist_voce "E hoje à noite, o senhor vai ficar onde?"
    renato "Perto da rodoviária. Durmo ali, debaixo de uma marquise. De dia eu fico na praça, no coreto."
    assist_voce "Alguém da saúde já acompanha o senhor? Posto? Consultório na Rua?"
    renato "Não. Antes eu tinha plano. Nunca precisei de posto."
    assist_voce "E documento, o senhor tem algum?"
    renato "Só sei o CPF. O resto foi junto com a mochila."
    assist_voce "Hoje o senhor tem renda? Recebe algum benefício?"
    renato "Nada. Faço um bico ou outro quando aparece."
    narr "Ao longo da conversa, você explica que ele pode ter direito a benefícios sociais e que o primeiro passo é o Cadastro Único, feito pela assistência social."
    narr "Falta acionar quem vai acompanhar Renato no território: a equipe do Consultório na Rua. Na sua frente, há mais dois casos esperando."

    menu:
        narr "A continuidade do cuidado depende de a equipe do Consultório na Rua saber de Renato e conseguir encontrá-lo. Como você faz o contato?"

        "Ligar para o Consultório na Rua com Renato no viva-voz, para ele mesmo combinar com a equipe.":
            $ escolher(9, "A")
            narr "Você liga para o número da equipe. Chama até cair. Liga de novo: caixa postal."
            assist_voce "Não atenderam. Eles passam o dia na rua, atendendo. Vou mandar uma mensagem, que é como eles recebem os casos."
            call resultado("Incluir Renato na conversa é o caminho certo. Mas, em João Pessoa, a equipe do Consultório na Rua recebe os casos por mensagem: o telefone nem sempre é atendido, porque a equipe passa o dia no território.")
            call renato_mensagem_com_renato

        "Mandar logo a mensagem com os dados da ficha e o resumo do atendimento: há dois casos esperando, e o importante é a equipe saber.":
            $ escolher(9, "B")
            narr "Enquanto Renato espera, você envia ao contato da equipe os dados da ficha, o resumo da evolução e os lugares que ele citou. Não comenta com ele: o importante é a equipe saber."
            call resultado("A equipe foi acionada, e isso conta. Mas os dados foram enviados sem que Renato soubesse, e ele saiu sem saber quem vai procurá-lo, nem quando, nem onde. O consentimento também aumenta a chance do encontro.")

        "Explicar o que é o Consultório na Rua, pedir autorização para mandar os dados e uma foto, perguntar onde ele costuma ficar e enviar a mensagem com ele ali.":
            $ escolher(9, "C")
            call renato_mensagem_com_renato
            call resultado("Em João Pessoa, o Consultório na Rua recebe os casos por mensagem: dados, local onde a pessoa fica e, se ela autorizar, uma foto. Renato autorizou e sabe quem vai procurá-lo, quando e onde.")

    window show
    narr "A partir desse contato, é o Consultório na Rua que acompanha Renato, atualiza o cadastro dele, o vincula a uma UBS de referência e articula, com a rede de atenção à saúde e os demais serviços, as necessidades identificadas hoje."
    narr "Faltam os documentos e um lugar para dormir: demandas da assistência social."

    menu:
        narr "São 16h. O Centro POP, serviço da assistência social, fica a vinte minutos a pé e atende até as cinco da tarde. O que você faz?"

        "Explicar o que o Centro POP oferece e fazer um encaminhamento por escrito, informando que ele usa medicação.":
            $ escolher(10, "A")
            assist_voce "Documento a gente não tira aqui, não. Quem cuida disso é a assistência social, no Centro POP. Lá eles podem orientar e ajudar o senhor com essa documentação e com os benefícios sociais."
            assist_voce "Lá também podem guardar as coisas de quem precisa, e o senhor pode dar o endereço de lá quando pedirem. Vou fazer um encaminhamento para o Centro POP, para que eles possam dar continuidade ao seu atendimento."
            renato "Tenho interesse em conhecer."
            assist_voce "E, se o senhor desejar, a equipe de lá também pode avaliar e articular uma vaga numa casa de acolhimento. Lá tem cama, banho e comida."
            renato "{i}(pausa){/i} Fui num albergue uma vez. Não deu certo."
            assist_voce "Pode ser diferente. O senhor é quem sabe, e pode conversar com eles sobre isso."
            renato "Lá dá pra guardar o remédio?"
            assist_voce "Essa informação a gente pode confirmar com a equipe do Centro POP. No encaminhamento, também vou informar que o senhor está fazendo uso de medicação."
            narr "Você escreve o encaminhamento e entrega a ele. Renato lê até o fim, corrige a grafia do sobrenome e guarda no caderno."
            call resultado("O encaminhamento por escrito leva a história de Renato junto, e o Centro POP sabe por que ele chegou. Documentos, benefícios e acolhimento ficaram com quem cuida deles: a assistência social.")

        "Passar o endereço e o horário do Centro POP, para ele ir quando puder.":
            $ escolher(10, "B")
            assist_voce "Documento e vaga pra dormir é com o Centro POP. Fica na Rua Treze de Maio, abre das oito às cinco. O senhor procura lá."
            narr "Renato anota o endereço no caderno."
            renato "Hoje ainda dá?"
            assist_voce "Se o senhor for agora, dá."
            call resultado("O endereço certo é um começo. Mas apenas informar não garante o acesso: Renato vai ter de explicar tudo de novo e descobrir sozinho como ser atendido. O encaminhamento por escrito leva a história dele junto.")

        "Deixar os documentos e a vaga para o Consultório na Rua resolver a partir de amanhã, já que a equipe vai acompanhá-lo.":
            $ escolher(10, "C")
            assist_voce "A equipe do Consultório na Rua vai procurar o senhor amanhã. Documento e lugar pra dormir o senhor vê com eles, tá?"
            renato "Tá."
            call resultado("O Consultório na Rua articula a rede, mas documentos, benefícios e acolhimento são da assistência social, e a UPA pode encaminhar hoje. Deixar para amanhã é mais uma noite na marquise.")

    jump renato_cena8


## Mensagem com Renato presente (Decisão 9, opções A e C)
label renato_mensagem_com_renato:
    window show
    assist_voce "Seu Renato, existe uma equipe de saúde chamada Consultório na Rua, que atende as pessoas nos lugares onde elas costumam ficar. Posso passar sua situação pra essa equipe?"
    renato "Pode."
    assist_voce "E, se o senhor autorizar, posso mandar uma foto sua, pra ficar mais fácil eles encontrarem o senhor. Só se o senhor quiser."
    renato "{i}(pensa){/i} Pode mandar."
    assist_voce "O senhor costuma ficar mais por onde? Assim eu digo pra eles onde é mais fácil achar o senhor."
    show renato aberto at center with dissolve
    renato "De dia, na praça. No coreto. De noite, perto da rodoviária."
    narr "Com a autorização de Renato, você envia a mensagem ao contato da equipe: nome, CPF, data de nascimento, o resumo do atendimento de hoje, os lugares onde ele costuma ficar e a foto."
    narr "Vinte minutos depois, chega a resposta."
    call mensagem("Mensagem recebida", "Boa tarde! Recebido. Vamos encontrar o Sr. Renato amanhã pela manhã, no coreto da praça, para dar continuidade ao acompanhamento. — Marcos, agente social, Consultório na Rua.")
    window show
    assist_voce "Seu Renato, a equipe respondeu. Eles vão encontrar o senhor amanhã de manhã, no coreto. Quem assinou foi o Marcos, agente social da equipe. O senhor consegue estar lá nesse horário?"
    renato "Consigo, sim. Vou esperar a equipe."
    assist_voce "Leva a receita e o que mais tiver de papel, viu?"
    show caderno at obj_dir with dissolve
    narr "Renato abre o caderno e anota: Consultório na Rua. Marcos. Amanhã de manhã, coreto. Levar receita."
    hide caderno with dissolve
    return


## ═════════════════════════════════════════════════════════════════════════════
## CENA 8 — Saída · Seu olhar: Assistente social da UPA (continua)
## ═════════════════════════════════════════════════════════════════════════════

label renato_cena8:
    scene bg aqua_saida with fade
    window show
    narr "Você acompanha Renato até a porta."
    show renato despedida at center with dissolve
    narr "Na porta, ele para e se vira, com o caderno na mão."

    if tem("renato_sem_saber"):
        renato "E daqui a uma semana, quem vai medir minha pressão?"
        narr "Você lembra que mandou a mensagem à equipe, mas ainda não teve resposta e não contou a ele."
    else:
        renato "E se a equipe do Consultório na Rua não for amanhã?"

    menu:
        narr "Renato está com medo de que o próximo passo não dê certo. O que você deixa com ele?"

        "Tranquilizá-lo: a equipe do Consultório na Rua foi avisada e vai procurá-lo.":
            $ escolher(11, "A")
            assist_voce "Pode ficar tranquilo, seu Renato. A equipe já tá avisada e vai procurar o senhor."
            renato "{i}(pausa){/i} Tá certo."
            call resultado("Tranquilizar é cuidado, mas a garantia não está nas suas mãos: a equipe pode precisar atender outra demanda ou ter sua programação alterada. Uma promessa que falha pesa mais do que uma alternativa anotada.")

        "Escrever no caderno uma alternativa para o caso de desencontro.":
            $ escolher(11, "B")
            assist_voce "Me empresta o caderno?"
            show caderno at obj_dir with dissolve
            if tem("renato_sem_saber"):
                narr "Na contracapa, embaixo do CPF, você escreve o endereço e o horário do Centro POP e o nome da equipe do Consultório na Rua que foi avisada."
            else:
                narr "Na contracapa, embaixo do CPF, você escreve o endereço e o horário do Centro POP e o nome da equipe do Consultório na Rua que respondeu."
            hide caderno with dissolve
            assist_voce "Se vocês se desencontrarem, procura o Centro POP: lá eles falam com a equipe. E se a dor de cabeça voltar forte, ou der dor no peito, aí é aqui, a qualquer hora."
            narr "Renato lê o que você escreveu e fecha o caderno."
            renato "Tá certo. Obrigado."
            call resultado("Você não prometeu o que não depende de você. Deixou um caminho escrito, que leva à rede e não de volta à urgência.")

        "Dizer que, se não der certo, ele pode voltar aqui na UPA e procurar o Serviço Social.":
            $ escolher(11, "C")
            assist_voce "Se não der certo, o senhor volta aqui e me procura, tá?"
            renato "Aqui?"
            assist_voce "Aqui."
            call resultado("Deixar uma porta aberta é acolhedor. Mas a UPA não é a referência para o acompanhamento contínuo da pressão, e voltar significa enfrentar a espera de novo. A alternativa precisa levar à rede.")

    window show
    show renato aberto at center with dissolve
    if tem("adiado_cnar"):
        narr "Renato põe o caderno debaixo do braço e sai. Até a rodoviária, são vinte minutos a pé."
    else:
        narr "Renato põe o caderno debaixo do braço e sai. Até o Centro POP, são vinte minutos a pé."
    hide renato with dissolve

    if tem("renato_sem_saber"):
        narr "A resposta da equipe chega às 16h20, quando Renato já saiu."
        call mensagem("Mensagem recebida · 16h20", "Recebido. Vamos procurá-lo amanhã pela manhã, no coreto. Sem foto, vamos perguntar no território. — Marcos, agente social, Consultório na Rua.")

    stop music fadeout 3.0

    call reflexao("Mandar os dados para o Consultório na Rua aciona a equipe. O encontro tem mais chances de acontecer quando o próprio Renato autoriza o que vai ser dito, diz onde costuma ficar e sabe quem vai procurá-lo e quando.", "Documento, acolhimento e renda são da assistência social. Quem trabalha na saúde precisa saber para onde encaminhar essas demandas, encaminhar por escrito, e não pode fazer da falta de documento uma barreira para o atendimento.")

    jump renato_epilogo
