# scripts/

## gerar_imagens.py — geração de arte com gpt-image-1 (OpenAI)

Reproduz o pipeline usado na entrega de 14-15/07/2026 (ver `assets-gerados/PROMPTS-GERADOS.md`):
o prompt descreve só o **conteúdo**, e o script anexa o **bloco de estilo** do jogo.

### Preparo

```bash
pip install openai pillow
```

Chave da API em `OPENAI_API_KEY` — variável de ambiente ou arquivo `.env` na raiz
(`.env` já está no `.gitignore`, nunca commitar):

```
OPENAI_API_KEY=sk-...
```

### Uso

```bash
# lote (recomendado) — copie o exemplo e edite
python scripts/gerar_imagens.py --lista scripts/imagens.json

# ver os prompts finais sem gastar crédito
python scripts/gerar_imagens.py --lista scripts/imagens.json --simular

# só um item da lista, refazendo o arquivo existente
python scripts/gerar_imagens.py --lista scripts/imagens.json --apenas obj_mochila_renato --substituir

# imagem avulsa
python scripts/gerar_imagens.py --estilo cenario --nome cen_praca_noite \
    --prompt "A small city square at night, empty benches, a lit lamppost"
```

### Estilos

| estilo | bloco | tamanho padrão | fundo |
|---|---|---|---|
| `cenario` | aquarela, fundo de visual novel | 1536x1024 | opaco |
| `objeto` | aquarela, estudo de objeto | 1024x1024 | transparente |
| `personagem` | sprite comic semi-realista, corpo inteiro | 1024x1536 | transparente |
| `ui` | peça de interface pintada à mão | 1024x1024 | transparente |
| `nenhum` | nenhum bloco (prompt cru) | 1024x1024 | opaco |

Sobrescreva por item na lista (`tamanho`, `transparente`, `saida`, `bloco_extra`)
ou globalmente pela linha de comando (`--tamanho`, `--qualidade`, `--saida`).

### Comportamento

- Salva PNG em `assets-gerados/` (ou `saida`) e **pula arquivos já existentes** — use `--substituir` para refazer.
- Confere o canal alpha com Pillow quando o fundo deveria ser transparente e avisa se saiu opaco
  (acontece com sprites de corpo inteiro; nesse caso reforce o recorte no prompt e refaça).
- Registra prompt, tamanho, qualidade e tempo em `_geracao_log.json` na pasta de destino.
- Repete até 3 vezes por imagem em caso de erro de rede/rate limit (`--tentativas`).
