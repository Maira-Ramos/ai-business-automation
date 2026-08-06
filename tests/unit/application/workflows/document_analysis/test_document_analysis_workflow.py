from ai_business_automation.application.services.ai_service import AIService
from ai_business_automation.application.workflows.document_analysis import (
    DocumentAnalysisWorkflow,
)
from ai_business_automation.core.workflow.context import WorkflowContext
from ai_business_automation.domain.entities.document import Document

from .mock_provider import MockProvider

def test_document_analysis_workflow():
    service = AIService()
    service.provider = MockProvider()  
    
    workflow = DocumentAnalysisWorkflow(service)
    
    context = WorkflowContext()
    context.document = Document(
        name="teste.txt",
        content="Conteúdo do documento",
    )
    
    workflow.run(context)
    
    assert context.analysis is not None
    assert "Resposta fake" in context.analysis.summary