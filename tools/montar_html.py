#!/usr/bin/env python3
"""Monta o scorecard HTML a partir do JSON gerado pelo agente.

Uso: python3 tools/montar_html.py scorecard.json scorecard.html
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TEMPLATE = RAIZ / "template" / "scorecard_template.html"
MARCADOR = "__SCORECARD_JSON__"

OBRIGATORIOS = ["avaliacao", "candidato", "vaga", "senioridade_alvo", "trilha", "ta",
                "contexto_vinculo", "senioridade_percebida", "itens", "resumo", "temas", "parecer"]


def validar(d):
    faltando = [k for k in OBRIGATORIOS if k not in d]
    if faltando:
        raise SystemExit(f"JSON incompleto, faltam: {', '.join(faltando)}")
    for it in d["itens"]:
        for k in ("nome", "grupo", "nota", "rotulo", "perguntas", "analise", "trechos"):
            if k not in it:
                raise SystemExit(f"Item '{it.get('nome', '?')}' sem o campo '{k}'")
    if d["parecer"].get("status") not in ("APROVADO", "REPROVADO", "INCONCLUSIVO"):
        raise SystemExit("parecer.status deve ser APROVADO, REPROVADO ou INCONCLUSIVO")


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    dados = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    validar(dados)
    bruto = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    if MARCADOR not in html:
        raise SystemExit("Template sem o marcador de dados")
    Path(sys.argv[2]).write_text(html.replace(MARCADOR, bruto, 1), encoding="utf-8")
    print(f"OK: {sys.argv[2]} gerado para {dados['candidato']}")


if __name__ == "__main__":
    main()
