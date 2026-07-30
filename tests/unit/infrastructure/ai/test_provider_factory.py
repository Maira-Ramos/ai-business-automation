from ai_business_automation.infrastructure.ai.provider_factory import ProviderFactory
from ai_business_automation.infrastructure.ai.gemini_provider import GeminiProvider


def test_provider_factory_returns_gemini():

    provider = ProviderFactory.create()

    assert isinstance(provider, GeminiProvider)