from ai_business_automation.core.workflow.events import (
    WorkflowStarted,
    WorkflowCompleted,
    WorkflowFailed,
)


def test_workflow_started_event():

    event = WorkflowStarted("Teste")

    assert event.workflow_name == "Teste"

    assert event.timestamp is not None


def test_workflow_completed_event():

    event = WorkflowCompleted("Teste")

    assert event.workflow_name == "Teste"

    assert event.timestamp is not None


def test_workflow_failed_event():

    event = WorkflowFailed("Teste")

    assert event.workflow_name == "Teste"

    assert event.timestamp is not None