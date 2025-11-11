#!/usr/bin/env python3
"""Test data versioning and changelog requirements."""
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_data_manifest_has_version():
    """Verify data-manifest.json includes version field."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"

    with open(manifest_path) as f:
        manifest = json.load(f)

    assert "version" in manifest, "data-manifest.json missing 'version' field"

    version = manifest["version"]
    assert isinstance(version, str), "version must be a string"
    assert len(version) > 0, "version cannot be empty"


def test_version_follows_semver():
    """Verify version follows semantic versioning (MAJOR.MINOR.PATCH)."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"

    with open(manifest_path) as f:
        manifest = json.load(f)

    version = manifest.get("version", "")

    # Semantic versioning pattern: MAJOR.MINOR.PATCH (e.g., 1.0.0, 1.2.3)
    semver_pattern = re.compile(r'^\d+\.\d+\.\d+$')

    assert semver_pattern.match(version), \
        f"Version '{version}' does not follow semantic versioning (MAJOR.MINOR.PATCH)"


def test_changelog_exists():
    """Verify CHANGELOG.md exists in repository root."""
    changelog_path = ROOT / "CHANGELOG.md"

    assert changelog_path.exists(), "CHANGELOG.md not found in repository root"

    # Verify file has content
    with open(changelog_path) as f:
        content = f.read()

    assert len(content) > 100, "CHANGELOG.md appears to be empty or too short"


def test_changelog_has_version_entry():
    """Verify CHANGELOG.md has entry for current version."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"
    changelog_path = ROOT / "CHANGELOG.md"

    with open(manifest_path) as f:
        manifest = json.load(f)

    current_version = manifest.get("version", "")

    with open(changelog_path) as f:
        changelog = f.read()

    # Look for version entry like "## [1.0.0]"
    version_pattern = rf'\[{re.escape(current_version)}\]'

    assert re.search(version_pattern, changelog), \
        f"CHANGELOG.md missing entry for version {current_version}"


def test_changelog_format():
    """Verify CHANGELOG.md follows Keep a Changelog format."""
    changelog_path = ROOT / "CHANGELOG.md"

    with open(changelog_path) as f:
        changelog = f.read()

    # Check for required sections
    required_headers = [
        "# Product Data Changelog",
        "## [Unreleased]",
    ]

    for header in required_headers:
        assert header in changelog, f"CHANGELOG.md missing required header: {header}"

    # Check for semantic versioning in entries
    version_entries = re.findall(r'## \[(\d+\.\d+\.\d+)\]', changelog)

    assert len(version_entries) > 0, "CHANGELOG.md has no versioned entries"
