from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from .agents import ExecutorAgent, PlannerAgent, ReporterAgent, ReviewerAgent
from .llm import ChatModel
from .models import WorkflowResult


class AgentWorkflow:
    def __init__(self, model: ChatModel) -> None:
        self.planner = PlannerAgent(model)
        self.executor = ExecutorAgent(model)
        self.reviewer = ReviewerAgent(model)
        self.reporter = ReporterAgent(model)

    def run(self, task: str) -> WorkflowResult:
        steps, planner_message = self.planner.plan(task)
        results, executor_messages = self.executor.execute(task, steps)
        review, reviewer_message = self.reviewer.review(task, steps, results)
        report, reporter_message = self.reporter.report(task, steps, results, review)
        messages = [planner_message, *executor_messages, reviewer_message, reporter_message]
        return WorkflowResult(
            task=task,
            steps=steps,
            results=results,
            review=review,
            report_markdown=report,
            messages=messages,
            metadata={
                "created_at": datetime.now().isoformat(timespec="seconds"),
                "agent_count": 4,
                "workflow": ["planner", "executor", "reviewer", "reporter"],
            },
        )


def save_result(result: WorkflowResult, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    md_path = output_dir / f"agent-run-{stamp}.md"
    json_path = output_dir / f"agent-run-{stamp}.json"
    md_path.write_text(result.report_markdown, encoding="utf-8")
    json_path.write_text(
        json.dumps(asdict(result), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return md_path, json_path

