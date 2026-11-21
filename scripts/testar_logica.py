"""Executa a lógica Python do núcleo e de uma história fora do Ren'Py.

Carrega os blocos "init python" de game/nucleo/estado.rpy e de
game/historias/<nome>/dados.rpy com um store simulado e percorre todos os
caminhos de decisão, chamando as mesmas funções que o jogo chama
(escolher, desfecho, mapa, caderno, barras, guardar/restaurar ponto,
concluir_historia). Pega erros que o lint do Ren'Py não vê, porque só
apareceriam durante a partida. Antes, confere as cenas contra a tabela de
decisões e os atalhos de teste (conferir_cenas).

Uso: python3 scripts/testar_logica.py renato
"""
import itertools
import pathlib
import re
import sys
import textwrap

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def blocos_python(caminho):
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    blocos, i = [], 0
    while i < len(linhas):
        if re.match(r"^init(\s+-?\d+)?\s+python\s*:", linhas[i]):
            corpo = []
            i += 1
            while i < len(linhas) and (linhas[i].startswith((" ", "\t")) or not linhas[i].strip()):
                corpo.append(linhas[i])
                i += 1
            blocos.append(textwrap.dedent("\n".join(corpo)))
        else:
            i += 1
    return blocos


class Store:
    def __init__(self, ns):
        object.__setattr__(self, "_ns", ns)

    def __getattr__(self, k):
        try:
            return self._ns[k]
        except KeyError:
            raise AttributeError(k)

    def __setattr__(self, k, v):
        self._ns[k] = v


class Persistent:
    progresso = {}


class Renpy:
    @staticmethod
    def save_persistent():
        pass


def carregar(nome):
    ns = {"persistent": Persistent(), "renpy": Renpy(), "Character": lambda *a, **k: None}
    ns["store"] = Store(ns)
    for arq in (RAIZ / "game/nucleo/estado.rpy", RAIZ / f"game/historias/{nome}/dados.rpy"):
        for bloco in blocos_python(arq):
            exec(compile(bloco, str(arq), "exec"), ns)
    return ns


def caminho_renato(e):
    """Decisões jogadas e desfecho, como em game/historias/renato/cenas.rpy."""
    jog = [1, 2, 3]
    if e[3] == "B" or (e[3] == "A" and e[2] == "C"):
        return jog, "C"
    jog += [4, 5, 6, 7, 8]
    if e[7] in ("A", "C"):
        return jog, None
    return jog + [9, 10, 11], None


def conferir_cenas(nome, ns):
    """Confere o texto das cenas contra o registro da história:
    cada escolher(n, "X") usa uma opção da tabela, cada opção da tabela
    aparece em alguma cena e cada atalho aponta para um label existente."""
    pasta = RAIZ / "game" / "historias" / nome
    texto = "\n".join(p.read_text(encoding="utf-8") for p in sorted(pasta.glob("*.rpy")))
    h = ns["HISTORIAS"][nome]
    tabela = {(n, letra) for n, ops in h["decisoes"].items() for letra in ops}
    nas_cenas = {(int(n), letra) for n, letra in re.findall(r'escolher\(\s*(\d+)\s*,\s*"([A-C])"\s*\)', texto)}
    erros = [f"escolher({n}, \"{l}\") nas cenas não existe na tabela" for n, l in sorted(nas_cenas - tabela)]
    erros += [f"opção {n}{l} da tabela não aparece em nenhuma cena" for n, l in sorted(tabela - nas_cenas)]
    labels = set(re.findall(r"^label\s+(\w+)", texto, re.M))
    erros += [f"atalho {r!r} aponta para o label inexistente {lab!r}" for r, lab in h["atalhos"] if lab not in labels]
    if h.get("label") and h["label"] not in labels:
        erros.append(f"label de início {h['label']!r} não existe")
    if erros:
        sys.exit("\n".join("ERRO: " + e for e in erros))
    print(f"{nome}: cenas conferidas com a tabela ({len(tabela)} opções, {len(h['atalhos'])} atalhos)")


def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "renato"
    ns = carregar(nome)
    conferir_cenas(nome, ns)
    if nome != "renato":
        print(f"{nome}: lógica carregada (sem simulação de caminhos)")
        return
    dec = ns["DECISOES_RENATO"]
    vistos, n = set(), 0
    for combo in itertools.product(*[sorted(dec[k]) for k in sorted(dec)]):
        e = dict(zip(sorted(dec), combo))
        jog, des = caminho_renato(e)
        chave = tuple(e[j] for j in jog)
        if chave in vistos:
            continue
        vistos.add(chave)
        ns["iniciar_historia"]("renato")
        for j in jog:
            if j in (3, 7):
                ns["guardar_ponto"](j)
            ns["escolher"](j, e[j])
        if des is None:
            des = ns["renato_desfecho"]()
        ns["renato_nos"](des)
        linhas = ns["renato_caderno"](des)
        barras = ns["barras"]()
        assert des in "ABC", chave
        assert all(0 <= v <= 100 for v in barras.values()), (chave, barras)
        assert linhas and all(isinstance(x, str) and x for x in linhas), chave
        assert set(ns["nos_rede"].values()) <= {"aceso", "contorno", "apagado"}, chave
        if des == "C":
            ns["restaurar_ponto"](3)
            assert ns["escolhas"].get(3) is None, chave
        ns["concluir_historia"](des)
        n += 1
    # linha canônica: 100 nas quatro barras, Desfecho A e seis nós no mapa
    ns["iniciar_historia"]("renato")
    for j in range(1, 12):
        ns["escolher"](j, ns["CANONICA_RENATO"][j])
    assert ns["renato_desfecho"]() == "A"
    ns["renato_nos"]("A")
    assert ns["barras"]() == {"direito": 100, "rede": 100, "empatia": 100, "acolhimento": 100}
    assert all(v in ("aceso", "contorno") for v in ns["nos_rede"].values())
    print(f"renato: {n} caminhos distintos executados sem erro; linha canônica ok")


if __name__ == "__main__":
    main()
