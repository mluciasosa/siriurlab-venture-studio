#!/usr/bin/env python3
"""Create a file-backed Venture Engine project scaffold for MVP-1."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


PHASES = {
    "0": {"agent": "explorador", "status": "pending", "output_ref": None, "handoff_ref": None, "gate": None},
    "1": {"agent": "cartografo", "status": "pending", "output_ref": None, "handoff_ref": None, "gate": None},
    "2": {"agent": "analista-negocio", "status": "pending", "output_ref": None, "handoff_ref": None, "gate": None},
    "3": {"agent": "arquitecto-ux", "status": "pending", "output_ref": None, "handoff_ref": None, "gate": None},
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_state(project_id: str, project_name: str, mode: str) -> dict:
    return {
        "project_id": project_id,
        "project_name": project_name,
        "mode": mode,
        "current_phase": 0,
        "status": "in_progress",
        "phases": PHASES,
        "pending_input_requests": [],
        "gate_decisions": [],
        "updated_at": utc_now(),
    }


def write_seed(path: Path, project_name: str, mode: str) -> None:
    path.write_text(
        "\n".join(
            [
                f"# SEED DE PROYECTO — {project_name}",
                "",
                "─── MODO ───",
                mode,
                "",
                "─── PROBLEMA / SECTOR ───",
                "[Completar antes de ejecutar Shifu]",
                "",
                "─── ALINEACIÓN ODS ───",
                "[Completar si se conoce]",
                "",
                "─── RESTRICCIONES ───",
                "[Completar presupuesto, geografía, tiempo, riesgos]",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_cost_log(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "# Cost Log",
                "",
                "| phase | tokens_in | tokens_out | usd | notes |",
                "|---|---:|---:|---:|---|",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Venture Engine MVP-1 project scaffold.")
    parser.add_argument("--project-id", required=True, help="Example: proyecto-001-nubia")
    parser.add_argument("--name", required=True, help="Human-readable project name")
    parser.add_argument("--mode", choices=["create", "audit"], default="create")
    parser.add_argument("--runs-dir", default="runs", help="Directory where projects are stored")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files in the project folder")
    args = parser.parse_args()

    project_dir = Path(args.runs_dir) / args.project_id
    if project_dir.exists() and not args.force:
        raise SystemExit(f"ERROR: project already exists: {project_dir}. Use --force to overwrite scaffold files.")

    project_dir.mkdir(parents=True, exist_ok=True)
    for phase in range(4):
        (project_dir / f"fase-{phase}").mkdir(exist_ok=True)

    write_seed(project_dir / "_seed.md", args.name, args.mode)
    write_cost_log(project_dir / "_cost-log.md")
    (project_dir / "_state.json").write_text(
        json.dumps(build_state(args.project_id, args.name, args.mode), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"OK: created {project_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
