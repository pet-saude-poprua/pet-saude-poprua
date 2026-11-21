# História 1 — Renato (documento de acompanhamento)

Documento pedido na ata de 11/11/2026: registra as dimensões que a história trabalha e o caso que a inspirou, fora do roteiro de falas.

| | |
|---|---|
| Personagem | Renato, 54 anos, ex-técnico de manutenção industrial, na rua há cerca de oito meses |
| Cenário | UPA de João Pessoa, uma quarta-feira (8h50 às 16h10) |
| Roteiro | Google Doc "ROTEIRO-VISUAL-NOVEL-v4 – Renato (corrigido + decisões)", pasta Frente TI - GT06 (revisões de 19 e 21/11/2026) |
| Código | `game/historias/renato/` (`dados.rpy`, `cenas.rpy`, `epilogo.rpy`) |
| Estado | Linha canônica validada pela equipe de saúde (v3, out–nov/2026). Decisões definidas pela Frente TI com base nas correções da saúde (Apêndice C do roteiro) |

## Dimensões trabalhadas

| Dimensão | Onde aparece |
|---|---|
| Direito em Saúde | Identificação sem documento nem Cartão SUS (D1); classificação pelo protocolo, não pela condição social (D2); sigilo (D6); consentimento para acionar a rede (D9) |
| Conhecimento da Rede | Serviço Social da UPA (D7), Consultório na Rua por mensagem (D9), Centro POP e acolhimento pela assistência social (D10), UBS de referência |
| Empatia / Sensibilidade Social | "Nem parece" (D6); sono e depressão (D4); preocupação com onde guardar o remédio (D5) |
| Acolhimento | Reavaliar quem fala em desistir (D3); explicar a espera (D2); não prometer o que não depende de você (D11) |

## Caso que inspirou

A confirmar com a equipe. A história foi escrita pela Frente TI a partir das reuniões do GT6 com o Consultório na Rua; registrar aqui se houve um caso relatado específico.

## Estrutura de jogo

- 8 cenas, 11 decisões (2 a 3 opções), 18 flags, 3 desfechos (A Rede ativada · B O encontro que não aconteceu · C A espera que venceu).
- Saídas antecipadas: C (Cena 3) e B pela Decisão 7, ambas com "Retomar a partir desta decisão".
- Simulação: `python3 scripts/simular_historia.py renato` (roda no CI).
