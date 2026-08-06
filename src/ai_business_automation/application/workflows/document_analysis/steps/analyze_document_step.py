from ai_business_automation.core.workflow.step import WorkflowStep
from ai_business_automation.core.workflow.context import WorkflowContext

from ai_business_automation.application.services.ai_service import AIService
from ai_business_automation.domain.entities.analysis_result import AnalysisResult


class AnalyzeDocumentStep(WorkflowStep):

    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service


    def execute(self, context: WorkflowContext) -> None:

        if context.document is None:
            raise ValueError("Documento não encontrado no contexto")

        document = context.document

        prompt = f"""
Analise o documento abaixo.

Nome:
{document.name}

Conteúdo:
{document.content}

Gere uma análise contendo:

- resumo
- decisões encontradas
- tarefas identificadas
- riscos
- próximos passos
"""

        response = self.ai_service.generate(prompt)

        context.analysis = AnalysisResult(
            summary=response.content
        )
