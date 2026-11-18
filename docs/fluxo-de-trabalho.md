# Fluxo de trabalho no GitHub

Organização por tarefas, sem equipes fixas (ata de 11/11/2026). Todos podem contribuir com código, arte e roteiro; a coordenação técnica é do Breno.

## Tarefas

- Toda tarefa vira uma **issue**, usando os modelos (botão *New issue*).
- Etiquetas de frente: `frente:código`, `frente:arte`, `frente:conteúdo`, `frente:ux`, `frente:docs`, `frente:áudio`.
- Dúvidas para a equipe de saúde: etiqueta `tipo:dúvida`; a pergunta vai pelo WhatsApp da TI.
- Quem ainda não tem conta no GitHub aparece no campo "Responsável" do quadro pelo nome.

## Mudanças no jogo

1. Crie uma branch a partir de `master` (`feat/…`, `fix/…`, `docs/…`).
2. Abra um Pull Request citando a issue (`Closes #N`) ou com a etiqueta `sem-issue`.
3. O CI roda o lint do Ren'Py e a conferência das tabelas de decisões (`scripts/simular_historia.py`).
4. Pelo menos uma revisão antes do merge. Nada vai direto para `master`.

## Builds

- Tag `v0.x` gera os pacotes de Windows, Linux e Mac numa Release.
- O APK sai do workflow "Build Android (APK)".
