# Arte do Além da Rua

Como gerar as imagens do jogo com o mesmo estilo e os mesmos personagens, entregar e colocar no jogo.

- **Pedidos e entregas:** issues com a etiqueta `frente:arte` no [Project](https://github.com/orgs/pet-saude-poprua/projects/1). Uma issue por imagem.
- **Model sheets e acervo:** [pasta de arte no Drive](https://drive.google.com/drive/folders/1LJwdm2SyJAL7FwMZ1yuR0zbXdJ3yln7p) (Personagens, Cenários, Objetos, Sprites).
- **Assistente:** GPT “Arte Além da Rua” (ChatGPT) e Gem “Arte Além da Rua” (Gemini), com o guia de estilo e as model sheets já carregados. Links: _(o Breno cola aqui depois de criar)_.

## Para quem gera a imagem (5 passos)

1. **Pegue uma issue de arte** com a etiqueta `disponível`: atribua-se e mova o card para **Em andamento**.
2. **Abra o assistente** (GPT ou Gem). Sem acesso a eles, qualquer ChatGPT ou Gemini serve.
3. **Anexe as referências** listadas na issue (model sheets e imagens do jogo) e **cole o prompt** da issue, sem resumir.
4. **Confira o checklist** da issue. Se algo sair errado, peça só o ajuste (“mantenha tudo, mude só X”).
5. **Entregue:** comente na issue com a imagem anexada (o PNG original) e diga a ferramenta. Mova o card para **Em revisão**.

Regras que mais derrubam uma imagem: texto legível, pessoas no fundo do cenário, personagem diferente da model sheet, sprite/objeto sem fundo transparente, formato errado (cenário é 16:9 paisagem; sprite é vertical).

Precisa de uma imagem que não tem issue? Abra uma com o formulário **“🎨 Pedido de arte”**.

## Para o Breno (implementação)

```bash
# prompts prontos de uma história (arte/prompts/<historia>.md)
python3 scripts/arte.py prompts --historia renato

# uma issue por pedido no Project (rodar de novo não duplica; --atualizar reescreve o corpo)
python3 scripts/arte.py issues --historia renato --simular
python3 scripts/arte.py issues --historia renato

# trazer a imagem entregue: confere, recorta/redimensiona, converte para WebP e grava em game/images/
python3 scripts/arte.py importar --issue 130
python3 scripts/arte.py importar --arquivo entrega.png --pedido renato/aqua_classificacao

# instruções do GPT/Gem (depois de mudar estilo.json ou personagens.json)
python3 scripts/arte.py assistente
```

O `importar` mostra a linha `image …` a usar e a definição atual que ela substitui. O encaixe na cena e o fechamento da issue ficam com você.

Para gerar direto pela API da OpenAI (pago), use `scripts/gerar_imagens.py`, que lê os mesmos blocos de `estilo.json`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `estilo.json` | Fonte única do estilo: blocos por tipo (cenário, sprite, objeto, cena composta, overlay, ui), bloco negativo, regras, tamanhos no jogo |
| `personagens.json` | Ficha fixa de cada personagem (aparência em inglês) e link da model sheet |
| `pedidos/<historia>.json` | Imagens que a história precisa; `id` = nome do arquivo e da imagem no código |
| `prompts/<historia>.md` | Gerado: prompts prontos com referências e checklist |
| `assistente/INSTRUCOES.txt` | Gerado: instruções do GPT e do Gem |

Personagem novo: gere primeiro a **model sheet** (frente, perfil, costas, expressões), guarde na pasta Personagens do Drive e acrescente a ficha em `personagens.json`. Só depois peça sprites e cenas com ele.

## Criar o GPT e o Gem (uma vez)

**Arquivos de conhecimento** (os mesmos nos dois): as model sheets da pasta Personagens do Drive, renomeadas com o nome do personagem (`renato_model_sheet.jpg`, `camila_assistente_social_model_sheet.jpg`, `livia_tecnica_enfermagem_model_sheet.jpg`, `medico_upa_model_sheet.jpg`, `recepcionista_upa_model_sheet.jpg`), `game/images/bg/aqua_recepcao.jpg`, `game/images/bg/aqua_consultorio.jpg`, `game/images/chars/medico_upa.webp` (único sprite já no visual das model sheets), `arte/estilo.json` e `arte/personagens.json`.

**A model sheet manda.** Os sprites antigos de Renato e Camila (camisa xadrez, cardigã) destoam das model sheets e estão sendo refeitos; não use esses sprites como referência de personagem, só de pose.

**ChatGPT (precisa de Plus para criar):** Explorar GPTs → Criar → Configurar. Nome “Arte Além da Rua”; em Instruções, cole `assistente/INSTRUCOES.txt`; em Conhecimento, envie os arquivos acima; em Recursos, deixe **Geração de imagens** ligada. Compartilhar → “Qualquer pessoa com o link”.

**Gemini (gratuito):** Gems → Novo Gem. Nome “Arte Além da Rua”; em Instruções, cole o mesmo texto; em Conhecimento, envie os mesmos arquivos. Salve e compartilhe o link.

Quando `estilo.json` ou `personagens.json` mudarem, rode `scripts/arte.py assistente` e cole o texto novo nos dois. O GPT aceita até 8.000 caracteres de instruções; se passar, tire os blocos de estilo do texto e deixe só o `estilo.json` no conhecimento.
