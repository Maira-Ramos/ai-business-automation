from ai_business_automation.core.workflow.context import WorkflowContext


def test_context_starts_empty():

    context = WorkflowContext()

    assert context.logs == []

    assert context.events == []

    assert context.variables == {}

    assert context.outputs == {}