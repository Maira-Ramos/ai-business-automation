from dataclasses import dataclass, field
from typing import Any

from ai_business_automation.domain.entities.analysis_result import AnalysisResult
from ai_business_automation.domain.entities.document import Document

from ai_business_automation.core.workflow.events.base import WorkflowEvent

@dataclass(slots=True)
class WorkflowContext:

    document: Document | None = None

    analysis: AnalysisResult | None = None

    variables: dict[str, Any] = field(default_factory=dict)

    outputs: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    logs: list[str] = field(default_factory=list)
    
    events: list[WorkflowEvent] = field(default_factory=list)