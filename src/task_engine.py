# Gera resumo, tarefas e plano de ação

class TaskEngine:
    def __init__(self, ai_client):
        self.ai = ai_client

    def summarize(self, text: str) -> str:
        return "Resumo placeholder."

    def extract_tasks(self, text: str) -> list:
        prompt = f"""
        A partir do texto abaixo, extraia tarefas estruturadas no formato JSON:

        Texto:
        {text}

        Cada tarefa deve conter:
        - title
        - priority (Alta, Média, Baixa)
        - department (Financeiro, RH, Comercial, TI, Jurídico etc.)
        - due (data sugerida ou null)

        Responda SOMENTE com JSON.
        """

        response = self.ai.generate(prompt)

        import json
        try:
            return json.loads(response)
        except:
            return [{"title": "Erro ao processar IA", "priority": "Média"}]

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