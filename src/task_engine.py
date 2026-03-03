# Gera resumo, tarefas e plano de ação

class TaskEngine:
    def __init__(self, ai_client):
        self.ai = ai_client

    def summarize(self, text: str) -> str:
        return "Resumo placeholder."

    def extract_tasks(self, text: str) -> list:
        prompt = f"""
        Gere um resumo executivo empresarial para o seguinte texto:

        {text}

        O resumo deve incluir:
        - Pontos-chave
        - Riscos
        - Oportunidades
        - Próximos passos recomendados
        """
        return self.ai.generate(prompt)

    def generate_action_plan(self, text: str) -> dict:
        return {
            "what": "Placeholder",
            "why": "Placeholder",
            "who": "Placeholder",
            "when": "Placeholder",
            "where": "Placeholder",
            "how": "Placeholder",
            "how_much": "Placeholder",
        }