from datetime import datetime

from .context import WorkflowContext


class WorkflowLogger:

    def info(self, context: WorkflowContext, message: str) -> None:
        self._add_log(
            context,
            "INFO",
            message
        )


    def error(self, context: WorkflowContext, message: str) -> None:
        self._add_log(
            context,
            "ERROR",
            message
        )


    def _add_log(
        self,
        context: WorkflowContext,
        level: str,
        message: str
    ) -> None:

        timestamp = datetime.now().isoformat()

        log_entry = (
            f"[{timestamp}] "
            f"{level}: "
            f"{message}"
        )

        context.logs.append(log_entry)