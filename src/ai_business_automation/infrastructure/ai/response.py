from dataclasses import dataclass


@dataclass(slots=True)
class AIResponse:
    content: str

    model: str

    usage_tokens: int | None = None