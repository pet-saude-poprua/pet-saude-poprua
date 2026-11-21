"""Confere a tabela de decisões de uma história e simula todos os caminhos.

Lê o bloco entre "## BEGIN DECISOES_<NOME>" e "## END DECISOES_<NOME>" em
game/historias/<nome>/dados.rpy (a mesma tabela que o jogo usa) e verifica:

- cada decisão tem 2 ou 3 opções, cada opção tem 4 efeitos inteiros e uma
  lista de flags;
- a linha canônica (opções ★) é o máximo em todas as dimensões, de modo que
  ela dá 100 nas quatro barras do epílogo;
- (Renato) conta os caminhos distintos e quantos terminam em cada desfecho
  (os números do Apêndice D do roteiro).

Uso: python3 scripts/simular_historia.py renato
Sai com código 1 se algo falhar (o CI usa isso).
"""
import ast
import itertools
import pathlib
import re
import sys
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def carregar(nome):
    texto = (RAIZ / "game" / "historias" / nome / "dados.rpy").read_text(encoding="utf-8")
    m = re.search(r"## BEGIN DECISOES_(\w+)[^\n]*\n(.*?)\n\s*## END DECISOES_\1", texto, re.S)
    if not m:
        sys.exit(f"bloco DECISOES não encontrado em {nome}/dados.rpy")
    tabelas = {}
    for alvo in re.finditer(r"^\s*(\w+)\s*=\s*", m.group(2), re.M):
        inicio = alvo.end()
        # literal até o próximo "NOME =" no início de linha ou fim do bloco
        prox = re.search(r"^\s*\w+\s*=\s*", m.group(2)[inicio:], re.M)
        trecho = m.group(2)[inicio:inicio + prox.start()] if prox else m.group(2)[inicio:]
        tabelas[alvo.group(1)] = ast.literal_eval(trecho.strip())
    dec = next(v for k, v in tabelas.items() if k.startswith("DECISOES"))
    canon = next(v for k, v in tabelas.items() if k.startswith("CANONICA"))
    return dec, canon


def validar(dec, canon):
    erros = []
    for n, ops in dec.items():
        if not 2 <= len(ops) <= 3:
            erros.append(f"D{n}: {len(ops)} opções")
        for letra, (ef, fl) in ops.items():
            if len(ef) != 4 or not all(isinstance(x, int) for x in ef):
                erros.append(f"D{n}{letra}: efeitos inválidos {ef}")
            if not isinstance(fl, list):
                erros.append(f"D{n}{letra}: flags devem ser lista")
        for d in range(4):
            mx = max(v[0][d] for v in ops.values())
            if ops[canon[n]][0][d] != mx:
                erros.append(f"D{n}: a opção ★ {canon[n]} não é o máximo na dimensão {d}")
    return erros


def jogar_renato(e):
    """Mesma lógica de game/historias/renato (cenas e Quadro D3).
    Retorna (decisões jogadas, desfecho)."""
    if e[3] == "B" or (e[3] == "A" and e[2] == "C"):  # Renato vai embora na Cena 3
        return (1, 2, 3), "C"
    if e[7] in ("A", "C"):  # sai da UPA sem passar pelo Serviço Social
        return tuple(range(1, 9)), "B"
    if e[9] == "B" and e[10] != "A" and e[11] != "B":
        return tuple(range(1, 12)), "B"
    return tuple(range(1, 12)), "A"


def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "renato"
    dec, canon = carregar(nome)
    erros = validar(dec, canon)
    if nome == "renato":
        if jogar_renato(canon)[1] != "A":
            erros.append("linha canônica não termina no Desfecho A")
        caminhos = {}
        for combo in itertools.product(*[sorted(dec[k]) for k in sorted(dec)]):
            e = dict(zip(sorted(dec), combo))
            jogadas, d = jogar_renato(e)
            caminhos[tuple(e[j] for j in jogadas)] = d
        cont = Counter(caminhos.values())
        print(f"{nome}: {len(dec)} decisões; {len(caminhos)} caminhos distintos "
              f"(A: {cont['A']}, B: {cont['B']}, C: {cont['C']}; Apêndice D do roteiro)")
    if erros:
        print("\n".join("ERRO: " + e for e in erros))
        sys.exit(1)
    print(f"{nome}: tabela de decisões ok")


if __name__ == "__main__":
    main()
