from ai_business_automation.infrastructure.ai.provider import AIProvider
from ai_business_automation.infrastructure.ai.response import AIResponse


class MockProvider(AIProvider):

    def generate(self, prompt: str) -> AIResponse:
        return AIResponse(
            content=f"Resposta fake para: {prompt}",
            model="mock-model",
            usage_tokens=10,
        )