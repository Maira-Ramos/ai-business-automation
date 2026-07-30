from ai_business_automation.infrastructure.ai.provider_factory import ProviderFactory
from ai_business_automation.infrastructure.ai.response import AIResponse


class AIService:

    def __init__(self):
        self.provider = ProviderFactory.create()

    def generate(self, prompt: str) -> AIResponse:
        return self.provider.generate(prompt)