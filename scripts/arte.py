#!/usr/bin/env python3
"""Fluxo de arte do Além da Rua: prompts, pedidos no GitHub e importação para o jogo.

Fontes (pasta arte/):
  estilo.json          blocos de estilo por tipo de imagem, regras e bloco negativo
  personagens.json     ficha fixa de cada personagem + link da model sheet
  pedidos/<hist>.json  imagens que cada história precisa (id = nome no código)

Comandos:
  prompts  --historia renato             gera arte/prompts/renato.md (prompts prontos)
  assistente                             gera arte/assistente/INSTRUCOES.txt (Gem e Projeto do ChatGPT)
  issues   --historia renato [--simular] [--atualizar]
                                         cria uma issue por pedido no Project (idempotente)
  importar --issue 130                   baixa a última imagem comentada na issue,
                                         confere, converte para WebP e grava em game/images/
  importar --arquivo img.png --pedido renato/aqua_classificacao [--destino pasta]
                                         o mesmo, a partir de um arquivo local

Requer: gh autenticado (issues/importar) e Pillow (importar).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARTE = RAIZ / "arte"
IMAGENS = RAIZ / "game" / "images"
REPO = "pet-saude-poprua/pet-saude-poprua"
ORG = "pet-saude-poprua"
PROJETO = 1
MARCA = "<!-- arte:{historia}/{id} -->"
RE_MARCA = re.compile(r"<!-- arte:([\w-]+)/([\w-]+) -->")
PRIORIDADE = {"alta": "prioridade:alta", "media": "prioridade:média", "baixa": "prioridade:baixa"}

CHECKLIST = {
    "comum": [
        "Parece da mesma família das referências (traço, paleta, luz).",
        "Nenhum texto legível (placas, telas e papéis com manchas no lugar de letras).",
        "Nada que contrarie o roteiro (lugar, objetos, horário).",
    ],
    "cenario": [
        "Formato paisagem 16:9.",
        "Sem pessoas.",
        "Centro e parte de baixo livres para o personagem.",
    ],
    "cena": [
        "Formato paisagem 16:9.",
        "Personagens iguais às model sheets (rosto, cabelo, roupa, cores).",
        "Mãos e rostos sem deformação.",
    ],
    "sprite": [
        "Corpo inteiro, retrato (vertical).",
        "Fundo transparente (PNG). Se a ferramenta não deixar, peça de novo “transparent background, PNG”.",
        "Igual à model sheet (rosto, cabelo, roupa, cores, crachá).",
        "Mãos e rosto sem deformação.",
    ],
    "objeto": [
        "Quadrado, objeto centralizado.",
        "Fundo transparente (PNG).",
        "Sem mãos nem pessoas.",
    ],
    "overlay": ["Formato paisagem 16:9.", "Visual limpo de interface/documento (não é aquarela)."],
    "ui": ["Fundo transparente (PNG).", "Uma peça só, centralizada."],
}


# --------------------------------------------------------------------------
# Leitura
# --------------------------------------------------------------------------


def ler(caminho: Path) -> dict:
    return json.loads(caminho.read_text(encoding="utf-8"))


def carregar(historia: str) -> tuple[dict, dict, dict, Path]:
    arquivo = ARTE / "pedidos" / f"{historia}.json"
    if not arquivo.exists():
        disponiveis = ", ".join(p.stem for p in (ARTE / "pedidos").glob("*.json"))
        sys.exit(f"Não há arte/pedidos/{historia}.json (disponíveis: {disponiveis})")
    estilo = ler(ARTE / "estilo.json")
    personagens = ler(ARTE / "personagens.json")["personagens"]
    pedidos = ler(arquivo)
    for p in pedidos["pedidos"]:
        if p["tipo"] not in estilo["tipos"]:
            sys.exit(f"{p['id']}: tipo '{p['tipo']}' não existe em arte/estilo.json")
        for k in p.get("personagens", []):
            if k not in personagens:
                sys.exit(f"{p['id']}: personagem '{k}' não existe em arte/personagens.json")
    return estilo, personagens, pedidos, arquivo


def achar_pedido(historia: str, ident: str) -> tuple[dict, dict]:
    estilo, _, pedidos, _ = carregar(historia)
    for p in pedidos["pedidos"]:
        if p["id"] == ident:
            return estilo, p
    sys.exit(f"Pedido '{ident}' não está em arte/pedidos/{historia}.json")


# --------------------------------------------------------------------------
# Prompt e ficha
# --------------------------------------------------------------------------


def montar_prompt(p: dict, estilo: dict, personagens: dict) -> str:
    partes = [p["conteudo"].strip().rstrip(".") + "."]
    for chave in p.get("personagens", []):
        partes.append(
            f"Character: {personagens[chave]['aparencia']}. Keep this character identical to the "
            "attached model sheet (face, hair, body, clothes, colors, badge)."
        )
    partes.append(estilo["tipos"][p["tipo"]]["bloco"] + ".")
    partes.append("Use the attached images as style reference. Avoid: " + estilo["negativo"] + ".")
    return " ".join(partes)


def link(caminho: str) -> str:
    if (RAIZ / caminho).exists():
        return f"[{caminho}](https://github.com/{REPO}/blob/master/{caminho})"
    return caminho


def destino_no_jogo(p: dict, estilo: dict) -> str:
    pasta = estilo["tipos"][p["tipo"]]["jogo"]["pasta"]
    return f"game/images/{pasta}/{p['id']}.webp".replace("images/../", "")


def ficha(p: dict, estilo: dict, personagens: dict, historia: str, com_marca: bool) -> str:
    tipo = estilo["tipos"][p["tipo"]]
    linhas = []
    if com_marca:
        linhas.append(MARCA.format(historia=historia, id=p["id"]))
    linhas += [
        f"**Cena:** {p['cena']}  ",
        f"**Tipo:** {p['tipo']} — {tipo['descricao']} Formato: {tipo['proporcao']}.  ",
        f"**No jogo:** `{p['uso']}` → `{destino_no_jogo(p, estilo)}`",
    ]
    if p.get("issue_mae"):
        linhas.append(f"**Parte de:** #{p['issue_mae']}")
    linhas += ["", f"**O que é:** {p['descricao']}", "", "### 1. Abra o assistente de arte",
               "Use o Gem “Arte Além da Rua” (link em `arte/README.md`) ou seu Projeto no ChatGPT. "
               "Sem o assistente, cole o prompt abaixo direto no ChatGPT ou no Gemini.", "",
               "### 2. Anexe as referências"]
    for chave in p.get("personagens", []):
        c = personagens[chave]
        ms = c.get("model_sheet") or "(sem model sheet: use o sprite do jogo)"
        linhas.append(f"- Model sheet de {c['nome']}: {ms}")
    for ref in p.get("referencias", []):
        linhas.append(f"- {link(ref)}")
    linhas += ["", "### 3. Cole o prompt", "```text", montar_prompt(p, estilo, personagens), "```", "",
               "### 4. Confira antes de entregar"]
    for item in CHECKLIST["comum"] + CHECKLIST.get(p["tipo"], []):
        linhas.append(f"- [ ] {item}")
    linhas += ["", "### 5. Entregue",
               "Comente **nesta issue** com a imagem anexada (o PNG original, sem recortar nem "
               "comprimir) e diga a ferramenta usada. Se refizer, comente de novo: vale a última "
               "imagem. Depois mova o card para **Em revisão**."]
    return "\n".join(linhas)


# --------------------------------------------------------------------------
# prompts
# --------------------------------------------------------------------------


def cmd_prompts(args) -> int:
    estilo, personagens, pedidos, _ = carregar(args.historia)
    saida = ARTE / "prompts" / f"{args.historia}.md"
    partes = [
        f"# Prompts de arte — {pedidos['titulo']}",
        "",
        f"Gerado por `scripts/arte.py prompts --historia {args.historia}` a partir de "
        f"`arte/pedidos/{args.historia}.json`. Não edite à mão: mude o JSON e gere de novo.",
        "",
    ]
    for p in pedidos["pedidos"]:
        titulo = f"## {p['id']}"
        if p.get("issue"):
            titulo += f" (#{p['issue']})"
        partes += [titulo, "", ficha(p, estilo, personagens, args.historia, com_marca=False), ""]
    saida.write_text("\n".join(partes), encoding="utf-8")
    print(f"✓ {saida.relative_to(RAIZ)} ({len(pedidos['pedidos'])} pedidos)")
    return 0


def cmd_assistente(args) -> int:
    estilo = ler(ARTE / "estilo.json")
    personagens = ler(ARTE / "personagens.json")["personagens"]
    l = [
        "Você é o assistente de arte do jogo educacional “Além da Rua” (PET-Saúde Digital, UFPB), "
        "uma visual novel sobre o cuidado a pessoas em situação de rua na rede de saúde de João Pessoa. "
        "Sua função é gerar imagens com estética e personagens sempre consistentes. Responda em português; "
        "escreva os prompts de imagem em inglês.",
        "",
        "COMO TRABALHAR",
        "1. Se a pessoa colar um prompt pronto (vem das issues de arte do GitHub), use-o sem resumir nem trocar o estilo.",
        "2. Se ela só descrever a cena, pergunte o tipo (cenário, sprite, objeto, cena composta, overlay) e monte o "
        "prompt assim: conteúdo da cena + ficha de cada personagem (abaixo, sem alterar) + bloco do tipo + bloco negativo.",
        "3. Use as model sheets do seu conhecimento (arquivo com o nome do personagem) e as imagens anexadas. "
        "A model sheet manda: se um sprite antigo do jogo divergir dela, siga a model sheet.",
        "4. Gere no formato do tipo. Sprites e objetos com fundo transparente (PNG).",
        "5. Depois de gerar, confira o checklist e aponte o que refazer. Nos ajustes, não mude o que já estava aprovado.",
        "6. Lembre: entregar comentando na issue do GitHub com o PNG original anexado.",
        "",
        "REGRAS DE OURO",
    ]
    l += [f"- {r}" for r in estilo["regras_de_ouro"]]
    l += ["", "TIPOS DE IMAGEM (bloco de estilo a colar no fim do prompt)"]
    for nome, t in estilo["tipos"].items():
        l += [f"- {nome} — {t['descricao']} Formato: {t['proporcao']}.", f"  Bloco: {t['bloco']}"]
    l += ["", f"BLOCO NEGATIVO (sempre, como “Avoid: …”): {estilo['negativo']}", "",
          "PERSONAGENS: a ficha (campo “aparencia”, em inglês) está em personagens.json; copie-a igual no prompt "
          "e use a model sheet indicada como referência."]
    for chave, c in personagens.items():
        ms = f"{chave}_model_sheet.jpg" if c.get("model_sheet") else "senhora_referencia.webp (sprite do jogo)" if chave == "senhora" else "sem model sheet"
        l.append(f"- {c['nome'].split(',')[0].split(' (')[0]}: ficha “{chave}”; {ms}")
    l += ["", "CHECKLIST"]
    l += [f"- {i}" for i in CHECKLIST["comum"]]
    l += ["- Cenário: 16:9, sem pessoas, centro e base livres.",
          "- Sprite: corpo inteiro, vertical, fundo transparente, igual à model sheet.",
          "- Objeto: quadrado, centralizado, fundo transparente, sem mãos."]
    texto = "\n".join(l) + "\n"
    saida = ARTE / "assistente" / "INSTRUCOES.txt"
    saida.write_text(texto, encoding="utf-8")
    print(f"✓ {saida.relative_to(RAIZ)} ({len(texto)} caracteres; manter abaixo de 8.000)")
    return 0


# --------------------------------------------------------------------------
# issues
# --------------------------------------------------------------------------


def gh(*args: str, entrada: str | None = None) -> str:
    r = subprocess.run(["gh", *args], input=entrada, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or r.stdout.strip())
    return r.stdout


def graphql(query: str, **variaveis: str) -> dict:
    args = ["api", "graphql", "-f", f"query={query}"]
    for k, v in variaveis.items():
        args += ["-F" if k.endswith("_num") else "-f", f"{k.removesuffix('_num')}={v}"]
    return json.loads(gh(*args))["data"]


def projeto() -> dict:
    d = graphql(
        """query($org:String!,$n:Int!){organization(login:$org){projectV2(number:$n){id
        fields(first:50){nodes{... on ProjectV2Field{id name}
        ... on ProjectV2SingleSelectField{id name options{id name}}}}}}}""",
        org=ORG, n_num=str(PROJETO))["organization"]["projectV2"]
    campos = {c["name"]: c for c in d["fields"]["nodes"] if c}
    return {"id": d["id"], "campos": campos}


def definir_campos(proj: dict, item: str, valores: dict) -> None:
    for nome, valor in valores.items():
        campo = proj["campos"].get(nome)
        if not campo:
            print(f"    ! campo '{nome}' não existe no Project")
            continue
        if "options" in campo:
            opcao = next((o["id"] for o in campo["options"] if o["name"] == valor), None)
            if not opcao:
                print(f"    ! opção '{valor}' não existe no campo '{nome}'")
                continue
            valor_gql = f'{{singleSelectOptionId:"{opcao}"}}'
        else:
            valor_gql = f'{{date:"{valor}"}}'
        graphql(
            f"""mutation{{updateProjectV2ItemFieldValue(input:{{projectId:"{proj['id']}",
            itemId:"{item}",fieldId:"{campo['id']}",value:{valor_gql}}}){{projectV2Item{{id}}}}}}""")


def issues_existentes() -> dict[tuple[str, str], int]:
    dados = json.loads(gh("issue", "list", "--repo", REPO, "--label", "frente:arte", "--state", "all",
                          "--limit", "500", "--json", "number,body"))
    achadas = {}
    for i in dados:
        m = RE_MARCA.search(i["body"] or "")
        if m:
            achadas[(m.group(1), m.group(2))] = i["number"]
    return achadas


def cmd_issues(args) -> int:
    estilo, personagens, pedidos, arquivo = carregar(args.historia)
    existentes = {} if args.simular else issues_existentes()
    proj = None
    mudou = False
    for p in pedidos["pedidos"]:
        titulo = f"Arte · {pedidos['titulo']}: {p['id']} ({p['cena']})"
        corpo = ficha(p, estilo, personagens, args.historia, com_marca=True)
        numero = existentes.get((args.historia, p["id"]))
        if args.simular:
            print(f"--- {titulo}\n{corpo}\n")
            continue
        if numero:
            if args.atualizar:
                gh("issue", "edit", str(numero), "--repo", REPO, "--title", titulo, "--body-file", "-",
                   entrada=corpo)
                print(f"  ↻ #{numero} {p['id']} (atualizada)")
            else:
                print(f"  · #{numero} {p['id']} (já existe)")
        else:
            etiquetas = ["frente:arte", "tipo:tarefa", "disponível", f"historia:{args.historia}"]
            if p.get("prioridade") in PRIORIDADE:
                etiquetas.append(PRIORIDADE[p["prioridade"]])
            cmd = ["issue", "create", "--repo", REPO, "--title", titulo, "--body-file", "-",
                   "--label", ",".join(etiquetas)]
            if pedidos.get("milestone"):
                cmd += ["--milestone", pedidos["milestone"]]
            url = gh(*cmd, entrada=corpo).strip()
            numero = int(url.rstrip("/").rsplit("/", 1)[1])
            print(f"  ✓ #{numero} {p['id']}")
            proj = proj or projeto()
            no = json.loads(gh("api", f"repos/{REPO}/issues/{numero}"))
            item = graphql(
                f"""mutation{{addProjectV2ItemById(input:{{projectId:"{proj['id']}",
                contentId:"{no['node_id']}"}}){{item{{id}}}}}}""")["addProjectV2ItemById"]["item"]["id"]
            definir_campos(proj, item, {"Status": "A fazer", "História": pedidos["projeto_historia"],
                                        "Área": "Arte", "Prazo": pedidos["prazo"]})
            if p.get("issue_mae"):
                try:
                    gh("api", "-X", "POST", f"repos/{REPO}/issues/{p['issue_mae']}/sub_issues",
                       "-F", f"sub_issue_id={no['id']}")
                except RuntimeError as erro:
                    print(f"    ! não virou sub-issue de #{p['issue_mae']}: {erro}")
        if p.get("issue") != numero:
            p["issue"] = numero
            mudou = True
    if mudou:
        arquivo.write_text(json.dumps(pedidos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"✓ números das issues gravados em {arquivo.relative_to(RAIZ)}")
    return 0


# --------------------------------------------------------------------------
# importar
# --------------------------------------------------------------------------


def ultima_imagem_da_issue(numero: int) -> tuple[str, str, str]:
    comentarios = json.loads(gh("api", "--paginate", "-H", "Accept: application/vnd.github.full+json",
                                f"repos/{REPO}/issues/{numero}/comments"))
    for c in reversed(comentarios):
        urls = re.findall(r'<img[^>]+src="([^"]+)"', c.get("body_html") or "")
        if urls:
            return urls[-1].replace("&amp;", "&"), c["user"]["login"], c["html_url"]
    sys.exit(f"#{numero}: nenhum comentário com imagem anexada.")


def pedido_da_issue(numero: int) -> tuple[str, str]:
    corpo = json.loads(gh("issue", "view", str(numero), "--repo", REPO, "--json", "body"))["body"]
    m = RE_MARCA.search(corpo or "")
    if not m:
        sys.exit(f"#{numero} não é uma issue de arte gerada por scripts/arte.py (sem marcador).")
    return m.group(1), m.group(2)


def preparar(origem: Path, p: dict, estilo: dict, forcar: bool):
    from PIL import Image

    jogo = estilo["tipos"][p["tipo"]]["jogo"]
    img = Image.open(origem)
    avisos = []
    if jogo.get("transparente"):
        img = img.convert("RGBA")
        minimo, _ = img.getchannel("A").getextrema()
        if minimo > 0:
            msg = "a imagem não tem fundo transparente"
            if not forcar:
                sys.exit(f"✗ {msg}. Peça uma nova versão com fundo transparente (ou use --forcar).")
            avisos.append(msg)
        caixa = img.getbbox()
        if caixa:
            img = img.crop(caixa)
        limite = jogo.get("altura_max") or jogo.get("largura_max")
        if limite and max(img.size) > limite:
            img.thumbnail((limite, limite), Image.LANCZOS)
    else:
        img = img.convert("RGB")
        alvo_l, alvo_a = jogo["largura"], jogo["altura"]
        if img.width < alvo_l * 0.8:
            avisos.append(f"resolução baixa ({img.width}x{img.height}); o ideal é a partir de {alvo_l}x{alvo_a}")
        razao, alvo = img.width / img.height, alvo_l / alvo_a
        if abs(razao - alvo) > 0.02:
            if abs(razao - alvo) > 0.25:
                avisos.append(f"proporção {img.width}x{img.height} longe de 16:9; o recorte central corta bastante")
            if razao > alvo:
                nova = round(img.height * alvo)
                x = (img.width - nova) // 2
                img = img.crop((x, 0, x + nova, img.height))
            else:
                nova = round(img.width / alvo)
                y = (img.height - nova) // 2
                img = img.crop((0, y, img.width, y + nova))
        img = img.resize((alvo_l, alvo_a), Image.LANCZOS)
    return img, avisos


def linha_image(p: dict, estilo: dict) -> tuple[str, list[str]]:
    nome = p["uso"].removeprefix("image ").strip()
    relativo = Path(destino_no_jogo(p, estilo)).relative_to("game/images").as_posix()
    linha = f'image {nome} = "{relativo}"'
    atuais = []
    padrao = re.compile(rf"^\s*image\s+{re.escape(nome)}\s*=", re.M)
    for rpy in (RAIZ / "game").rglob("*.rpy"):
        for n, texto in enumerate(rpy.read_text(encoding="utf-8").splitlines(), 1):
            if padrao.match(texto):
                atuais.append(f"{rpy.relative_to(RAIZ)}:{n}: {texto.strip()}")
    return linha, atuais


def cmd_importar(args) -> int:
    if args.issue:
        historia, ident = pedido_da_issue(args.issue)
        url, autor, onde = ultima_imagem_da_issue(args.issue)
        print(f"#{args.issue}: {historia}/{ident} — imagem de {autor} ({onde})")
        tmp = Path(tempfile.mkdtemp()) / "entrega"
        urllib.request.urlretrieve(url, tmp)
        origem = tmp
    else:
        if not args.pedido or "/" not in args.pedido:
            sys.exit("Com --arquivo, informe --pedido historia/id (ex.: renato/aqua_classificacao).")
        historia, ident = args.pedido.split("/", 1)
        origem = Path(args.arquivo)
    estilo, p = achar_pedido(historia, ident)
    img, avisos = preparar(origem, p, estilo, args.forcar)
    destino = RAIZ / destino_no_jogo(p, estilo)
    if args.destino:
        destino = Path(args.destino) / destino.name
    destino.parent.mkdir(parents=True, exist_ok=True)
    img.save(destino, "WEBP", quality=85, method=6)
    for a in avisos:
        print(f"  ! {a}")
    print(f"✓ {destino} ({img.width}x{img.height}, {destino.stat().st_size // 1024} KB)")
    linha, atuais = linha_image(p, estilo)
    print(f"\nNo código: {linha}")
    if atuais:
        print("Troque a definição atual:")
        for a in atuais:
            print(f"  {a}")
    else:
        print(f"Ainda não há `image` com esse nome; acrescente em game/nucleo/personagens.rpy "
              f"e use em {p['cena']}.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="comando", required=True)

    a = sub.add_parser("prompts", help="gera arte/prompts/<historia>.md")
    a.add_argument("--historia", required=True)
    a.set_defaults(func=cmd_prompts)

    a = sub.add_parser("assistente", help="gera arte/assistente/INSTRUCOES.txt (Gem/Projeto)")
    a.set_defaults(func=cmd_assistente)

    a = sub.add_parser("issues", help="cria/atualiza uma issue por pedido no Project")
    a.add_argument("--historia", required=True)
    a.add_argument("--simular", action="store_true", help="só mostra o que seria criado")
    a.add_argument("--atualizar", action="store_true", help="reescreve o corpo das issues existentes")
    a.set_defaults(func=cmd_issues)

    a = sub.add_parser("importar", help="traz a imagem entregue para game/images/")
    fonte = a.add_mutually_exclusive_group(required=True)
    fonte.add_argument("--issue", type=int, help="número da issue de arte")
    fonte.add_argument("--arquivo", help="imagem local (teste ou entrega fora do GitHub)")
    a.add_argument("--pedido", help="historia/id, obrigatório com --arquivo")
    a.add_argument("--destino", help="pasta de saída (padrão: a pasta do jogo)")
    a.add_argument("--forcar", action="store_true", help="aceita sprite/objeto sem transparência")
    a.set_defaults(func=cmd_importar)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
