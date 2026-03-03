import json

def export_json(data) -> str:
    return json.dumps(data, indent=4, ensure_ascii=False)

def export_markdown(summary: str, tasks: list, plan: dict) -> str:
    """
    Gera um Markdown simples.
    """
    md = "# Resumo\n"
    md += f"{summary}\n\n"

    md += "## Tarefas\n"
    for t in tasks:
        md += f"- **{t['title']}** (Prioridade: {t['priority']})\n"

    md += "\n## Plano de Ação (5W2H)\n"
    for key, value in plan.items():
        md += f"- **{key.capitalize()}**: {value}\n"

    return md