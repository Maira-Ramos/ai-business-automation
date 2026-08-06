import json

from ai_business_automation.domain.entities.analysis_result import (
    AnalysisResult,
)


class AnalysisResultParser:

    @staticmethod
    def parse(text: str) -> AnalysisResult:

        data = json.loads(text)

        return AnalysisResult(
            summary=data.get("summary", ""),
            decisions=data.get("decisions", []),
            tasks=data.get("tasks", []),
            risks=data.get("risks", []),
            next_steps=data.get("next_steps", []),
        )