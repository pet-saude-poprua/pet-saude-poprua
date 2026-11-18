# Além da Rua

Serious game em formato de visual novel sobre o cuidado à **população em situação de rua (PSR)**, desenvolvido pelo **PET-Saúde Digital · GT06 População em Situação de Rua · UFPB**, Frente TI.

O jogo terá cinco histórias. Em cada uma, o jogador acompanha o atendimento pelo olhar de diferentes profissionais (recepção, enfermagem, medicina, serviço social) e escolhe condutas em momentos de decisão. As escolhas movem quatro dimensões do cuidado (**Direito em Saúde, Conhecimento da Rede, Empatia e Acolhimento**), reveladas só no fim de cada dia, junto com o mapa da rede. O jogo não avalia certo ou errado: as escolhas abrem reflexões.

## Como rodar o jogo

1. Baixe o [Ren'Py SDK 8.5.3](https://www.renpy.org/latest.html) e extraia em qualquer pasta.
2. Abra o `renpy.exe` (launcher), clique em **preferences → projects directory** e aponte para a pasta que contém este repositório.
3. Selecione o projeto e clique em **Launch Project**.

## Estrutura do repositório

| Pasta | O que tem |
|---|---|
| `game/nucleo/` | Peças comuns às cinco histórias: decisões, medidores, mapa da rede, telas, personagens, início |
| `game/historias/<nome>/` | Uma pasta por história (dados, cenas, epílogo) |
| `game/` (raiz) | Interface: `gui.rpy`, `screens.rpy`, `telas_menu.rpy`, `options.rpy` |
| `scripts/` | `simular_historia.py` (confere as decisões no CI) e `gerar_imagens.py` |
| [`docs/`](docs/) | Cronograma, fluxo de trabalho, guia do roteiro ao código, histórias, telas e padrões visuais |
| `assets-gerados/` | Imagens geradas por IA (com os prompts em `PROMPTS-GERADOS.md`) |

## Documentação

| Documento | O que tem |
|---|---|
| [`docs/CRONOGRAMA.md`](docs/CRONOGRAMA.md) | Cronograma até ago/2027 e estado das cinco histórias |
| [`docs/fluxo-de-trabalho.md`](docs/fluxo-de-trabalho.md) | Issues, etiquetas, branches, PRs e builds |
| [`docs/guia-roteiro-para-codigo.md`](docs/guia-roteiro-para-codigo.md) | Como transformar um roteiro em cenas usando o núcleo |
| [`docs/historias/`](docs/historias/) | Documento de acompanhamento de cada história (dimensões, caso inspirador) e inventários |
| [`docs/estrutura-telas.md`](docs/estrutura-telas.md) | Estrutura de menus e telas |
| [`docs/fluxograma-navegacao.md`](docs/fluxograma-navegacao.md) | Fluxograma de navegação (Mermaid) |
| [`docs/padroes-visuais.md`](docs/padroes-visuais.md) | Padrões visuais: estilo aquarela, personagens, geração de imagens |

## Baixar o jogo pronto (builds)

Não precisa instalar nada para gerar os pacotes — o GitHub builda sozinho:

1. Vá na aba **[Actions](../../actions)** → workflow **"Build do jogo (Windows / Linux / Mac)"** → botão **Run workflow**.
2. Ao terminar (~5 min), abra a execução e baixe o pacote em **Artifacts** (zips para Windows, Linux e Mac).
3. Para versões oficiais: criar uma tag `v0.x` gera os builds e anexa numa **[Release](../../releases)** automaticamente.

**Android (APK):** workflow **"Build Android (APK)"** na mesma aba Actions (as chaves de assinatura já estão como secrets do repositório). Também dá para buildar manualmente pelo launcher do Ren'Py.

A cada Pull Request, um verificador automático roda o **lint do Ren'Py** e acusa erros de script antes da revisão.

## Como o grupo trabalha aqui

Ver [`docs/fluxo-de-trabalho.md`](docs/fluxo-de-trabalho.md). Em resumo: toda tarefa é uma issue; mudanças entram por Pull Request com revisão; o CI roda o lint do Ren'Py e a conferência das decisões. Quadro do projeto: [Projects](https://github.com/orgs/pet-saude-poprua/projects/1).

## Referências do projeto

- Roteiros: pasta "Frente TI - GT06" no Google Drive (Renato v4, revisão de 19/11/2026; Cleide v1.0).
- Atas: Livro de ATAS da Frente TI e Classroom da turma.
- Fontes citadas no jogo: ver o card "Contexto real" de cada história.

## Licenças de terceiros

- Fontes **Atkinson Hyperlegible** e **Kaushan Script** — [SIL Open Font License](game/fonts/OFL.txt)
- Motor **Ren'Py** — licença própria (MIT/LGPL, ver site)
