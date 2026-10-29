#!/usr/bin/env python3
"""Gera imagens do jogo com a API de imagens da OpenAI (gpt-image-1).

Uso rápido (uma imagem):
    python scripts/gerar_imagens.py --estilo objeto --nome obj_mochila \
        --prompt "A worn backpack resting on the floor, faded green canvas"

Uso em lote (recomendado):
    python scripts/gerar_imagens.py --lista scripts/imagens.exemplo.json

A chave da API vem de OPENAI_API_KEY (variável de ambiente ou arquivo .env na
raiz do projeto — .env já está no .gitignore).

Cada estilo abaixo replica os blocos usados na entrega de 14-15/07/2026,
documentados em assets-gerados/PROMPTS-GERADOS.md.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_PADRAO = RAIZ / "assets-gerados"
LOG = "_geracao_log.json"

MODELO = "gpt-image-1"
TAMANHOS_VALIDOS = ("1024x1024", "1536x1024", "1024x1536", "auto")
QUALIDADES_VALIDAS = ("low", "medium", "high", "auto")

# --------------------------------------------------------------------------
# Blocos de estilo (sufixados ao prompt de conteúdo)
# --------------------------------------------------------------------------

ESTILOS: dict[str, dict] = {
    "cenario": {
        "bloco": (
            "digital watercolor illustration, soft loose washes, muted faded pastel palette, "
            "simplified almost cartoonish shapes, minimal fine detail, gentle soft edges, "
            "light paper texture, slightly desaturated, calm subdued mood, soft background blur, "
            "mobile visual novel background, clean uncluttered composition, eye-level view, "
            "no text, no letters, no logos"
        ),
        "tamanho": "1536x1024",
        "transparente": False,
    },
    "objeto": {
        "bloco": (
            "digital watercolor illustration, single object study, soft loose washes, muted faded pastel palette, "
            "simplified but clearly readable shapes, gentle soft edges, light paper texture, slightly desaturated, "
            "calm mood, centered close-up prop, transparent background, subtle soft shadow beneath, "
            "mobile game item art, clean and uncluttered, no people, no hands, no readable text, no letters, no numbers"
        ),
        "tamanho": "1024x1024",
        "transparente": True,
    },
    "personagem": {
        "bloco": (
            "clean semi-realistic comic illustration style, soft cel shading, natural proportions, "
            "warm approachable rendering, full body standing character for a visual novel sprite, "
            "facing slightly toward viewer, isolated character cutout, plain empty transparent background, "
            "no environment, no floor, no wall, no text, no watermark, "
            "consistent with a Brazilian public health (SUS) educational game cast"
        ),
        "tamanho": "1024x1536",
        "transparente": True,
    },
    "ui": {
        "bloco": (
            "digital watercolor illustration, soft loose washes, gentle soft edges, light paper texture, "
            "slightly desaturated, hand-painted game UI element, single element centered, "
            "transparent background, nothing else in frame, no text, no letters, no numbers, no logos"
        ),
        "tamanho": "1024x1024",
        "transparente": True,
    },
    "nenhum": {"bloco": "", "tamanho": "1024x1024", "transparente": False},
}


# --------------------------------------------------------------------------
# Infra
# --------------------------------------------------------------------------


def carregar_env() -> None:
    """Lê .env da raiz do projeto sem exigir python-dotenv."""
    env = RAIZ / ".env"
    if not env.exists():
        return
    for linha in env.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip("'\""))


def montar_prompt(item: dict) -> str:
    estilo = ESTILOS[item["estilo"]]
    bloco = item.get("bloco_extra") or estilo["bloco"]
    prompt = item["prompt"].strip()
    if bloco:
        prompt = f"{prompt.rstrip('.')}. {bloco}"
    return prompt


def conferir_alpha(caminho: Path) -> str:
    """Confere o canal alpha de verdade (não a olho). Retorna um rótulo curto."""
    try:
        from PIL import Image
    except ImportError:
        return "alpha não verificado (Pillow ausente)"
    with Image.open(caminho) as img:
        if img.mode != "RGBA":
            return f"sem canal alpha (modo {img.mode})"
        minimo, _ = img.getchannel("A").getextrema()
    return "transparente OK" if minimo == 0 else "OPACO — o modelo pintou fundo"


def registrar_log(pasta: Path, registro: dict) -> None:
    arquivo = pasta / LOG
    try:
        historico = json.loads(arquivo.read_text(encoding="utf-8"))
        if not isinstance(historico, list):
            historico = []
    except (FileNotFoundError, json.JSONDecodeError):
        historico = []
    historico.append(registro)
    arquivo.write_text(json.dumps(historico, ensure_ascii=False, indent=1), encoding="utf-8")


# --------------------------------------------------------------------------
# Geração
# --------------------------------------------------------------------------


def gerar(cliente, item: dict, args) -> bool:
    nome = item["nome"]
    pasta = Path(item.get("saida") or args.saida)
    if not pasta.is_absolute():
        pasta = RAIZ / pasta
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / f"{nome}.png"

    if destino.exists() and not args.substituir:
        print(f"  · {nome}: já existe, pulando (use --substituir para refazer)")
        return True

    estilo = ESTILOS[item["estilo"]]
    tamanho = item.get("tamanho") or args.tamanho or estilo["tamanho"]
    transparente = item.get("transparente", estilo["transparente"])
    prompt = montar_prompt(item)

    if args.simular:
        print(f"  · {nome} [{tamanho}, {'transparente' if transparente else 'opaco'}] -> {destino}")
        print(f"    {prompt}")
        return True

    parametros = dict(
        model=MODELO,
        prompt=prompt,
        size=tamanho,
        quality=args.qualidade,
        output_format="png",
        n=1,
    )
    if transparente:
        parametros["background"] = "transparent"

    inicio = time.time()
    for tentativa in range(1, args.tentativas + 1):
        try:
            resposta = cliente.images.generate(**parametros)
            break
        except Exception as erro:  # rede, rate limit, moderação...
            if tentativa == args.tentativas:
                print(f"  x {nome}: falhou após {tentativa} tentativa(s) — {erro}")
                return False
            espera = 5 * tentativa
            print(f"  ! {nome}: erro ({erro}); nova tentativa em {espera}s")
            time.sleep(espera)

    segundos = round(time.time() - inicio)
    destino.write_bytes(base64.b64decode(resposta.data[0].b64_json))

    situacao = conferir_alpha(destino) if transparente else "opaco"
    print(f"  ✓ {nome}: {destino.name} ({tamanho}, {segundos}s) — {situacao}")

    registrar_log(
        pasta,
        {
            "nome": nome,
            "arquivo": str(destino),
            "segundos": segundos,
            "prompt": prompt,
            "size": tamanho,
            "quality": args.qualidade,
            "background": "transparent" if transparente else "opaque",
            "alpha": situacao,
        },
    )
    return True


def carregar_itens(args) -> list[dict]:
    if args.lista:
        caminho = Path(args.lista)
        if not caminho.is_absolute():
            caminho = RAIZ / caminho
        dados = json.loads(caminho.read_text(encoding="utf-8"))
        itens = dados["imagens"] if isinstance(dados, dict) else dados
    else:
        itens = [{"nome": args.nome, "prompt": args.prompt, "estilo": args.estilo}]

    for i, item in enumerate(itens, 1):
        faltando = [c for c in ("nome", "prompt") if not item.get(c)]
        if faltando:
            sys.exit(f"Item {i} da lista sem campo(s): {', '.join(faltando)}")
        item.setdefault("estilo", args.estilo)
        if item["estilo"] not in ESTILOS:
            sys.exit(f"Item '{item['nome']}': estilo '{item['estilo']}' inválido "
                     f"(use: {', '.join(ESTILOS)})")
        tamanho = item.get("tamanho")
        if tamanho and tamanho not in TAMANHOS_VALIDOS:
            sys.exit(f"Item '{item['nome']}': tamanho '{tamanho}' inválido "
                     f"(use: {', '.join(TAMANHOS_VALIDOS)})")
    if args.apenas:
        alvos = set(args.apenas)
        itens = [i for i in itens if i["nome"] in alvos]
        if not itens:
            sys.exit("Nenhum item da lista bate com --apenas")
    return itens


def main() -> int:
    p = argparse.ArgumentParser(
        description="Gera imagens do jogo com gpt-image-1 (OpenAI).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    fonte = p.add_mutually_exclusive_group(required=True)
    fonte.add_argument("--lista", help="JSON com a lista de imagens (ver scripts/imagens.exemplo.json)")
    fonte.add_argument("--prompt", help="Prompt de conteúdo de uma única imagem")

    p.add_argument("--nome", help="Nome do arquivo (sem .png) — obrigatório com --prompt")
    p.add_argument("--estilo", default="objeto", choices=list(ESTILOS),
                   help="Bloco de estilo aplicado (padrão: objeto)")
    p.add_argument("--saida", default=str(SAIDA_PADRAO), help="Pasta de destino (padrão: assets-gerados/)")
    p.add_argument("--tamanho", choices=TAMANHOS_VALIDOS, help="Sobrescreve o tamanho do estilo")
    p.add_argument("--qualidade", default="high", choices=QUALIDADES_VALIDAS, help="Padrão: high")
    p.add_argument("--tentativas", type=int, default=3, help="Tentativas por imagem (padrão: 3)")
    p.add_argument("--apenas", nargs="+", metavar="NOME", help="Gera só estes itens da lista")
    p.add_argument("--substituir", action="store_true", help="Refaz imagens já existentes")
    p.add_argument("--simular", action="store_true", help="Mostra os prompts finais sem chamar a API")
    args = p.parse_args()

    if args.prompt and not args.nome:
        p.error("--prompt exige --nome")

    itens = carregar_itens(args)

    cliente = None
    if not args.simular:
        carregar_env()
        if not os.environ.get("OPENAI_API_KEY"):
            sys.exit("OPENAI_API_KEY não definida (exporte a variável ou crie um .env na raiz).")
        try:
            from openai import OpenAI
        except ImportError:
            sys.exit("Pacote 'openai' ausente. Instale com: pip install openai pillow")
        cliente = OpenAI()

    print(f"{len(itens)} imagem(ns) · modelo {MODELO} · qualidade {args.qualidade}"
          f"{' · SIMULAÇÃO' if args.simular else ''}")
    falhas = [item["nome"] for item in itens if not gerar(cliente, item, args)]

    if falhas:
        print(f"\n{len(falhas)} falha(s): {', '.join(falhas)}")
        return 1
    print("\nConcluído.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
