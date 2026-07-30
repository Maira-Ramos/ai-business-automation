from google import genai

from ai_business_automation.core.settings import settings
from ai_business_automation.infrastructure.ai.provider import AIProvider
from ai_business_automation.infrastructure.ai.response import AIResponse

from google.genai import errors
from ai_business_automation.infrastructure.ai.exceptions import AIProviderError

class GeminiProvider(AIProvider):
    
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )
    def generate(self, prompt: str) -> AIResponse:
        
        try:
            response = self.client.models.generate_content(
                model=settings.model_name,
                contents=prompt,
            )
            return AIResponse(
                content=response.text,
                model=settings.model_name,
            )
        except errors.ClientError as exc:
            raise AIProviderError(
                f"Erro ao comunicar com o Gemini: {exc}"
            ) from exc
  