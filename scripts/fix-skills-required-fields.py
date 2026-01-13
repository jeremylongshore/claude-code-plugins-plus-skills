#!/usr/bin/env python3
"""
Ensure all SKILL.md files satisfy the required 2025 frontmatter fields.

This is a pragmatic bulk-fixer intended to make the repo pass
scripts/validate-skills-schema.py by ensuring required enterprise fields exist:
  - allowed-tools (CSV string)
  - version (semver)
  - author
  - license

It also normalizes unscoped 'Bash' -> 'Bash(cmd:*)' to avoid validator warnings.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


RE_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+")

DEFAULT_AUTHOR = "Jeremy Longshore <jeremy@intentsolutions.io>"
DEFAULT_LICENSE = "MIT"
DEFAULT_VERSION = "1.0.0"

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "archive",
    "backups",
    "000-docs",
    "consistency-reports",
    "notebooks",
    "workspace",
}


def _slug_words(slug: str) -> str:
    return slug.replace("_", "-").replace("-", " ").strip()


def _default_description(skill_name: str) -> str:
    words = _slug_words(skill_name)
    return (
        f"Configure and manage {words} workflows.\n\n"
        f"Use when working on {words} tasks or related integrations. "
        f"Trigger with phrases like \"{words}\", \"{words} setup\", or \"{words} troubleshooting\"."
    )


def _infer_allowed_tools(content: str) -> str:
    c = content.lower()
    tools: list[str] = ["Read", "Grep", "Glob"]

    if any(w in c for w in ["write", "edit", "modify", "refactor", "update", "create", "generate"]):
        tools = ["Read", "Write", "Edit", "Grep", "Glob"]

    if any(w in c for w in ["bash", "shell", "cli", "terminal", "command", "npm", "pnpm", "pip", "python", "git", "curl"]):
        if "Bash(cmd:*)" not in tools:
            tools.append("Bash(cmd:*)")

    return ", ".join(tools)


def _normalize_allowed_tools(value: Any, fallback: str) -> str:
    if isinstance(value, list):
        tools = ", ".join(str(t).strip() for t in value if str(t).strip())
    elif isinstance(value, str):
        tools = value.strip()
    else:
        tools = ""

    if not tools:
        tools = fallback

    # Normalize accidental quoting.
    tools = tools.strip().strip('"').strip("'")

    # Avoid unscoped Bash.
    parts = [p.strip() for p in tools.split(",") if p.strip()]
    normalized: list[str] = []
    for p in parts:
        if p == "Bash":
            normalized.append("Bash(cmd:*)")
        else:
            normalized.append(p)
    return ", ".join(normalized)


def _dump_frontmatter(fm: dict) -> str:
    # Stable key order: required fields first, then everything else in original order.
    ordered_keys = ["name", "description", "allowed-tools", "version", "author", "license"]
    out: list[str] = ["---"]

    def _emit_description(text: str) -> None:
        out.append("description: |")
        for line in text.splitlines():
            out.append(f"  {line}".rstrip())

    for key in ordered_keys:
        if key not in fm:
            continue
        val = fm[key]
        if key == "description":
            _emit_description(str(val))
        else:
            out.append(f"{key}: {val}")

    for key, val in fm.items():
        if key in ordered_keys:
            continue
        if isinstance(val, bool):
            out.append(f"{key}: {str(val).lower()}")
        elif isinstance(val, list):
            out.append(f"{key}:")
            for item in val:
                out.append(f"  - {item}")
        elif key == "description":
            _emit_description(str(val))
        else:
            out.append(f"{key}: {val}")

    out.append("---")
    return "\n".join(out)


def _load_frontmatter(raw: str) -> dict:
    if yaml is None:
        raise RuntimeError("pyyaml is required: run with .venv/bin/python or install pyyaml")
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter is not a YAML mapping")
    return data


def _should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return any(p in parts for p in EXCLUDED_DIRS) or any(p.startswith("skills-backup-") for p in path.parts)


def _iter_skill_files(repo_root: Path) -> list[Path]:
    results: list[Path] = []

    plugins_dir = repo_root / "plugins"
    if plugins_dir.exists():
        for p in plugins_dir.rglob("skills/*/SKILL.md"):
            if p.is_file() and not _should_skip(p):
                results.append(p)

    skills_dir = repo_root / "skills"
    if skills_dir.exists():
        for p in skills_dir.rglob("*/SKILL.md"):
            if p.is_file() and not _should_skip(p):
                results.append(p)

    return results


def fix_skill_file(path: Path, dry_run: bool) -> bool:
    content = path.read_text(encoding="utf-8")
    m = RE_FRONTMATTER.match(content)
    if not m:
        return False

    fm_raw, body = m.group(1), m.group(2)
    fm = _load_frontmatter(fm_raw)

    original = dict(fm)
    folder_name = path.parent.name

    fm.setdefault("name", folder_name)
    if not str(fm.get("description", "")).strip():
        fm["description"] = _default_description(str(fm["name"]))

    fallback_tools = _infer_allowed_tools(content)
    fm["allowed-tools"] = _normalize_allowed_tools(fm.get("allowed-tools"), fallback=fallback_tools)

    version = str(fm.get("version", "")).strip() or DEFAULT_VERSION
    if not RE_SEMVER.match(version):
        version = DEFAULT_VERSION
    fm["version"] = version

    fm.setdefault("author", DEFAULT_AUTHOR)
    fm.setdefault("license", DEFAULT_LICENSE)

    if fm == original:
        return False

    new_content = _dump_frontmatter(fm) + "\n" + body.lstrip()
    if not dry_run:
        path.write_text(new_content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix required SKILL.md frontmatter fields")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repo root (defaults to scripts/..).",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(__file__).resolve().parent.parent
    files = _iter_skill_files(repo_root)
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Found {len(files)} SKILL.md files")

    changed = 0
    for p in files:
        try:
            if fix_skill_file(p, dry_run=args.dry_run):
                changed += 1
        except Exception as e:
            print(f"ERROR: {p}: {e}", file=sys.stderr)
            return 1

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

