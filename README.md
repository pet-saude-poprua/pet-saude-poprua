# Caminhos do Cuidado *(nome provisório)*

Visual novel educacional sobre o cuidado à **população em situação de rua (PSR)**, desenvolvida pelo **PET-Saúde · GT6 Pop Rua · UFPB** — Frente TI.

O jogador é um profissional de saúde numa UPA e, a cada cena, troca de perspectiva (recepção, medicina, enfermagem, serviço social). Suas escolhas movem quatro dimensões do cuidado — **Direito em Saúde, Conhecimento da Rede, Empatia e Acolhimento** — reveladas apenas no epílogo, junto com o mapa dos nós da rede que foram (ou não) acionados.

## Como rodar o jogo

1. Baixe o [Ren'Py SDK 8.5.3](https://www.renpy.org/latest.html) e extraia em qualquer pasta.
2. Abra o `renpy.exe` (launcher), clique em **preferences → projects directory** e aponte para a pasta que contém este repositório.
3. Selecione o projeto e clique em **Launch Project**.

## Estrutura do repositório

| Pasta | O que tem |
|---|---|
| `game/` | O jogo (roteiro em `missao1.rpy`, telas, imagens, áudio, fontes) |
| [`docs/`](docs/) | Cronograma, fluxograma de navegação, estrutura de telas, padrões visuais e mockups |
| `assets-gerados/` | Imagens geradas por IA (com os prompts documentados em `PROMPTS-GERADOS.md`) |

## Documentação

| Documento | O que tem |
|---|---|
| [`docs/CRONOGRAMA.md`](docs/CRONOGRAMA.md) | Cronograma de desenvolvimento do protótipo (S0–S3, entrega 05/08) |
| [`docs/estrutura-telas.md`](docs/estrutura-telas.md) | Estrutura de menus e telas (10 telas + telas in-game, direção visual) |
| [`docs/fluxograma-navegacao.md`](docs/fluxograma-navegacao.md) | Fluxograma de navegação em Mermaid (menus + fluxo interno da História 1) |
| [`docs/padroes-visuais.md`](docs/padroes-visuais.md) | Padrões visuais — estilo aquarela, personagens, pipeline de geração |
| [`docs/mockups/`](docs/mockups/) | Mockups das telas (diálogo, decisão, objeto, menu) |

## Baixar o jogo pronto (builds)

Não precisa instalar nada para gerar os pacotes — o GitHub builda sozinho:

1. Vá na aba **[Actions](../../actions)** → workflow **"Build do jogo (Windows / Linux / Mac)"** → botão **Run workflow**.
2. Ao terminar (~5 min), abra a execução e baixe o pacote em **Artifacts** (zips para Windows, Linux e Mac).
3. Para versões oficiais: criar uma tag `v0.x` gera os builds e anexa numa **[Release](../../releases)** automaticamente.

**Android (APK):** workflow **"Build Android (APK)"** na mesma aba Actions (as chaves de assinatura já estão como secrets do repositório). Também dá para buildar manualmente pelo launcher do Ren'Py.

A cada Pull Request, um verificador automático roda o **lint do Ren'Py** e acusa erros de script antes da revisão.

## Como o grupo trabalha aqui

- **[Issues](../../issues)** — toda tarefa, bug ou decisão vira uma issue. Use os modelos prontos (botão *New issue*); as etiquetas indicam a frente (conteúdo, arte, código, docs) e os *milestones* marcam a semana do cronograma.
- **[Quadro do projeto](https://github.com/orgs/pet-saude-poprua/projects/1)** — visão geral do que está *A fazer / Em andamento / Concluído*, atualizada pelas issues.
- **Pull Requests** — mudanças no jogo entram por PR, com pelo menos 1 revisão. Um verificador automático (lint do Ren'Py) roda em cada PR.
- **Reuniões** — quartas-feiras; atas no Livro de Atas do grupo.

## Referências do projeto

- Roteiro da História 1: `ROTEIRO-VISUAL-NOVEL.docx` (Dia 1 — "Ele não parece morador de rua")
- Base pedagógica: `REFLEXOES-JOGO.docx` (4 casos: Renato, Cleide, Seu Zé, Andressa)
- Fontes citadas no jogo: MDHC (Diagnóstico Federal 2023) · Portaria GM/MS 940/2011 · PNAB 2017 · Decreto 7053/2009 · PNH/HumanizaSUS

## Licenças de terceiros

- Fontes **Atkinson Hyperlegible** e **Kaushan Script** — [SIL Open Font License](game/fonts/OFL.txt)
- Motor **Ren'Py** — licença própria (MIT/LGPL, ver site)
