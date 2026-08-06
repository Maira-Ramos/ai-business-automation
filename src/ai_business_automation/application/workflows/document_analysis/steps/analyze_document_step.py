from ai_business_automation.core.workflow.step import WorkflowStep
from ai_business_automation.core.workflow.context import WorkflowContext

from ai_business_automation.application.services.ai_service import AIService
from ai_business_automation.domain.entities.analysis_result import AnalysisResult

from ai_business_automation.application.prompts.document_analysis_prompt import (
    DocumentAnalysisPrompt,
)

from ai_business_automation.application.parsers.analysis_result_parser import (
    AnalysisResultParser,
)

class AnalyzeDocumentStep(WorkflowStep):

    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service


    def execute(self, context: WorkflowContext) -> None:

        if context.document is None:
            raise ValueError("Documento não encontrado no contexto")

        document = context.document

        prompt = DocumentAnalysisPrompt.build(document)

        response = self.ai_service.generate(prompt)

        context.analysis = AnalysisResultParser.parse(
            response.content
        )
