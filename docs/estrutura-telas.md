# Estrutura de Menus e Telas — Proposta v1

**Projeto:** Visual novel educacional PET-Saúde Pop Rua (GT6) · **Versão:** 1.0 — 14/07/2026
**Base:** protótipo inicial da tela de menu (quadro "Caminhos do cuidado") usado como **referência de conteúdo**, não como versão final. Esta proposta reorganiza a estrutura para o formato **paisagem 16:9** — o formato de todos os cenários aquarela aprovados na reunião de 01/07 — e integra o estilo visual aquarelado também aos menus.

---

## Direção visual dos menus

- **Fundo:** ilustração aquarela da UPA ao entardecer com profissionais acolhendo pessoas em situação de rua (nova arte gerada nesta entrega, `assets-gerados/menu_upa_entardecer.png`) — mantém o conceito do protótipo inicial, executado no padrão aquarela aprovado.
- **Paleta da interface** (harmonizada da proposta azul forte / azul claro / verde com os tons aquarela):
  - Azul escuro `#1D3D5C` — botões primários e títulos
  - Azul médio `#3E7CB1` — hover/realce
  - Verde suave `#5E8C61` — confirmações e progresso
  - Branco gelo `#F4F1EA` — painéis translúcidos sobre o fundo aquarela
  - Cinza escuro `#33393F` — textos
- **Composição:** os cenários aquarela têm o terço esquerdo mais calmo — os menus ocupam um painel translúcido à esquerda, deixando a ilustração respirar à direita.
- Tipografia: Lato (já no projeto), corpo ≥ 28px em 1280x720 (legibilidade em celular).

## Mapa de telas

### 1. Abertura (splash)
Logos UFPB · PET-Saúde · GT6 Pop Rua sobre fundo neutro aquarela (N7), ~2s, pula com toque.

### 2. Menu principal
| Elemento | Conteúdo | Status |
|---|---|---|
| Título | "Além da Rua" (nome definido; antes, "Caminhos do Cuidado") + tagline "Um jogo sobre acolhimento, direito e empatia" | nome final em aberto (ata) |
| Botão **Jogar** | vai a Capítulos (se há jogo salvo, oferece "Continuar") | definido |
| Botão **Perfil / Progresso** | tela 4 | definido |
| Botões **Materiais · Redes de apoio · Sobre o jogo · Créditos** | telas 5–8 | conteúdo provisório |
| Ícone **Configurações** (canto) | tela 9 | definido |
| Rodapé | brasões UFPB · PET-Saúde · GT-6 POP RUA | definido |

### 3. Capítulos
Cards horizontais, um por história: **História 1 — "Ele não parece morador de rua"** (jogável) + Histórias 2–4 bloqueadas (silhuetas aquarela + cadeado). Cada card mostra estado: não iniciada / em andamento / concluída (com desfecho A/B). Primeira entrada na História 1 passa antes pela **tela conceitual sobre PSR** (dados de contexto, 1 tela, botão "Começar").

### 4. Perfil / Progresso *(pedido da ata: persistência + progresso)*
- Histórias concluídas × pendentes (4 slots).
- Resultado da última jogada de cada história: desfecho (A/B), 4 medidores, nós de rede acesos (7 da história 1).
- Persistente entre sessões (Ren'Py `persistent`).

### 5. Materiais
Lista de conteúdos educativos curtos (releitura da tela conceitual PSR, dados MDHC 2023, Portaria 940/2011, PNH/HumanizaSUS). Conteúdo provisório: estrutura pronta, textos a validar com o grupo.

### 6. Redes de apoio
Cards dos serviços: UPA · UBS · Consultório na Rua · CRAS · CAPS · Serviço Social · Defensoria Pública — o que é, quando acionar, como se conectam (mesma iconografia dos nós de rede do jogo). Conteúdo provisório.

### 7. Sobre o jogo
Proposta, objetivos educacionais, funcionamento das missões e medidores, instituições responsáveis (UFPB, PET-Saúde, GT6).

### 8. Créditos
Equipe do GT por frente (coordenação, conteúdo, TI), tutoria, apoios.

### 9. Configurações
Volume música/efeitos · tamanho do texto (acessibilidade) · velocidade do texto · apagar progresso (com confirmação).

### 10. Telas da história (in-game)
| Tela | Descrição |
|---|---|
| **Cena de diálogo** | BG aquarela + sprite do personagem + caixa de diálogo inferior translúcida com faixa colorida por personagem. HUD de Empatia opcional (o roteiro atualizado esconde todos os medidores até o epílogo — implementado como interruptor `hud_empatia`, padrão desligado; decidir com o grupo) |
| **Tela de decisão** | pergunta + 3 opções (A/B/C) em botões grandes; sem indicação de "resposta certa" |
| **Overlay e-SUS** | mock da interface de registro (cenas 2 e 3) |
| **Mapa de nós** | overlay com os 7 serviços; nós acendem ao serem acionados |
| **Card de reflexão** | fim de cada cena: fundo neutro aquarela + texto curto |
| **Card de contexto real** | antes do epílogo: dados reais com fontes |
| **Epílogo / Pontuação** | revela os 4 medidores + mapa final + desfecho A ou B |

## Diferenças em relação ao protótipo inicial (para discussão em 15/07)

1. **Paisagem 16:9** em vez de retrato — aproveita 100% dos cenários aquarela aprovados e funciona igual em celular (jogo segurado de lado), tablet e computador; o Ren'Py exporta Android nativamente assim.
2. **Menus integrados ao estilo aquarela** (painel translúcido sobre ilustração) em vez de interface chapada — reforça a identidade aprovada.
3. **"Pontuação" não é item do menu**: vive no epílogo e no Perfil/Progresso, para não revelar os medidores ocultos durante o jogo (mecânica pedagógica do roteiro).
4. **Tela conceitual sobre PSR** posicionada na entrada da 1ª história (e relida em Materiais).
5. Mantidos do protótipo inicial: itens do menu (Perfil, Materiais, Redes de apoio, Sobre), tagline, rodapé institucional e a paleta fria como base da interface.
