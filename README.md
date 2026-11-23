# scorecard-cultura-workspace

Área de trabalho do workflow **Scorecard de Cultura BRQ** no Fusion (projeto "Scorecard de Cultura | Avaliação por Competências").

- `template/scorecard_template.html` — modelo visual do scorecard (React + Astryx, tema neutral, arquivo único).
- `tools/montar_html.py` — injeta o `scorecard.json` gerado pelo agente no modelo e gera `scorecard.html`.
- `docs/schema-scorecard.md` — estrutura do `scorecard.json`.
- `exemplos/` — exemplo de dados para conferir o visual.

Teste local: `python3 tools/montar_html.py exemplos/exemplo_ficticio.json /tmp/teste.html`

Repositório provisório: será transferido para um repositório corporativo da BRQ no handover.
