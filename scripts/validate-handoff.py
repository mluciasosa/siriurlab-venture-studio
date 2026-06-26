#!/usr/bin/env python3
"""Validate a Venture Engine handoff v2 document.

This intentionally uses only Python's standard library. It validates the MVP-1
contract shape, required skill coverage, alias resolution, and referenced
markdown anchors.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL_IO = REPO_ROOT / "contracts" / "skill-io.md"


class ValidationError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"{path}: JSON invalido: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: se esperaba un objeto JSON")
    return data


def load_skill_io(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- skill-io:start -->\s*```json\s*(.*?)\s*```\s*<!-- skill-io:end -->",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ValidationError(f"{path}: no se encontro bloque machine-readable skill-io")
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"{path}: bloque skill-io no es JSON valido: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: skill-io debe ser un objeto JSON")
    return data


def canonical(skill_id: str, aliases: dict[str, str]) -> str:
    seen = set()
    current = skill_id
    while current in aliases:
        if current in seen:
            raise ValidationError(f"alias circular detectado para skill {skill_id}")
        seen.add(current)
        current = aliases[current]
    return current


def require_fields(data: dict[str, Any], fields: list[str], label: str) -> None:
    missing = [field for field in fields if field not in data]
    if missing:
        raise ValidationError(f"{label}: faltan campos obligatorios: {', '.join(missing)}")


def validate_shape(handoff: dict[str, Any]) -> None:
    require_fields(
        handoff,
        [
            "handoff_version",
            "project_id",
            "from_agent",
            "to_agent",
            "required_by_destination",
            "outputs",
            "context_summary",
            "flags",
            "created_at",
        ],
        "handoff",
    )
    if handoff["handoff_version"] != "2.0":
        raise ValidationError("handoff_version debe ser 2.0")
    if not isinstance(handoff["required_by_destination"], list) or not handoff["required_by_destination"]:
        raise ValidationError("required_by_destination debe ser una lista no vacia")
    if not isinstance(handoff["outputs"], list) or not handoff["outputs"]:
        raise ValidationError("outputs debe ser una lista no vacia")
    for idx, output in enumerate(handoff["outputs"]):
        if not isinstance(output, dict):
            raise ValidationError(f"outputs[{idx}] debe ser un objeto")
        require_fields(output, ["skill_id", "output_ref", "type"], f"outputs[{idx}]")
        if "#" not in output["output_ref"]:
            raise ValidationError(f"outputs[{idx}].output_ref debe incluir ancla: {output['output_ref']}")


def anchor_exists(markdown_path: Path, anchor: str) -> bool:
    if not markdown_path.exists():
        raise ValidationError(f"archivo referenciado no existe: {markdown_path}")
    text = markdown_path.read_text(encoding="utf-8")
    explicit_anchor = re.compile(r"\{#" + re.escape(anchor) + r"\}")
    literal_anchor = re.compile(r"(^|\s)#" + re.escape(anchor) + r"(\s|$)")
    return bool(explicit_anchor.search(text) or literal_anchor.search(text))


def validate_outputs(handoff: dict[str, Any], skill_io: dict[str, Any], handoff_path: Path) -> None:
    aliases = skill_io.get("aliases", {})
    if not isinstance(aliases, dict):
        raise ValidationError("skill-io aliases debe ser un objeto")

    required = {canonical(str(skill), aliases) for skill in handoff["required_by_destination"]}
    outputs = {
        canonical(str(output["skill_id"]), aliases): output
        for output in handoff["outputs"]
    }

    missing = sorted(required - set(outputs))
    if missing:
        raise ValidationError(f"faltan outputs requeridos por skill_id: {', '.join(missing)}")

    base_dir = handoff_path.parent
    for skill_id, output in outputs.items():
        output_ref = str(output["output_ref"])
        file_part, anchor = output_ref.split("#", 1)
        markdown_path = (base_dir / file_part).resolve()
        if not anchor:
            raise ValidationError(f"{skill_id}: output_ref sin ancla: {output_ref}")
        if not anchor_exists(markdown_path, anchor):
            raise ValidationError(f"{skill_id}: ancla no encontrada: #{anchor} en {markdown_path}")


def validate_transition(handoff: dict[str, Any], skill_io: dict[str, Any], transition: str | None) -> None:
    if not transition:
        transition = handoff.get("transition")
    if not transition:
        return

    transitions = skill_io.get("transitions", {})
    if transition not in transitions:
        raise ValidationError(f"transicion no declarada en skill-io.md: {transition}")

    aliases = skill_io.get("aliases", {})
    expected = {canonical(skill, aliases) for skill in transitions[transition].get("required", [])}
    actual = {canonical(str(skill), aliases) for skill in handoff["required_by_destination"]}
    if expected != actual:
        raise ValidationError(
            "required_by_destination no coincide con skill-io para "
            f"{transition}: esperado {sorted(expected)}, recibido {sorted(actual)}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Venture Engine handoff v2 JSON file.")
    parser.add_argument("handoff", help="Path to handoff.json")
    parser.add_argument("--skill-io", default=str(DEFAULT_SKILL_IO), help="Path to contracts/skill-io.md")
    parser.add_argument("--transition", help="Optional transition key, e.g. 0->1")
    args = parser.parse_args()

    handoff_path = Path(args.handoff).resolve()
    try:
        handoff = load_json(handoff_path)
        skill_io = load_skill_io(Path(args.skill_io).resolve())
        validate_shape(handoff)
        validate_transition(handoff, skill_io, args.transition)
        validate_outputs(handoff, skill_io, handoff_path)
    except ValidationError as exc:
        print(f"FALLA: {exc}")
        return 1

    print("PASA: handoff valido")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
