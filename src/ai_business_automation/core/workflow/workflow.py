from .context import WorkflowContext
from .step import WorkflowStep
from .logger import WorkflowLogger
from .events import (
    WorkflowStarted,
    WorkflowCompleted,
    WorkflowFailed,
)


class Workflow:

    def __init__(self, name: str):

        self.name = name

        self.steps: list[WorkflowStep] = []

        self.logger = WorkflowLogger()


    def add(self, step: WorkflowStep):

        self.steps.append(step)


    def run(self, context: WorkflowContext):

        started_event = WorkflowStarted(
            self.name
        )

        context.events.append(
            started_event
        )

        self.logger.info(
            context,
            f"Workflow '{self.name}' iniciado"
        )


        try:

            for step in self.steps:

                step.execute(context)


            completed_event = WorkflowCompleted(
                self.name
            )

            context.events.append(
                completed_event
            )


            self.logger.info(
                context,
                f"Workflow '{self.name}' concluído"
            )


        except Exception as error:

            failed_event = WorkflowFailed(
                self.name
            )

            context.events.append(
                failed_event
            )


            self.logger.error(
                context,
                str(error)
            )


            raise