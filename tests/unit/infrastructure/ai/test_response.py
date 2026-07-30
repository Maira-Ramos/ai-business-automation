from ai_business_automation.infrastructure.ai.response import AIResponse


def test_ai_response_defaults():

    response = AIResponse(
        content="Olá",
        model="gemini"
    )

    assert response.content == "Olá"
    assert response.model == "gemini"
    assert response.usage_tokens is None