from abc import ABC, abstractmethod

from .context import WorkflowContext

class WorkflowStep(ABC):
    
    @abstractmethod
    def execute(self, context: WorkflowContext) -> None:
        """Execute uma etapa do workflow."""