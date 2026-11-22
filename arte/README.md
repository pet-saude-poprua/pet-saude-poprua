# Arte do Além da Rua

Como gerar as imagens do jogo com o mesmo estilo e os mesmos personagens, entregar e colocar no jogo.

- **Pedidos e entregas:** issues com a etiqueta `frente:arte` no [Project](https://github.com/orgs/pet-saude-poprua/projects/1). Uma issue por imagem.
- **Model sheets e acervo:** [pasta de arte no Drive](https://drive.google.com/drive/folders/1LJwdm2SyJAL7FwMZ1yuR0zbXdJ3yln7p) (Personagens, Cenários, Objetos, Sprites).
- **Assistente:** habilidade “arte-alem-da-rua” do Gemini (gratuita), com as instruções, as fichas e as model sheets já carregadas. [Baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e, no Gemini, vá em **Habilidades → Criar → Enviar** e escolha o arquivo. Depois é só pedir a imagem numa conversa. Quem tem ChatGPT Plus pode montar um Projeto com os mesmos arquivos (ver abaixo).

## Para quem gera a imagem (5 passos)

1. **Pegue uma issue de arte** com a etiqueta `disponível`: atribua-se e mova o card para **Em andamento**.
2. **Abra o assistente** (a habilidade do Gemini, ou o seu Projeto no ChatGPT). Sem eles, qualquer ChatGPT ou Gemini serve: o prompt da issue já é completo.
3. **Anexe as referências** listadas na issue (model sheets e imagens do jogo) e **cole o prompt** da issue, sem resumir.
4. **Confira o checklist** da issue. Se algo sair errado, peça só o ajuste (“mantenha tudo, mude só X”).
5. **Entregue:** comente na issue com a imagem anexada (o PNG original) e diga a ferramenta. Mova o card para **Em revisão**.

Regras que mais derrubam uma imagem: texto legível, pessoas no fundo do cenário, personagem diferente da model sheet, sprite/objeto com fundo branco (tem de ser transparente ou magenta puro #FF00FF, sem sombra), formato errado (cenário é 16:9 paisagem; sprite é vertical).

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

# instruções do Gem/Projeto (depois de mudar estilo.json ou personagens.json)
python3 scripts/arte.py assistente
```

O `importar` tira sozinho o fundo magenta (#FF00FF) de sprites e objetos e mostra a linha `image …` a usar e a definição atual que ela substitui. O encaixe na cena e o fechamento da issue ficam com você.

Para gerar direto pela API da OpenAI (pago), use `scripts/gerar_imagens.py`, que lê os mesmos blocos de `estilo.json`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `estilo.json` | Fonte única do estilo: blocos por tipo (cenário, sprite, objeto, cena composta, overlay, ui), bloco negativo, regras, tamanhos no jogo |
| `personagens.json` | Ficha fixa de cada personagem (aparência em inglês) e link da model sheet |
| `pedidos/<historia>.json` | Imagens que a história precisa; `id` = nome do arquivo e da imagem no código |
| `prompts/<historia>.md` | Gerado: prompts prontos com referências e checklist |
| `assistente/INSTRUCOES.txt` | Gerado: instruções do Projeto do ChatGPT |
| `assistente/INSTRUCOES_GEMINI.txt` | Gerado: instruções da habilidade do Gemini (com as fichas) |
| `assistente/arte-alem-da-rua.zip` | Gerado (fora do git): a habilidade do Gemini pronta para enviar |
| `referencias/` | Model sheets aprovadas (cópia das da pasta Personagens do Drive); entram na habilidade |

**Personagem novo (nesta história ou nas próximas):** a model sheet vem antes de qualquer sprite ou cena.
1. Acrescente a ficha em `personagens.json` (aparência em inglês, sem pose fixa; `model_sheet` vazio) e um pedido do tipo `model_sheet` em `pedidos/<historia>.json`; rode `arte.py issues`.
2. Alguém gera a sheet pela issue (mesmo layout e traço das sheets atuais) e entrega na issue.
3. A autora da história e a Saúde aprovam na issue.
4. A sheet aprovada vai para a pasta Personagens do Drive e para `arte/referencias/<ficha>_model_sheet.jpg`; preencha `model_sheet` na ficha, rode `arte.py habilidade` e substitua a habilidade no Gemini (⋯ → Substituir habilidade).
5. Só então peça sprites e cenas com o personagem.

## Criar o assistente (uma vez)

Os GPTs personalizados do ChatGPT serão descontinuados em 11/12/2026; por isso o assistente compartilhado é uma habilidade do Gemini (antigo Gem).

**Arquivos de conhecimento** (os mesmos no Gem e no Projeto; 18 arquivos, o limite é 20):
- model sheets da pasta Personagens do Drive, com o nome da ficha: `renato_model_sheet.jpg`, `assistente_social_model_sheet.jpg`, `colega_enfermagem_model_sheet.jpg`, `medico_upa_model_sheet.jpg`, `recepcionista_model_sheet.jpg`, `marcos_model_sheet.jpg`;
- `senhora_referencia.webp` (= `game/images/chars/senhora.webp`, ela não tem model sheet) e `game/images/chars/medico_upa.webp`;
- cenários de `game/images/bg/`: `aqua_recepcao`, `aqua_consultorio`, `aqua_espera`, `aqua_corredor`, `aqua_fachada`, `aqua_box`, `aqua_esus` (overlay);
- objetos de `game/images/obj/`: `caderno_renato.webp`, `obj_receita_medica.webp`;
- `arte/estilo.json` e `arte/personagens.json`.

**A model sheet manda.** Os sprites antigos de Renato e Camila (camisa xadrez, cardigã) destoam das model sheets e estão sendo refeitos; não use esses sprites como referência de personagem, só de pose.

**Gemini (gratuito, compartilhável):** a habilidade é gerada pelo repositório. Rode `python3 scripts/arte.py habilidade`: ele monta `arte/assistente/arte-alem-da-rua.zip` (SKILL.md com as instruções e as fichas + model sheets de `arte/referencias/` + cenários e objetos de exemplo). No Gemini: **Habilidades → Criar → Enviar** (primeira vez) ou **⋯ → Substituir habilidade** (atualização), escolhendo esse .zip. Para compartilhar: ⋯ → Compartilhar habilidade → Qualquer pessoa com o link; o Gemini cria o .zip na pasta “Gemini Skills” do Drive.

**Nunca troque o .zip compartilhado direto no Drive** (Gerenciar versões): o Gemini bloqueia a habilidade (“Precisa de revisão”). Se o link mudar depois de uma atualização, troque `HABILIDADE_LINK` em `scripts/arte.py` e rode `arte.py issues --historia <h> --atualizar`.

**ChatGPT (Plus, uso pessoal):** barra lateral → Novo projeto “Arte Além da Rua”; nas instruções do projeto, cole o mesmo texto; em Arquivos, envie os mesmos arquivos. Toda conversa dentro do projeto já sai com estilo e personagens.

Quando `estilo.json`, `personagens.json` ou as model sheets mudarem, rode `scripts/arte.py habilidade`, substitua a habilidade no Gemini e cole o `INSTRUCOES.txt` novo no Projeto do ChatGPT. Mantenha o texto abaixo de 8.000 caracteres; se passar, tire os blocos de estilo do texto e deixe só o `estilo.json` no conhecimento.
