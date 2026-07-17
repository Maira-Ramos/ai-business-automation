from dataclasses import dataclass, field


@dataclass(slots=True)
class AnalysisResult:

    summary: str = ""

    decisions: list[str] = field(default_factory=list)

    tasks: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)

    next_steps: list[str] = field(default_factory=list)