from ai_business_automation.core.settings import settings
from .gemini_provider import GeminiProvider

from .provider import AIProvider
from .openai_provider import OpenAIProvider

class ProviderFactory:
    
    @staticmethod
    def create() -> AIProvider:
        
        provider = settings.ai_provider.lower()
        
        if provider == "openai":
            return OpenAIProvider()
        
        if provider == "gemini":
            return GeminiProvider()
        
        raise ValueError(
            f"Provider '{provider}' não suportado."
        )