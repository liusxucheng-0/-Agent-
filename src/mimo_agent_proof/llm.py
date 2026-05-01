from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol

import requests


class ChatModel(Protocol):
    def complete(self, system: str, user: str) -> str:
        """Return a model completion."""


@dataclass
class OfflineModel:
    """Deterministic model used when no external API key is available."""

    def complete(self, system: str, user: str) -> str:
        if "Planner" in system:
            return (
                "1. 明确任务目标与验收标准\n"
                "2. 拆解执行步骤并标注产物\n"
                "3. 生成可提交材料与运行证据\n"
                "4. 审核完整性、风险和后续迭代点"
            )
        if "Reviewer" in system:
            return (
                "整体通过。流程包含目标拆解、执行记录、质量检查和最终报告。"
                "建议后续补充更多真实运行截图和连续使用日志。"
            )
        if "Reporter" in system:
            return "已生成可提交的 Markdown 证明报告，包含项目目标、Agent 流程、影响力和证据路径。"
        return (
            "根据任务要求完成当前步骤，并保留可追溯证据。"
            f"输入摘要：{user[:120]}"
        )


@dataclass
class OpenAICompatibleModel:
    base_url: str
    api_key: str
    model: str
    timeout: int = 60

    def complete(self, system: str, user: str) -> str:
        url = self.base_url.rstrip("/") + "/chat/completions"
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.2,
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()


def build_model(offline: bool = False) -> ChatModel:
    if offline:
        return OfflineModel()

    base_url = os.getenv("MIMO_BASE_URL", "").strip()
    api_key = os.getenv("MIMO_API_KEY", "").strip()
    model = os.getenv("MIMO_MODEL", "").strip()
    if base_url and api_key and model:
        return OpenAICompatibleModel(base_url=base_url, api_key=api_key, model=model)

    return OfflineModel()

