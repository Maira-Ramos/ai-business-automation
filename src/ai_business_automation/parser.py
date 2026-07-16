# Responsável por comunicar com a OpenAI

from src.config import settings

class AIClient:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY

    def generate(self, prompt: str) -> str:
        """
        Função placeholder.
        Depois você implementa a chamada real para a OpenAI.
        """
        return "Resposta fictícia da IA (placeholder)."