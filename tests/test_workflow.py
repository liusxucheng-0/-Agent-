from mimo_agent_proof.llm import OfflineModel
from mimo_agent_proof.workflow import AgentWorkflow


def test_workflow_generates_four_agent_report():
    workflow = AgentWorkflow(OfflineModel())
    result = workflow.run("生成 MiMo Agent 申请证明项目")

    assert len(result.steps) == 4
    assert len(result.results) == 4
    assert result.review.passed is True
    assert result.metadata["agent_count"] == 4
    assert "Planner" in result.report_markdown or "目标澄清" in result.report_markdown

