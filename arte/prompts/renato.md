# Prompts de arte — Renato

Gerado por `scripts/arte.py prompts --historia renato` a partir de `arte/pedidos/renato.json`. Não edite à mão: mude o JSON e gere de novo.

## senhora_model_sheet (#137)

**Cena:** Cena 1 — sala de espera (a senhora da primeira fileira)  
**Tipo:** model_sheet — Folha de referência de personagem novo (não entra no jogo); vem antes de sprites e cenas. Formato: 3:2 (paisagem).  
**Destino:** pasta Personagens do Drive (referência dos próximos pedidos; não entra no jogo)
**Parte de:** #114

**O que é:** Model sheet da senhora da primeira fileira, a paciente que se incomoda com a presença de Renato na sala de espera. Hoje ela só existe como sprite antigo. Precisa ser verossímil e humana (incômodo, não vilania).

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- https://drive.google.com/file/d/1gDNrDULU8bUiVmdcg90na1qN5kzox8t-/view (model sheet do Renato: só layout e traço)
- https://drive.google.com/file/d/1jOE3WdKmWc9WL5nwVAeYgFMakFz5gSD6/view (model sheet da recepcionista: só layout e traço)
- game/images/chars/senhora.webp (ideia atual da personagem; não precisa copiar)

### 3. Cole o prompt
```text
Model sheet of a supporting character for a Brazilian public health educational visual novel: an older woman waiting in the emergency unit waiting room who feels uncomfortable sitting near a man in homelessness; she is an ordinary, believable person, not a villain; poses: sitting with her purse on her lap, arms crossed looking sideways, whispering to someone, standing with the purse, looking away embarrassed, softening her expression. Character: a Brazilian woman in her early 60s, fuller plus-size body, light-brown skin, gray-streaked hair in a low bun, simple floral yellow blouse and long brown skirt, flat brown shoes, a small brown purse; an ordinary, well-kept retiree. character model sheet / reference sheet on a clean off-white paper background, same layout and same art style as the attached model sheets: on the left a full-body turnaround of the same character (front, three-quarter, side profile, back), on the upper right a grid of 12 to 15 facial expression headshots (neutral, attentive, worried, tired, sad, hopeful, relieved, grateful, thoughtful, firm, slight smile, embarrassed), along the bottom a row of 6 full-body gesture poses that fit the character's role, a small color palette swatch strip and three close-up detail boxes (face, clothing detail, key accessory); clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, the character identical in every view, short section titles allowed but no other text, dignified and respectful portrayal, 3:2 landscape. Use the attached model sheets only as layout and style reference, not for the character's appearance. Avoid: different faces between views, inconsistent clothing, extra characters, background scenery, photorealistic, hyperrealistic, caricature, exaggerated dirt, extra fingers, deformed hands, watermark, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Mesmo layout e mesmo traço das model sheets atuais (vistas, expressões, poses, paleta, detalhes).
- [ ] O personagem é o mesmo em todas as vistas e expressões (rosto, cabelo, roupa, cores).
- [ ] Roupa, idade e acessórios batem com o roteiro; crachá só em quem trabalha na UPA ou na rede.
- [ ] Retrato digno: sem caricatura nem sujeira exagerada.
- [ ] Antes de valer: aprovação da autora da história e da Saúde (comentem na issue).

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

### 6. Depois da aprovação
A autora da história e a Saúde aprovam aqui na issue. Aprovada, a model sheet vai para a pasta Personagens do Drive e passa a ser a referência de todos os sprites e cenas desse personagem.

## aqua_classificacao (#123)

**Cena:** Cena 2 — Classificação de risco  
**Tipo:** cenario — Fundo de cena (sem pessoas). Formato: 16:9 (paisagem).  
**No jogo:** `bg aqua_classificacao` → `game/images/bg/aqua_classificacao.webp`
**Parte de:** #112

**O que é:** Sala de classificação de risco da UPA: pequena, porta fechada, mesa com computador, aparelho de pressão, oxímetro, termômetro, glicosímetro, cadeira do paciente. Hoje o jogo usa o consultório como provisório.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/bg/aqua_consultorio.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_consultorio.jpg)
- [game/images/bg/aqua_recepcao.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_recepcao.jpg)

### 3. Cole o prompt
```text
Interior of a small risk-classification (triage) room in a Brazilian public emergency unit (UPA 24h): a simple desk with a computer monitor turned slightly away, a digital blood pressure monitor, a pulse oximeter and a thermometer on the desk, a small glucometer case, a patient chair facing the desk, a closed door, a wall shelf with color-coded triage wristbands as small soft shapes (red, orange, yellow, green, blue), soft fluorescent ceiling light, warm muted institutional palette. digital watercolor illustration, soft loose washes, muted faded pastel palette, simplified almost cartoonish shapes, minimal fine detail, gentle soft edges, light paper texture, slightly desaturated, calm subdued mood, soft background blur, mobile visual novel background, clean uncluttered composition, eye-level view, no text, no letters, no logos, empty center and lower foreground reserved for characters, no people, no characters, 16:9 landscape. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Formato paisagem 16:9.
- [ ] Sem pessoas.
- [ ] Centro e parte de baixo livres para o personagem.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## aqua_observacao (#124)

**Cena:** Cena 5 — Sala de observação  
**Tipo:** cenario — Fundo de cena (sem pessoas). Formato: 16:9 (paisagem).  
**No jogo:** `bg aqua_observacao` → `game/images/bg/aqua_observacao.webp`
**Parte de:** #112

**O que é:** Sala de observação com oito poltronas reclináveis e quatro macas, um posto de enfermagem num canto, suportes de soro, um cilindro de oxigênio. Cheia, mas sem pessoas desenhadas (os pacientes entram como sugestão de volume).

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/bg/aqua_box.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_box.jpg)
- [game/images/bg/aqua_corredor.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_corredor.jpg)

### 3. Cole o prompt
```text
Interior of an observation room in a Brazilian public emergency unit: a row of blue reclining patient armchairs along one wall, four hospital stretchers separated by light curtains on the other side, IV drip stands, a wall oxygen outlet and a small oxygen cylinder, a nursing station desk in a corner with a computer and paperwork, soft clinical lighting, muted teal and white palette, busy but calm, the armchairs and stretchers empty. digital watercolor illustration, soft loose washes, muted faded pastel palette, simplified almost cartoonish shapes, minimal fine detail, gentle soft edges, light paper texture, slightly desaturated, calm subdued mood, soft background blur, mobile visual novel background, clean uncluttered composition, eye-level view, no text, no letters, no logos, empty center and lower foreground reserved for characters, no people, no characters, 16:9 landscape. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Formato paisagem 16:9.
- [ ] Sem pessoas.
- [ ] Centro e parte de baixo livres para o personagem.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## aqua_servico_social (#125)

**Cena:** Cena 7 — Serviço Social  
**Tipo:** cenario — Fundo de cena (sem pessoas). Formato: 16:9 (paisagem).  
**No jogo:** `bg aqua_servico_social` → `game/images/bg/aqua_servico_social.webp`
**Parte de:** #112

**O que é:** Sala do Serviço Social: pequena, uma mesa, duas cadeiras, o celular do serviço sobre a mesa, um mural com a lista de contatos da rede (números riscados e reescritos, sem texto legível).

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/bg/aqua_consultorio.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_consultorio.jpg)
- [game/images/bg/aqua_recepcao.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_recepcao.jpg)

### 3. Cole o prompt
```text
Interior of a small social work office inside a Brazilian public emergency unit: one simple desk with two chairs facing each other, a basic smartphone lying on the desk next to a folder and a pen, a cork board on the wall with a handwritten contact list and pinned notes rendered as illegible scribbles with some lines crossed out, a small window with soft afternoon light, a filing cabinet, a potted plant, warm muted earthy palette, intimate and quiet. digital watercolor illustration, soft loose washes, muted faded pastel palette, simplified almost cartoonish shapes, minimal fine detail, gentle soft edges, light paper texture, slightly desaturated, calm subdued mood, soft background blur, mobile visual novel background, clean uncluttered composition, eye-level view, no text, no letters, no logos, empty center and lower foreground reserved for characters, no people, no characters, 16:9 landscape. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Formato paisagem 16:9.
- [ ] Sem pessoas.
- [ ] Centro e parte de baixo livres para o personagem.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## colega_enfermagem (#126)

**Cena:** Cena 5 — Sala de observação (a colega no posto)  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image colega_enfermagem` → `game/images/chars/colega_enfermagem.webp`
**Parte de:** #114

**O que é:** Sprite de corpo inteiro da colega da enfermagem (Lívia), de pé, olhando para o lado, em conversa.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Lívia Souza, técnica de enfermagem (a colega da Cena 5): https://drive.google.com/file/d/12H-TEYWnKjrgXOhcxwhgS_JREBYudS7j/view
- [game/images/chars/assistente_social.webp](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/chars/assistente_social.webp)

### 3. Cole o prompt
```text
Full body standing pose, body turned three-quarters to the viewer's left as if talking to a colleague, one hand resting on a clipboard held against the chest, neutral curious expression with a slight raised eyebrow. Character: Livia, a Brazilian woman aged 41, warm tan skin, curly dark-brown hair gathered in a loose high bun with a few curls falling around the face, welcoming face; wears dark teal-green nursing scrubs (V-neck top with a chest pocket and matching trousers), white sneakers, a black wristwatch, an ID badge on a retractable clip; sometimes holds a clipboard. Keep this character identical to the attached model sheet (face, hair, body, clothes, colors, badge). clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## obj_pulseira_amarela (#127)

**Cena:** Cena 2 — Classificação de risco (pulseira amarela)  
**Tipo:** objeto — Objeto em destaque (caderno, receita, pulseira...). Formato: 1:1 (quadrado), fundo transparente.  
**No jogo:** `image pulseira_amarela` → `game/images/obj/obj_pulseira_amarela.webp`
**Parte de:** #113

**O que é:** Pulseira hospitalar de identificação, amarela (classificação de risco).

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/obj/caderno_renato.webp](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/obj/caderno_renato.webp)

### 3. Cole o prompt
```text
A plastic hospital identification wristband in yellow, the kind used for emergency triage, closed in a loop and lying at a slight angle, a small white label area with illegible soft gray lines. digital watercolor illustration, single object study, soft loose washes, muted faded pastel palette, simplified but clearly readable shapes, gentle soft edges, light paper texture, slightly desaturated, calm mood, centered close-up prop, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), mobile game item art, clean and uncluttered, no people, no hands, no readable text, no letters, no numbers, 1:1 square. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Quadrado, objeto centralizado.
- [ ] Fundo transparente (PNG) ou magenta puro (#FF00FF), sem sombra.
- [ ] Sem mãos nem pessoas.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## obj_pulseira_laranja (#128)

**Cena:** Cena 2 — Classificação de risco (pulseira laranja)  
**Tipo:** objeto — Objeto em destaque (caderno, receita, pulseira...). Formato: 1:1 (quadrado), fundo transparente.  
**No jogo:** `image pulseira_laranja` → `game/images/obj/obj_pulseira_laranja.webp`
**Parte de:** #113

**O que é:** A mesma pulseira, laranja. Gerar depois da amarela, pedindo “a mesma pulseira, só que laranja”.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- a pulseira amarela aprovada (imagem entregue no pedido obj_pulseira_amarela)

### 3. Cole o prompt
```text
The same plastic hospital identification wristband as the reference, now in orange, same angle and lighting. digital watercolor illustration, single object study, soft loose washes, muted faded pastel palette, simplified but clearly readable shapes, gentle soft edges, light paper texture, slightly desaturated, calm mood, centered close-up prop, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), mobile game item art, clean and uncluttered, no people, no hands, no readable text, no letters, no numbers, 1:1 square. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Quadrado, objeto centralizado.
- [ ] Fundo transparente (PNG) ou magenta puro (#FF00FF), sem sombra.
- [ ] Sem mãos nem pessoas.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## obj_encaminhamento (#129)

**Cena:** Cena 7 — Serviço Social (encaminhamento escrito)  
**Tipo:** objeto — Objeto em destaque (caderno, receita, pulseira...). Formato: 1:1 (quadrado), fundo transparente.  
**No jogo:** `image encaminhamento` → `game/images/obj/obj_encaminhamento.webp`
**Parte de:** #113

**O que é:** Folha de encaminhamento que a assistente social entrega a Renato, dobrada uma vez, com carimbo e assinatura ilegíveis.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/obj/obj_receita_medica.webp](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/obj/obj_receita_medica.webp)

### 3. Cole o prompt
```text
A single sheet of white paper referral form folded once, with a soft blue institutional header shape, handwritten illegible blue-ink lines, a faint round stamp and a signature scribble, a corner slightly bent. digital watercolor illustration, single object study, soft loose washes, muted faded pastel palette, simplified but clearly readable shapes, gentle soft edges, light paper texture, slightly desaturated, calm mood, centered close-up prop, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), mobile game item art, clean and uncluttered, no people, no hands, no readable text, no letters, no numbers, 1:1 square. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Quadrado, objeto centralizado.
- [ ] Fundo transparente (PNG) ou magenta puro (#FF00FF), sem sombra.
- [ ] Sem mãos nem pessoas.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## ovl_prontuario (#130)

**Cena:** Cenas 1, 4 e 6 — tela do prontuário eletrônico  
**Tipo:** overlay — Tela ou papel que aparece por cima da cena (prontuário, celular, documento). Exceção: não é aquarela. Formato: 16:9 (paisagem).  
**No jogo:** `image esus` → `game/images/bg/ovl_prontuario.webp`
**Parte de:** #113

**O que é:** Tela do prontuário eletrônico que aparece por cima da cena (substitui a atual aqua_esus.jpg). Campos e textos como blocos, sem letras.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- [game/images/bg/aqua_esus.jpg](https://github.com/pet-saude-poprua/pet-saude-poprua/blob/master/game/images/bg/aqua_esus.jpg)

### 3. Cole o prompt
```text
A flat electronic patient record screen in the style of the Brazilian e-SUS system shown on a computer monitor frame: a header bar, a left sidebar with menu blocks, form panels with labeled fields drawn as gray placeholder bars, a vital signs panel with small chart shapes, a large free-text notes area, soft blue and white UI. flat minimal interface or document illustration, clean flat design, soft blue, white and gray palette, simple rounded panels, placeholder blocks and soft lines instead of readable text, no photo, no watercolor, no people, centered, 16:9 landscape. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Formato paisagem 16:9.
- [ ] Visual limpo de interface/documento (não é aquarela).

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## renato_normal (#131)

**Cena:** Cenas 1 e 3 — sala de espera  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image renato normal` → `game/images/chars/renato_normal.webp`
**Parte de:** #114

**O que é:** Renato sentado numa cadeira de madeira, cabeça baixa, lendo o caderno aberto nas mãos. Refaz o sprite antigo conforme a model sheet; manter a pose.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Renato: https://drive.google.com/file/d/1gDNrDULU8bUiVmdcg90na1qN5kzox8t-/view
- game/images/chars/renato_normal.webp (só a pose; roupa e rosto da model sheet)

### 3. Cole o prompt
```text
Full body, seated on a simple wooden chair, slightly hunched forward, head lowered, reading the open notebook held in both hands, quiet tired expression; include the wooden chair. Character: Renato, a Brazilian man aged 54, lean build, warm tan weathered skin, messy wavy dark hair with gray streaks at the temples, short salt-and-pepper stubble beard, tired but gentle dark eyes, forehead lines; wears a dark charcoal-brown canvas zip jacket (worn, slightly faded) open over a beige button-up shirt, faded medium-blue jeans, old dark-brown leather work boots; his clothes are simple and clean but worn; often holds an old dark spiral notebook with a small taped paper label (no readable text). Keep this character identical to the attached model sheet (face, hair, body, clothes, colors) and do not add an ID badge or lanyard. clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## renato_hesitante (#132)

**Cena:** Cenas 2, 4 e 5 — em pé, inseguro  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image renato hesitante` → `game/images/chars/renato_hesitante.webp`
**Parte de:** #114

**O que é:** Renato em pé, inseguro: uma mão no queixo, a outra segurando o caderno contra o peito. Refaz o sprite antigo conforme a model sheet; manter a pose.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Renato: https://drive.google.com/file/d/1gDNrDULU8bUiVmdcg90na1qN5kzox8t-/view
- game/images/chars/renato_hesitante.webp (só a pose; roupa e rosto da model sheet)

### 3. Cole o prompt
```text
Full body standing, weight on one leg, one hand raised to his chin, the other holding the notebook against his chest, hesitant worried expression, looking slightly to the side. Character: Renato, a Brazilian man aged 54, lean build, warm tan weathered skin, messy wavy dark hair with gray streaks at the temples, short salt-and-pepper stubble beard, tired but gentle dark eyes, forehead lines; wears a dark charcoal-brown canvas zip jacket (worn, slightly faded) open over a beige button-up shirt, faded medium-blue jeans, old dark-brown leather work boots; his clothes are simple and clean but worn; often holds an old dark spiral notebook with a small taped paper label (no readable text). Keep this character identical to the attached model sheet (face, hair, body, clothes, colors) and do not add an ID badge or lanyard. clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## renato_aberto (#133)

**Cena:** Cenas 4 e 6 — conversa que se abre  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image renato aberto` → `game/images/chars/renato_aberto.webp`
**Parte de:** #114

**O que é:** Renato sentado, mãos nos joelhos, caderno aberto no colo, olhando para quem fala, expressão mais aberta. Refaz o sprite antigo conforme a model sheet; manter a pose.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Renato: https://drive.google.com/file/d/1gDNrDULU8bUiVmdcg90na1qN5kzox8t-/view
- game/images/chars/renato_aberto.webp (só a pose; roupa e rosto da model sheet)

### 3. Cole o prompt
```text
Full body, seated on a simple wooden chair, hands resting on his knees, the notebook open on his lap, looking at the viewer with a gentle, more open and trusting expression, faint hopeful smile; include the wooden chair. Character: Renato, a Brazilian man aged 54, lean build, warm tan weathered skin, messy wavy dark hair with gray streaks at the temples, short salt-and-pepper stubble beard, tired but gentle dark eyes, forehead lines; wears a dark charcoal-brown canvas zip jacket (worn, slightly faded) open over a beige button-up shirt, faded medium-blue jeans, old dark-brown leather work boots; his clothes are simple and clean but worn; often holds an old dark spiral notebook with a small taped paper label (no readable text). Keep this character identical to the attached model sheet (face, hair, body, clothes, colors) and do not add an ID badge or lanyard. clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## renato_despedida (#134)

**Cena:** Desfecho — saída da UPA  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image renato despedida` → `game/images/chars/renato_despedida.webp`
**Parte de:** #114

**O que é:** Renato de pé, virado de três quartos, olhando para trás por cima do ombro, mochila num ombro e caderno na mão. Refaz o sprite antigo conforme a model sheet; manter a pose.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Renato: https://drive.google.com/file/d/1gDNrDULU8bUiVmdcg90na1qN5kzox8t-/view
- game/images/chars/renato_despedida.webp (só a pose; roupa e rosto da model sheet)

### 3. Cole o prompt
```text
Full body standing, body turned three-quarters away toward the exit, looking back over his shoulder at the viewer with a soft grateful half-smile, a worn olive canvas backpack on one shoulder, the notebook held in one hand. Character: Renato, a Brazilian man aged 54, lean build, warm tan weathered skin, messy wavy dark hair with gray streaks at the temples, short salt-and-pepper stubble beard, tired but gentle dark eyes, forehead lines; wears a dark charcoal-brown canvas zip jacket (worn, slightly faded) open over a beige button-up shirt, faded medium-blue jeans, old dark-brown leather work boots; his clothes are simple and clean but worn; often holds an old dark spiral notebook with a small taped paper label (no readable text). Keep this character identical to the attached model sheet (face, hair, body, clothes, colors) and do not add an ID badge or lanyard. clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.

## assistente_social (#135)

**Cena:** Cena 7 — Serviço Social  
**Tipo:** sprite — Personagem recortado, corpo inteiro, para aparecer por cima do cenário. Formato: 2:3 (retrato), fundo transparente.  
**No jogo:** `image assistente` → `game/images/chars/assistente_social.webp`
**Parte de:** #114

**O que é:** Camila em pé, segurando pastas, expressão neutra e atenta. Refaz o sprite antigo conforme a model sheet.

### 1. Abra o assistente de arte
Use a habilidade “arte-alem-da-rua” do Gemini ([baixe o .zip](https://drive.google.com/file/d/1r6c075KdQesls-z04F6hRNIn2gkR1AnD/view) e envie em Habilidades → Criar → Enviar) ou seu Projeto no ChatGPT. Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.

### 2. Anexe as referências
- Model sheet de Camila Ferreira, assistente social da UPA: https://drive.google.com/file/d/1HALke0Qm9M-Y8eA84WGSH89Zrqjd23jR/view
- game/images/chars/assistente_social.webp (só a pose; roupa e rosto da model sheet)

### 3. Cole o prompt
```text
Full body standing, facing three-quarters toward the viewer, holding beige paper folders and a kraft notebook against her side with one arm, neutral attentive expression, relaxed posture. Character: Camila, a Brazilian woman aged 38, light-tan skin, shoulder-length curly dark-brown hair worn loose, round dark-rimmed glasses, attentive kind expression; wears an olive-green button-up overshirt with sleeves rolled to the forearm over a beige blouse, beige-khaki straight trousers with a brown belt, brown loafers, a wristwatch, an ID badge on a navy lanyard; often holds a kraft-brown spiral notebook or beige paper folders. Keep this character identical to the attached model sheet (face, hair, body, clothes, colors, badge). clean semi-realistic comic illustration style, soft cel shading, natural proportions, warm approachable rendering, full body standing character for a visual novel sprite, facing slightly toward viewer, isolated character cutout, transparent background (if transparency is not possible: flat solid pure magenta #FF00FF background, no gradient, no shadow), no environment, no floor, no cast shadow, no wall, no text, no watermark, consistent with a Brazilian public health (SUS) educational game cast, 2:3 portrait. Use the attached images as style reference. Avoid: people in the background, crowd, text, letters, numbers, logos, readable signage, watermark, UI icons, photorealistic, hyperrealistic, heavy detail, cluttered composition, oversaturated, high contrast, harsh dramatic lighting, lens flare, distorted perspective, warped lines, extra fingers, deformed hands, caricature, low quality, jpeg artifacts.
```

### 4. Confira antes de entregar
- [ ] Parece da mesma família das referências (traço, paleta, luz).
- [ ] Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).
- [ ] Nada que contrarie o roteiro (lugar, objetos, horário).
- [ ] Corpo inteiro, retrato (vertical).
- [ ] Fundo transparente (PNG) ou, se a ferramenta não conseguir, magenta puro (#FF00FF) liso e sem sombra. Branco não serve.
- [ ] Igual à model sheet (rosto, cabelo, roupa, cores e acessórios; crachá só em quem trabalha na UPA ou na rede).
- [ ] Mãos e rosto sem deformação.

### 5. Entregue
Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última imagem. Depois mova o card para **Em revisão**.
