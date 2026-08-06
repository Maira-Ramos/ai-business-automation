import json

from ai_business_automation.domain.entities.analysis_result import AnalysisResult
from ai_business_automation.infrastructure.ai.exceptions import (
    AIResponseParseException,
)


class AnalysisResultParser:

    @staticmethod
    def parse(text: str) -> AnalysisResult:

        try:
            data = json.loads(text)

        except json.JSONDecodeError as error:
            raise AIResponseParseException(
                "Resposta da IA não está em formato JSON válido"
            ) from error


        return AnalysisResult(
            summary=data.get("summary", ""),
            decisions=data.get("decisions", []),
            tasks=data.get("tasks", []),
            risks=data.get("risks", []),
            next_steps=data.get("next_steps", []),
        )