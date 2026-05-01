from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class TaskStep:
    id: int
    title: str
    detail: str
    acceptance: str


@dataclass
class AgentMessage:
    role: str
    content: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


@dataclass
class StepResult:
    step_id: int
    title: str
    output: str
    evidence: list[str]


@dataclass
class ReviewResult:
    passed: bool
    score: int
    findings: list[str]
    improvements: list[str]


@dataclass
class WorkflowResult:
    task: str
    steps: list[TaskStep]
    results: list[StepResult]
    review: ReviewResult
    report_markdown: str
    messages: list[AgentMessage]
    metadata: dict[str, Any]

