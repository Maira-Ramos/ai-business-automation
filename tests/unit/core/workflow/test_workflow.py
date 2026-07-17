from ai_business_automation.core.workflow.context import WorkflowContext
from ai_business_automation.core.workflow.step import WorkflowStep
from ai_business_automation.core.workflow.workflow import Workflow


class FakeStep(WorkflowStep):

    def execute(self, context: WorkflowContext) -> None:
        context.variables["executed"] = True


def test_workflow_executes_steps():

    workflow = Workflow("Teste")

    workflow.add(FakeStep())

    context = WorkflowContext()

    workflow.run(context)

    assert context.variables["executed"] is True

    assert len(context.events) == 2

    assert len(context.logs) == 2