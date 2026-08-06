from ai_business_automation.application.parsers.analysis_result_parser import (
    AnalysisResultParser,
)


def test_analysis_result_parser():

    text = """
    {
        "summary": "Resumo",
        "decisions": ["Decisão 1"],
        "tasks": ["Tarefa 1"],
        "risks": ["Risco 1"],
        "next_steps": ["Próximo passo"]
    }
    """

    result = AnalysisResultParser.parse(text)

    assert result.summary == "Resumo"

    assert result.decisions == [
        "Decisão 1"
    ]

    assert result.tasks == [
        "Tarefa 1"
    ]

    assert result.risks == [
        "Risco 1"
    ]

    assert result.next_steps == [
        "Próximo passo"
    ]