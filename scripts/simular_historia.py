"""Confere a tabela de decisões de uma história e simula todos os caminhos.

Lê o bloco entre "## BEGIN DECISOES_<NOME>" e "## END DECISOES_<NOME>" em
game/historias/<nome>/dados.rpy (a mesma tabela que o jogo usa) e verifica:

- cada decisão tem 2 ou 3 opções, cada opção tem 4 efeitos inteiros e uma
  lista de flags;
- a linha canônica (opções ★) é o máximo em todas as dimensões, de modo que
  ela dá 100 nas quatro barras do epílogo;
- (Renato) todos os caminhos terminam em um desfecho A, B ou C.

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
    """Mesma lógica de game/historias/renato (cenas, Quadro D3)."""
    f = set()
    if e[2] == "C":
        f.add("sem_orientacao")
    if e[3] == "B":
        return "C"
    if e[3] == "A" and "sem_orientacao" in f:
        return "C"
    if e[7] in ("A", "C"):
        return "B"
    if e[9] == "B" and e[10] != "A" and e[11] != "B":
        return "B"
    return "A"


def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "renato"
    dec, canon = carregar(nome)
    erros = validar(dec, canon)
    if nome == "renato":
        if jogar_renato(canon) != "A":
            erros.append("linha canônica não termina no Desfecho A")
        cont = Counter()
        for combo in itertools.product(*[sorted(dec[k]) for k in sorted(dec)]):
            d = jogar_renato(dict(zip(sorted(dec), combo)))
            if d not in "ABC":
                erros.append(f"caminho sem desfecho: {combo}")
                break
            cont[d] += 1
        print(f"{nome}: {len(dec)} decisões; combinações por desfecho: {dict(cont)}")
    if erros:
        print("\n".join("ERRO: " + e for e in erros))
        sys.exit(1)
    print(f"{nome}: tabela de decisões ok")


if __name__ == "__main__":
    main()
