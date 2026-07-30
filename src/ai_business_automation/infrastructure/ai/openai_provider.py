from openai import OpenAI

from ai_business_automation.core.settings import settings

from .provider import AIProvider
from .response import AIResponse


class OpenAIProvider(AIProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

    def generate(self, prompt: str) -> AIResponse:

        response = self.client.responses.create(
            model=settings.model,
            input=prompt,
        )

        return AIResponse(
            content=response.output_text,
            model=settings.model,
            usage_tokens=response.usage.total_tokens
            if response.usage
            else None,
        )