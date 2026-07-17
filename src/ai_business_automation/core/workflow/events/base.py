from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class WorkflowEvent:

    workflow_name: str

    timestamp: datetime = field(
        default_factory=datetime.now
    )