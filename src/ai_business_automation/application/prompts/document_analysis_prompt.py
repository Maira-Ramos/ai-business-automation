from ai_business_automation.domain.entities.document import Document

class DocumentAnalysisPrompt:
    
    @staticmethod
    def build(document: Document) -> str:
        
        return f"""
        Analise o documento abaixo.

        Nome:
        {document.name}

        Conteúdo:
        {document.content}

        Retorne APENAS um JSON válido.

        Não utilize markdown.
        Não utilize ```json.
        Não escreva explicações.

        Formato esperado:

        {{
            "summary": "string",
            "decisions": [
                "string"
            ],
            "tasks": [
                "string"
            ],
            "risks": [
                "string"
            ],
            "next_steps": [
                "string"
            ]
        }}
        """