# Padrões Visuais — Caminho de Criação das Telas da História do Renato

> **Para gerar imagens novas, use o kit em [`arte/`](../arte/README.md)**: estilo, fichas dos personagens, prompts prontos e pedidos no Project. Este documento registra a direção visual definida no protótipo.

**Projeto:** Visual novel educacional PET-Saúde Pop Rua (GT6) · **Versão:** 1.0 — 14/07/2026
**Decisão de base (ata 01/07):** fundos em **aquarela digital suave** + **personagens em ilustração mais definida** que "saltam" sobre o fundo dessaturado.

---

## 1. O padrão aquarela (bloco de estilo mestre)

Todo cenário é gerado colando este bloco ao final da descrição da cena (fonte: `01-07/PROMPTS-CENARIOS-MISSAO1.md`):

```
digital watercolor illustration, soft loose washes, muted faded pastel palette,
simplified almost cartoonish shapes, minimal fine detail, gentle soft edges,
light paper texture, slightly desaturated, calm subdued mood, soft background blur,
mobile visual novel background, clean uncluttered composition, eye-level view,
empty center and lower foreground reserved for characters, no people, no characters,
no text, no letters, 16:9 landscape
```

**Regras de ouro** (o que mantém o conjunto coeso):
1. **Sem pessoas nos fundos** — personagens entram como sprites por cima (exceção única: o fundo do menu, que é ilustração de capa).
2. **Sem texto legível** — placas, cartazes e telas viram manchas de cor.
3. **Centro e base livres** para os sprites e a caixa de diálogo.
4. **Paleta contínua entre cenas:** bege/ocre/verde-oliva nos interiores quentes → teal/branco no box clínico → dourado-alaranjado no entardecer.
5. Ponto de vista à altura dos olhos; baixo contraste; textura de papel visível.

Variações do bloco: **objetos** (single object study, fundo transparente, sombra suave) e **neutros** (mesmo bloco, sem arquitetura reconhecível — usados em reflexões e transições).

## 2. Personagens

Estilo distinto **de propósito**: ilustração semirrealista com luz suave (fichas em `Imagens/Personagens/`), para destacar a pessoa sobre o fundo aquarela — a mensagem visual do projeto (a pessoa antes do cenário).

- Fichas prontas: Renato · Marcos (CNR) · Médico · Assistente Social (Camila) · Recepcionista · Técnica de Enfermagem (Lívia).
- **Novos nesta entrega** (`assets-gerados/`): a **senhora da sala de espera** e o **outro paciente** (NPCs da Cena 1) — já contemplando a **diversidade corporal** pedida na ata.
- Pipeline S1: fatiar as fichas em sprites individuais por pose/expressão, com fundo transparente, exportados a ~1000px de altura.

## 3. Inventário atual

| Grupo | Qtde | Estado |
|---|---|---|
| Cenários da missão (16:9, 1600x900) | 9 | ✅ completos — fachada, recepção, sala de espera, balcão, consultório, box, corredor, saída ao entardecer, overlay e-SUS |
| Fundos neutros (16:9) | 8 | ✅ completos — N1–N8 (reflexões, transições, epílogo) |
| Objetos | 1 → 4 | caderno ✅ · **novos:** carteira de trabalho, Cartão SUS, receita (`assets-gerados/`) |
| Fichas de personagens | 6 + 2 novos | ✅ · falta fatiar em sprites (S1) |
| Fundo de menu aquarela | 1 | **novo** (`assets-gerados/menu_upa_entardecer.png`) |

**Fora do padrão (não usar):** os 3 cenários verticais (estilo saturado tipo anime, texto embutido com erros, multidão pintada no fundo) — conflitam com as regras 1–4. Se o formato retrato voltar a ser necessário, regenerar a partir do bloco mestre.

**Lacunas conhecidas** (geram na S1, sob demanda da implementação): close do monitor multiparâmetro (a cena do box já o mostra no fundo), variação noturna da recepção, sprite do médico de plantão cansado.

## 4. Anatomia da tela da história (o "caminho de criação")

Cada tela da história do Renato é montada em camadas:

```
[1] Fundo aquarela (cena)          ← 9 cenários prontos
[2] Sprite(s) do personagem         ← fichas fatiadas / novos NPCs
[3] Objeto em destaque (quando há)  ← caderno, carteira, cartão, receita
[4] Caixa de diálogo translúcida    ← faixa de cor por personagem
[5] HUD: medidor de Empatia         ← único visível em tempo real
[6] Overlays por momento            ← e-SUS, mapa de nós, cards
```

Os mockups em `docs/mockups/` mostram a régua aplicada: cena de diálogo (Renato na sala de espera), tela de decisão A/B/C e cena com objeto (caderno). Cores de faixa por personagem seguem `characters.rpy` (Renato azul `#5C8FB3`, técnica verde `#7CA982`, assistente âmbar `#B38B59`, médico vinho `#A55858`).

## 5. Pipeline de geração (reprodutível)

1. Escrever a descrição da cena/objeto/personagem em 1 parágrafo (sem estilo).
2. Colar o bloco de estilo correspondente (cenário/objeto/personagem).
3. Gerar em `gpt-image-1` (OpenAI): cenários 1536x1024 opacos · objetos 1024x1024 transparentes · personagens 1024x1536 transparentes; qualidade alta.
4. Conferir contra as regras de ouro (sem texto, sem pessoas, centro livre, paleta).
5. Salvar em `assets-gerados/` e registrar o prompt em `assets-gerados/PROMPTS-GERADOS.md`.

Prompts exatos das imagens novas desta entrega: `assets-gerados/PROMPTS-GERADOS.md`.
