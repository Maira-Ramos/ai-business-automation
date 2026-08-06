import json

from ai_business_automation.application.services.ai_service import AIService

from .mock_provider import MockProvider


def test_ai_service_uses_provider():

    service = AIService()

    service.provider = MockProvider()

    response = service.generate("Olá")

    data = json.loads(response.content)

    assert data["summary"] == "Resumo fake"
    assert data["decisions"] == ["Decisão 1"]
    assert data["tasks"] == ["Tarefa 1"]
    assert data["risks"] == ["Risco 1"]
    assert data["next_steps"] == ["Próximo passo"]