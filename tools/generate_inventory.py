#!/usr/bin/env python3
"""Generates repository inventory and syncs documentation blocks."""
from __future__ import annotations

import hashlib
import os
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
INFO_PATH = ROOT / "REPOSITORY_INFO.md"
INVENTORY_PATH = ROOT / "INVENTORY.md"

SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    ".idea",
    ".vscode",
}
SKIP_FILES = {".DS_Store", "Thumbs.db"}

SNAPSHOT_START = "<!-- AUTO-REPO-SNAPSHOT:START -->"
SNAPSHOT_END = "<!-- AUTO-REPO-SNAPSHOT:END -->"
STRUCTURE_START = "<!-- AUTO-REPO-STRUCTURE:START -->"
STRUCTURE_END = "<!-- AUTO-REPO-STRUCTURE:END -->"


def human_bytes(num: int) -> str:
    step = 1024.0
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(num)
    for unit in units:
        if value < step or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"
        value /= step
    return f"{value:.1f} TB"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def collect_inventory():
    top_summary: Dict[str, Dict[str, int]] = defaultdict(lambda: {"dirs": 0, "files": 0, "bytes": 0})
    top_summary.setdefault(".", {"dirs": 0, "files": 0, "bytes": 0})
    entries: List[Dict[str, str]] = []
    total_dirs = 0
    total_files = 0
    total_bytes = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = Path(dirpath).relative_to(ROOT)
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if rel_dir != Path('.'):
            parts = rel_dir.parts
            top = parts[0]
            _summary = top_summary.setdefault(top, {"dirs": 0, "files": 0, "bytes": 0})
            if len(parts) > 1:
                _summary["dirs"] += 1
            total_dirs += 1
        for filename in filenames:
            if filename in SKIP_FILES:
                continue
            file_path = Path(dirpath) / filename
            rel_path = file_path.relative_to(ROOT)
            parts = rel_path.parts
            if len(parts) == 1:
                top = "."
            else:
                top = parts[0]
            summary = top_summary.setdefault(top, {"dirs": 0, "files": 0, "bytes": 0})
            stat = file_path.stat()
            size = stat.st_size
            summary["files"] += 1
            summary["bytes"] += size
            total_files += 1
            total_bytes += size
            entries.append(
                {
                    "path": rel_path.as_posix(),
                    "size": size,
                    "size_h": human_bytes(size),
                    "modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "sha256": sha256_file(file_path),
                }
            )

    entries.sort(key=lambda item: item["path"].lower())
    timestamp = datetime.now(timezone.utc)
    return {
        "top_summary": top_summary,
        "entries": entries,
        "total_dirs": total_dirs,
        "total_files": total_files,
        "total_bytes": total_bytes,
        "timestamp": timestamp,
    }


def replace_block(path: Path, start_marker: str, end_marker: str, new_body: str) -> None:
    content = path.read_text(encoding="utf-8")
    if start_marker not in content or end_marker not in content:
        raise ValueError(f"Markers {start_marker} / {end_marker} not found in {path}")
    start_idx = content.index(start_marker) + len(start_marker)
    end_idx = content.index(end_marker, start_idx)
    new_section = "\n" + new_body.strip() + "\n"
    updated = content[:start_idx] + new_section + content[end_idx:]
    path.write_text(updated, encoding="utf-8")


def build_snapshot(summary: Dict[str, Dict[str, int]], total_dirs: int, total_files: int, total_bytes: int, timestamp: datetime) -> str:
    lines = [f"_Last updated: {timestamp.strftime('%Y-%m-%d %H:%M:%S')} UTC_", ""]
    lines.append("| Top-Level | Subdirs | Files | Size |")
    lines.append("| --- | ---: | ---: | ---: |")

    keys = sorted(k for k in summary.keys() if k != ".")
    if summary["."].get("files"):
        keys = ["."] + keys
    total_subdirs = sum(summary[k]["dirs"] for k in summary if k != ".")

    for key in keys:
        data = summary[key]
        label = "./ (root)" if key == "." else f"{key}/"
        lines.append(
            f"| {label} | {data['dirs']:,} | {data['files']:,} | {human_bytes(data['bytes'])} |"
        )

    lines.append(
        f"| **Total** | **{total_subdirs:,}** | **{total_files:,}** | **{human_bytes(total_bytes)}** |"
    )
    lines.append("")
    lines.append("See [`INVENTORY.md`](INVENTORY.md) for the complete file listing.")
    return "\n".join(lines)


def build_structure_block(summary: Dict[str, Dict[str, int]]) -> str:
    dirs = sorted(
        [p.name for p in ROOT.iterdir() if p.is_dir() and p.name not in SKIP_DIRS],
        key=str.lower,
    )
    files = sorted(
        [p.name for p in ROOT.iterdir() if p.is_file() and p.name not in SKIP_FILES],
        key=str.lower,
    )
    tree_items: List[str] = []
    for name in dirs:
        data = summary.get(name, {"dirs": 0, "files": 0, "bytes": 0})
        tree_items.append(f"{name}/ (dirs: {data['dirs']:,}, files: {data['files']:,}, size: {human_bytes(data['bytes'])})")
    for fname in files:
        fsize = human_bytes((ROOT / fname).stat().st_size)
        tree_items.append(f"{fname} ({fsize})")

    lines = ["."]
    for idx, entry in enumerate(tree_items):
        connector = "\u2514\u2500\u2500" if idx == len(tree_items) - 1 else "\u251c\u2500\u2500"
        lines.append(f"{connector} {entry}")
    return "\n".join(lines)


def write_inventory_file(entries: List[Dict[str, str]], totals: Dict[str, int], timestamp: datetime) -> None:
    header = ["# Repository Inventory", "", f"Generated: {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')}"]
    header.append(f"Total directories: {totals['dirs']:,}")
    header.append(f"Total files: {totals['files']:,}")
    header.append(f"Total size: {human_bytes(totals['bytes'])}")
    header.extend(["", "## File Listing", "", "| # | Path | Size | Modified (UTC) | SHA-256 |", "| ---: | --- | ---: | --- | --- |"])

    for idx, entry in enumerate(entries, start=1):
        header.append(
            f"| {idx} | `{entry['path']}` | {entry['size_h']} | {entry['modified']} | `{entry['sha256']}` |"
        )

    INVENTORY_PATH.write_text("\n".join(header) + "\n", encoding="utf-8")


def main() -> None:
    data = collect_inventory()
    snapshot = build_snapshot(data["top_summary"], data["total_dirs"], data["total_files"], data["total_bytes"], data["timestamp"])
    replace_block(README_PATH, SNAPSHOT_START, SNAPSHOT_END, snapshot)
    structure = build_structure_block(data["top_summary"])
    replace_block(INFO_PATH, STRUCTURE_START, STRUCTURE_END, f"```\n{structure}\n```")
    write_inventory_file(
        data["entries"],
        {"dirs": data["total_dirs"], "files": data["total_files"], "bytes": data["total_bytes"]},
        data["timestamp"],
    )


if __name__ == "__main__":
    main()
