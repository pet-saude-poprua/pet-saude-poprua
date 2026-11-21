# Guia: do roteiro ao código

Como uma história sai do roteiro (Google Doc) e entra no jogo usando o núcleo comum. Vale para as cinco histórias.

## 1. Estrutura de pastas

```
game/
  nucleo/            peças comuns (não depende de nenhuma história)
    estado.rpy       medidores, flags, decisões, mapa, "Retomar", progresso
    telas.rpy        cartão de reflexão/RESULTADO, "Seu olhar", mensagem, caderno,
                     contexto real, painel final (barras + mapa), encerramento
    personagens.rpy  narrador, profissionais "(você)", cenários, sprites, transforms
    inicio.rpy       label start e abertura conceitual
  historias/
    renato/          uma pasta por história
      dados.rpy      registro da história + tabela de decisões + desfecho/mapa/caderno
      cenas.rpy      cenas, na ordem do roteiro
      epilogo.rpy    contexto real, reflexão final, desfechos
```

Para criar a história nova, copie a pasta `renato/` como modelo.

## 2. `dados.rpy`

1. `registrar_historia("id", ordem=…, titulo=…, subtitulo=…, sinopse=…, label="id", decisoes=…, nos=[…], atalhos=[("Cena 4", "id_atalho_cena4")])`. A ficha aparece sozinha no menu Casos. `atalhos` é opcional: cada par (rótulo, label) vira um botão de teste na ficha, enquanto `MOSTRAR_ATALHOS_TESTE` (em `nucleo/estado.rpy`) for `True`. O label do atalho aplica as escolhas canônicas anteriores e pula para a cena (ver `renato_preparar_atalho` em `historias/renato/dados.rpy`).
2. A tabela de decisões copia o Quadro D1 do Apêndice D do roteiro:

```python
## BEGIN DECISOES_NOME
DECISOES_NOME = {
    1: {"A": ((1, 1, 1, 1), []),                     # ★
        "B": ((-1, 0, -1, 0), ["exposto_recepcao"])},
}
CANONICA_NOME = {1: "A"}
## END DECISOES_NOME
```

Os quatro números são ▲/▼ em unidades, na ordem Direito, Rede, Empatia, Acolhimento. Os marcadores BEGIN/END permitem que `scripts/simular_historia.py` leia a tabela no CI.

## 3. Cenas

| No roteiro | No código |
|---|---|
| Cabeçalho "Seu olhar" | `$ olhar("Enfermeiro(a) do acolhimento")` |
| Narração | `narr "…"` |
| FALA (você) | `recep`, `enf`, `med`, `tec`, `assist_voce` |
| ▶ DECISÃO n + opções | `menu:` com a pergunta em `narr` e uma opção por linha |
| Efeitos e flags da opção | `$ escolher(n, "B")` (lê a tabela; não escreva números na cena) |
| RESULTADO | `call resultado("…")` |
| Reflexão (card) | `call reflexao("linha 1", "linha 2")` |
| [Se flag: …] | `if tem("flag"):` |
| Mensagem de celular | `call mensagem("Mensagem recebida", "…")` |
| Saída antecipada com "Retomar" | `$ guardar_ponto(n)` antes da decisão e um label logo depois; no desfecho, `$ restaurar_ponto(n)` + `jump` para esse label |

Regras de texto:
- Falas e narrações com mais de ~220 caracteres viram duas linhas, divididas num ponto final, sem mudar o texto.
- Use aspas curvas (“ ”).
- Não escreva `[` nem `{` no texto: o Ren'Py usa esses sinais. Se precisar, escreva `[[` ou `{{`.
- Use só caracteres que a fonte do jogo tem. Setas como “→” aparecem como quadradinho: use “›” ou reescreva a frase.
- Escreva `%` como `%%` dentro de falas e narrações.

## 4. Epílogo

1. Contexto real: `call screen contexto_real(titulo, subtitulo, BLOCOS, FONTES, mais=BLOCOS_MAIS)`. `mais` é opcional: os blocos dele (por exemplo, a base conceitual) e as fontes abrem numa tela à parte, pelo botão “Saiba mais”, para o card principal não ficar longo demais.
2. Reflexão final.
3. Caderno (opcional): `call screen pagina_caderno(linhas)`.
4. Mapa da rede: acender e contornar os nós (`acender`, `contornar`), depois `call screen painel_final("A rede de …")`.
5. Desfecho.
6. `call encerrar_historia(desfecho)`, que grava o progresso.

## 5. Antes do PR

- `python3 scripts/simular_historia.py <id>`: confere a tabela e a linha canônica.
- `python3 scripts/testar_logica.py <id>`: executa a lógica Python (desfecho, mapa, caderno, barras) em todos os caminhos.
- O lint do Ren'Py roda no PR e falha se apontar algum problema.
- Jogue a linha canônica inteira e pelo menos um caminho de cada desfecho.
