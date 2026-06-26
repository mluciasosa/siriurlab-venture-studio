#!/usr/bin/env python3
"""Summarize manual Venture Engine cost logs."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CostRow:
    phase: str
    tokens_in: int
    tokens_out: int
    usd: float
    notes: str


def parse_int(value: str) -> int:
    clean = value.strip().replace(",", "")
    return int(clean) if clean else 0


def parse_float(value: str) -> float:
    clean = value.strip().replace("$", "").replace(",", "")
    return float(clean) if clean else 0.0


def parse_table(path: Path) -> list[CostRow]:
    rows: list[CostRow] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or "---" in line or "phase" in line.lower():
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        rows.append(
            CostRow(
                phase=parts[0],
                tokens_in=parse_int(parts[1]),
                tokens_out=parse_int(parts[2]),
                usd=parse_float(parts[3]),
                notes=parts[4],
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a Venture Engine _cost-log.md file.")
    parser.add_argument("cost_log", help="Path to _cost-log.md")
    args = parser.parse_args()

    path = Path(args.cost_log)
    if not path.exists():
        raise SystemExit(f"ERROR: cost log not found: {path}")

    rows = parse_table(path)
    if not rows:
        raise SystemExit(f"ERROR: no cost rows found in {path}")

    by_phase: dict[str, dict[str, float]] = defaultdict(lambda: {"tokens_in": 0, "tokens_out": 0, "usd": 0.0})
    for row in rows:
        by_phase[row.phase]["tokens_in"] += row.tokens_in
        by_phase[row.phase]["tokens_out"] += row.tokens_out
        by_phase[row.phase]["usd"] += row.usd

    total_in = sum(row.tokens_in for row in rows)
    total_out = sum(row.tokens_out for row in rows)
    total_usd = sum(row.usd for row in rows)

    print("COST REPORT")
    print("phase,tokens_in,tokens_out,usd")
    for phase in sorted(by_phase):
        data = by_phase[phase]
        print(f"{phase},{int(data['tokens_in'])},{int(data['tokens_out'])},{data['usd']:.4f}")
    print(f"TOTAL,{total_in},{total_out},{total_usd:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
