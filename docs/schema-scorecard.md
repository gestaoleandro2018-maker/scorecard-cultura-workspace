# Estrutura do scorecard.json

O agente grava `scorecard.json` com este formato. O script `tools/montar_html.py` injeta esses dados no modelo `template/scorecard_template.html`.

```json
{
  "avaliacao": "título da entrevista",
  "candidato": "nome da pessoa candidata",
  "vaga": "nome da vaga",
  "senioridade_alvo": "Júnior | Pleno | Sênior | Especialista | Coordenação | Gerência+",
  "trilha": "Analista (IC) | Liderança",
  "ta": "nome da TA",
  "contexto_vinculo": "A/B/C + 1 linha",
  "senioridade_percebida": "nível — justificativa — abaixo/alinhada/acima do alvo",
  "divergencia": "opcional",
  "itens": [
    {
      "nome": "Inovação",
      "grupo": "pilar | lideranca",
      "nota": 3,
      "rotulo": "Evidente",
      "nivel": "Sênior",
      "iniciativa": "Iniciativa própria | Induzida",
      "recorrencia": "Pontual | Recorrente",
      "escopo": "tarefa | time | times | organização",
      "perguntas": ["pergunta resumida"],
      "star": {
        "situacao": "frase narrada",
        "tarefa": "frase narrada",
        "acao": "frase narrada",
        "resultado": "frase narrada"
      },
      "analise": "1 a 2 frases afirmativas, executivas",
      "pergunta_sugerida": "só quando nota = null",
      "trechos": [{"texto": "trecho literal", "tempo": "5:08"}]
    }
  ],
  "resumo": {
    "media_pilares": 3.0,
    "media_comportamentos": null,
    "media_final": 3.0,
    "conta": "(3 + 3 + 3) ÷ 3 = 3,0 – Evidente",
    "pontos_fortes": ["..."],
    "pontos_atencao": ["..."],
    "aprofundar": ["..."]
  },
  "temas": [{"tema": "Pretensão salarial / modelo de contratação", "texto": "..."}],
  "parecer": {"status": "APROVADO | REPROVADO | INCONCLUSIVO", "motivo": "1 linha"}
}
```

Regras: `nota` é `null` para "Não avaliado – aprofundar" (sem `star`, com `pergunta_sugerida`). `media_comportamentos` é `null` na trilha Analista (IC).
