# Renato v4 — inventário de reaproveitamento

Tarefa da ata de 11/11/2026: identificar quais cenários e componentes já produzidos podem ser mantidos na versão revisada da história do Renato e quais precisam de trabalho novo.

Levantamento feito em 19/11/2026, comparando o roteiro v4 (revisão de 19/11) com `game/images/`, `game/audio/` e o código da v0.3.

## Por cena

| Cena | O que a cena pede | Já existe | Falta |
|---|---|---|---|
| 1 · Recepção | Recepção, balcão, Renato hesitante, caderno, tela do sistema, senhora da primeira fileira (ramo `exposto_recepcao`) | `bg aqua_recepcao`, `bg aqua_balcao`, `renato hesitante`, `caderno`, `esus`, `senhora` | — |
| 2 · Classificação | Sala de classificação de risco, Renato sentado, pulseira (opcional) | `renato hesitante` | **Cenário da sala de classificação** (hoje usa `aqua_consultorio`, provisório). Pulseira amarela/laranja (opcional) |
| 3 · Sala de espera | Sala de espera, Renato à porta | `bg aqua_espera`, `renato hesitante` | — |
| 4 · Consulta | Consultório, médico no início, tela do prontuário | `bg aqua_consultorio`, `medico_upa`, `esus`, `renato aberto` | — |
| 5 · Observação | Sala de observação com poltronas, posto de enfermagem, colega da enfermagem | `bg aqua_box` (provisório), `bg aqua_corredor`, `renato normal` | **Cenário da sala de observação** no estilo `aqua_` (existe `upa_sala_observacao.webp`, mas em outro estilo; ver #98). Sprite da colega (opcional) |
| 6 · Alta | Consultório, receita, corredor, assistente social | `bg aqua_consultorio`, `receita`, `bg aqua_corredor`, `assistente` | — |
| 7 · Serviço Social | Sala do Serviço Social, celular do serviço | `assistente`, tela de mensagem (feita em código) | **Cenário da sala do Serviço Social** (hoje usa `aqua_consultorio`). Encaminhamento escrito (opcional) |
| 8 · Saída | Porta da UPA no fim da tarde | `bg aqua_saida`, `renato despedida`, `renato aberto` | — |
| Epílogo | Fundos neutros, caderno, medidores, mapa | `bg neutro_*`, telas em código | — |
| Áudio | Ambiente da UPA, música da reflexão | `ambiente_upa.ogg`, `reflexao.ogg` | Efeitos sonoros (#6) continuam opcionais |

## Tarefas de arte que saem daqui

1. Cenário: sala de classificação de risco (estilo aquarela `aqua_`, 1280x720).
2. Cenário: sala de observação com poltronas (estilo `aqua_`).
3. Cenário: sala do Serviço Social (mesa, duas cadeiras, mural de contatos).
4. Opcionais: pulseira amarela e laranja; colega da enfermagem; folha de encaminhamento.

## Arquivos que não são mais usados pelo jogo

Ficam no repositório até a equipe de arte decidir (nada foi apagado):

- `bg/upa_*.webp` (5), `bg/titulo.webp`, `bg/Teste001.webp`, `bg/Img2.webp`, `bg/consulta_anamnese.webp`;
- `chars/*-removebg-preview.*` (7 cópias em PNG/WebP dos sprites);
- `chars/SenhoraFofoqueira.webp`, `SenhorFofoqueiro.webp`, `RenatoFofocado.webp`, `RecepcionistaChamandoRenato.webp`, `outro_paciente.webp`, `consulta_medico_renato.webp`, `renato_emocionado.webp`;
- `obj/obj_carteira_trabalho.webp`, `obj/obj_cartao_sus.webp` (a v4 não usa carteira de trabalho nem Cartão SUS).

## Código da v0.3

| Peça | Destino |
|---|---|
| Medidores, `ajustar()`, nós da rede | Generalizados em `game/nucleo/estado.rpy` (tabela de decisões por história) |
| `reflexao_card`, `contexto_real`, `epilogo_medidores` | `game/nucleo/telas.rpy` (`card`, `contexto_real`, `painel_final`) |
| Personagens, cenários, transforms | `game/nucleo/personagens.rpy` |
| Menus "Casos" e "Progresso" | `game/telas_menu.rpy`, agora lendo o registro de histórias |
| Roteiro antigo (`missao1.rpy`) | Removido; preservado na tag `v0.3-roteiro-v1` (a criar) e no histórico do git |
