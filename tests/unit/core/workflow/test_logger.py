from ai_business_automation.core.workflow.context import WorkflowContext
from ai_business_automation.core.workflow.logger import WorkflowLogger


def test_logger_adds_info_message():
    
    context = WorkflowContext()
    
    logger = WorkflowLogger()
    
    logger.info(context, "Workflow iniciado")
    
    assert len(context.logs) == 1
    
    assert "INFO" in context.logs[0]

    assert "Workflow iniciado" in context.logs[0]
    
def test_logger_adds_error_massage():
    
    context = WorkflowContext()
    
    logger = WorkflowLogger()
    
    logger.error(context, "Erro durante a execução")
    
    assert len(context.logs) == 1
    
    assert "ERROR" in context.logs[0]
    
    assert "Erro durante a execução" in context.logs[0]