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
    
    Gere uma análise contendo:
    
    - resumo
    - decisões encontradas
    - tarefas identificadas
    - riscos
    - próximos passos
    """