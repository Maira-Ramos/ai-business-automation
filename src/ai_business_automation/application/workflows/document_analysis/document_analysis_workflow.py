from ai_business_automation.core.workflow.workflow import Workflow

from ai_business_automation.application.services.ai_service import AIService
from ai_business_automation.application.workflows.document_analysis.steps.analyze_document_step import (
    AnalyzeDocumentStep,
)


class DocumentAnalysisWorkflow(Workflow):

    def __init__(self, ai_service: AIService):

        super().__init__(
            "DocumentAnalysisWorkflow"
        )

        self.add(
            AnalyzeDocumentStep(
                ai_service
            )
        )
