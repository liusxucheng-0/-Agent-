from __future__ import annotations

import argparse
from pathlib import Path

from .llm import build_model
from .workflow import AgentWorkflow, save_result


def load_env_if_available() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a MiMo multi-agent proof workflow.")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run the agent workflow.")
    run_parser.add_argument("--task", required=True, help="Task to process.")
    run_parser.add_argument("--output-dir", default="runs", help="Directory for generated reports.")
    run_parser.add_argument("--offline", action="store_true", help="Force deterministic offline model.")
    return parser


def main(argv: list[str] | None = None) -> int:
    load_env_if_available()
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command != "run":
        parser.print_help()
        return 1

    model = build_model(offline=args.offline)
    workflow = AgentWorkflow(model)
    result = workflow.run(args.task)
    md_path, json_path = save_result(result, Path(args.output_dir))

    print("MiMo Agent workflow completed.")
    print(f"Markdown report: {md_path}")
    print(f"JSON log: {json_path}")
    print(f"Review score: {result.review.score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
