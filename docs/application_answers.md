# MiMo 申请表填写材料

## 04 请描述你使用 Agent 或 AI 驱动构建的具体成果

我构建了一个面向个人知识工作和研发任务的多 Agent 自动化工作流项目 MiMo Agent Proof Kit，用来沉淀我长期使用 AI Agent 的方法论与真实流程。项目解决的核心痛点是：复杂任务只靠单轮对话容易缺少规划、执行记录、质量复核和可追溯产物。因此我把任务处理拆成 Planner、Executor、Reviewer、Reporter 四个角色：Planner 将用户目标拆为可执行步骤；Executor 调用工具或模型完成每一步；Reviewer 根据验收标准检查遗漏、风险和改进点；Reporter 汇总生成 Markdown/JSON 日志，方便复盘和提交证明。项目支持 OpenAI-compatible API，也支持离线模拟模式，便于稳定展示完整流程。我计划将它用于日常代码审阅、文档生成、学习计划拆解和项目复盘，形成持续的 Agent 使用记录。

## 05 使用证明与影响力证明

建议提交以下内容：

- GitHub 项目链接：上传本仓库后填写你的 GitHub URL。
- 运行日志：执行 `python -m mimo_agent_proof run --task "整理一个 AI Agent 申请证明项目"` 后，提交 `runs/` 目录下生成的 `.md` 或 `.json`。
- 截图：上传终端运行结果、GitHub README 页面、或 `runs/*.md` 的预览截图。

## GitHub 链接占位

上传后替换为：

`https://github.com/<你的用户名>/mimo-agent-proof`

