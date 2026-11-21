# Teste automático do jogo

`zz_teste_automatico.rpy` joga o Renato sozinho, usando o framework de testes do Ren'Py 8.5 (comando `test`). Percorre sete caminhos (canônico; Desfecho C com "Retomar"; Desfecho B pela Decisão 7 com "Retomar"; vários desvios; desencontro recuperado; Desfecho C sem orientação; atalho da Cena 7), mais o menu principal, Casos, Materiais e Redes de apoio. Para cada caminho grava:

- `tests/<caminho>.txt`: a transcrição do que o jogo mostrou (falas, opções escolhidas, RESULTADOS, reflexões, caderno, barras e nós do mapa);
- `tests/screenshots/<caminho>/`: capturas das telas.

O arquivo **não** fica em `game/`, para não entrar nos pacotes do jogo.

## Como rodar (Linux)

1. Baixe o pacote `petsaude-pop-rua-<versão>-linux.tar.bz2` do artefato `builds-alem-da-rua` (aba Actions) e extraia numa pasta de trabalho.
2. Copie este arquivo para a pasta `game/` do pacote extraído.
3. Na pasta do pacote:

```bash
mkdir -p ../saves
SDL_AUDIODRIVER=dummy ./petsaude-pop-rua.sh "$PWD" --savedir "$PWD/../saves" test global
```

- A janela do jogo abre e joga sozinha (cerca de 16 minutos para a suíte inteira). Não feche: o último teste (`zz_sair`) encerra o jogo.
- Para um teste só: `test global::p1_canonica`. Nesse caso o jogo não fecha sozinho no fim; encerre a janela.
- O Ren'Py ignora o sinal de término comum; se usar `timeout`, use `timeout -s KILL`.
- O jogo não roda sem janela neste build (`SDL_VIDEODRIVER=offscreen` não é suportado).

## Como ler o resultado

- O resumo `[rpytest] Status: PASSED` indica que nenhum caminho travou nem deu erro.
- `!!` na transcrição marca um problema do teste (tela não reconhecida ou escolhas a menos).
- As barras do `[PAINEL]` devem bater com a regra do Apêndice D da v4 (Quadro D2, com exemplos calculados).

Para testar outro caminho, acrescente um `testcase` com a sequência de letras na ordem em que os menus aparecem (os menus de "Retomar/Encerrar o dia" também contam).
