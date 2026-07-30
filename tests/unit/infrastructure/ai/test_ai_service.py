from ai_business_automation.application.services.ai_service import AIService

from .mock_provider import MockProvider


def test_ai_service_uses_provider():

    service = AIService()

    service.provider = MockProvider()

    response = service.generate("Olá")

    assert response.content == "Resposta fake para: Olá"
    assert response.model == "mock-model"