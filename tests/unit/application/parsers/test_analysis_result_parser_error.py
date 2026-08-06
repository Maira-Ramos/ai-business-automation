import pytest

from ai_business_automation.application.parsers.analysis_result_parser import (
    AnalysisResultParser,
)

from ai_business_automation.infrastructure.ai.exceptions import (
    AIResponseParseException,
)


def test_analysis_result_parser_invalid_json():

    invalid_response = """
    A análise do documento está pronta.
    O resumo é esse...
    """

    with pytest.raises(AIResponseParseException):
        AnalysisResultParser.parse(invalid_response)