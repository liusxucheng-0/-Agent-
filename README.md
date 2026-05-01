# MiMo Agent Proof Kit

一个用于证明长期 AI Agent 使用经验的可运行项目：输入一个真实任务，系统会通过“规划 Agent -> 执行 Agent -> 审核 Agent -> 报告 Agent”的流水线完成拆解、执行、复盘与产物沉淀。

项目默认支持离线模拟运行，便于稳定展示完整 Agent 工作流；也可以通过 OpenAI-compatible API 接入 MiMo 或其他模型服务。

## 适合提交到申请表的项目介绍

我构建了一个面向个人知识工作和研发任务的多 Agent 自动化工作流项目 MiMo Agent Proof Kit，用来沉淀我长期使用 AI Agent 的方法论与真实流程。项目解决的核心痛点是：单轮聊天难以稳定完成复杂任务，容易缺少规划、执行记录、质量复核和可追溯产物。因此我把任务处理拆成 Planner、Executor、Reviewer、Reporter 四个角色：Planner 将用户目标拆为可执行步骤；Executor 调用工具或模型完成每一步；Reviewer 根据验收标准检查遗漏、风险和改进点；Reporter 汇总生成 Markdown/JSON 日志，方便复盘和提交证明。该项目支持 OpenAI-compatible API，也支持离线模拟模式，便于在没有额度时展示完整流程。我的目标是把它用于日常代码审阅、文档生成、学习计划拆解和项目复盘，形成长期稳定的 Agent 使用记录。项目包含可运行 CLI、示例任务、测试和完整日志输出，能证明我不仅使用 AI 对话，还在构建可复用、可验证、可持续迭代的 Agent 工作流。

## 表单第 04 项可直接填写

我构建了一个面向个人知识工作和研发任务的多 Agent 自动化工作流项目 MiMo Agent Proof Kit，用来沉淀我长期使用 AI Agent 的方法论与真实流程。项目解决的核心痛点是：复杂任务只靠单轮对话容易缺少规划、执行记录、质量复核和可追溯产物。因此我把任务处理拆成 Planner、Executor、Reviewer、Reporter 四个角色：Planner 将用户目标拆为可执行步骤；Executor 调用工具或模型完成每一步；Reviewer 根据验收标准检查遗漏、风险和改进点；Reporter 汇总生成 Markdown/JSON 日志，方便复盘和提交证明。项目支持 OpenAI-compatible API，也支持离线模拟模式，便于稳定展示完整流程。我计划将它用于日常代码审阅、文档生成、学习计划拆解和项目复盘，形成持续的 Agent 使用记录。

## 表单第 05 项建议提交

- GitHub 项目链接：上传本仓库后填写你的 GitHub URL。
- 运行日志：执行 `python -m mimo_agent_proof run --task "整理一个 AI Agent 申请证明项目"` 后，提交 `runs/` 目录下生成的 `.md` 或 `.json`。
- 截图：可以上传终端运行结果、GitHub README 页面、或 `runs/*.md` 的预览截图。

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
python -m mimo_agent_proof run --task "为 MiMo 申请材料生成一个 Agent 项目说明"
```

如果你还没有模型额度，可以使用离线模式：

```bash
python -m mimo_agent_proof run --task "规划一个一周 AI Agent 学习计划" --offline
```

## 接入 OpenAI-compatible API

复制配置模板：

```bash
copy .env.example .env
```

填写：

```env
MIMO_BASE_URL=https://api.example.com/v1
MIMO_API_KEY=你的APIKey
MIMO_MODEL=your-model-name
```

运行：

```bash
python -m mimo_agent_proof run --task "审阅一个 Python 项目的 README 并给出改进建议"
```

## 工作流

1. Planner Agent：明确目标、约束、验收标准，生成步骤。
2. Executor Agent：逐步产出执行结果，并记录证据。
3. Reviewer Agent：检查步骤覆盖率、风险、缺口和改进建议。
4. Reporter Agent：输出可提交的 Markdown/JSON 证明材料。

## 项目结构

```text
src/mimo_agent_proof/
  agents.py      # 四类 Agent 的核心逻辑
  cli.py         # 命令行入口
  llm.py         # OpenAI-compatible 客户端与离线模拟模型
  workflow.py    # 工作流编排
examples/
  task.md        # 示例任务
docs/
  application_answers.md # 表单填写模板
tests/
  test_workflow.py
```

## 测试

```bash
pytest
```

