from ai_business_automation.infrastructure.ai.provider import AIProvider
from ai_business_automation.infrastructure.ai.response import AIResponse


class MockProvider(AIProvider):

    def generate(self, prompt: str) -> AIResponse:

        return AIResponse(
            content="""
{
    "summary": "Resumo fake",
    "decisions": ["Decisão 1"],
    "tasks": ["Tarefa 1"],
    "risks": ["Risco 1"],
    "next_steps": ["Próximo passo"]
}
""",
            model="mock-model",
            usage_tokens=10,
        )