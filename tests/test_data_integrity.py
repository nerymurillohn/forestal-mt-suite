#!/usr/bin/env python3
"""Basic data integrity tests for Forestal MT Suite."""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_data_manifest_exists():
    """Verify data-manifest.json exists and is valid JSON."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"
    assert manifest_path.exists(), "data-manifest.json not found"

    with open(manifest_path) as f:
        data = json.load(f)

    assert "skus" in data, "manifest missing 'skus' key"
    assert isinstance(data["skus"], list), "skus should be a list"
    assert len(data["skus"]) == 46, f"Expected 46 SKUs, found {len(data['skus'])}"


def test_all_hero_images_exist():
    """Verify all hero images referenced in manifest exist."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)

    missing_images = []
    for sku_entry in manifest["skus"]:
        hero_path = ROOT / sku_entry["hero_image"]["path"]
        if not hero_path.exists():
            missing_images.append(sku_entry["hero_image"]["path"])

    assert len(missing_images) == 0, f"Missing hero images: {missing_images}"


def test_all_doc_references_exist():
    """Verify all documentation references in manifest exist."""
    manifest_path = ROOT / "products-data" / "data-manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)

    missing_docs = []
    for sku_entry in manifest["skus"]:
        doc_path = ROOT / sku_entry["doc_reference"]
        if not doc_path.exists():
            missing_docs.append(sku_entry["doc_reference"])

    assert len(missing_docs) == 0, f"Missing doc references: {missing_docs}"


def test_csv_files_parseable():
    """Verify CSV files are valid and parseable."""
    import csv

    retail_csv = ROOT / "products-data" / "retail.csv"
    wholesale_csv = ROOT / "products-data" / "wholesale.csv"

    # Test retail CSV
    with open(retail_csv) as f:
        reader = csv.DictReader(f)
        retail_rows = list(reader)

    assert len(retail_rows) > 0, "retail.csv has no data rows"
    assert "SKU" in retail_rows[0], "retail.csv missing SKU column"

    # Test wholesale CSV
    with open(wholesale_csv) as f:
        reader = csv.DictReader(f)
        wholesale_rows = list(reader)

    assert len(wholesale_rows) > 0, "wholesale.csv has no data rows"
    assert "SKU" in wholesale_rows[0], "wholesale.csv missing SKU column"


def test_json_files_parseable():
    """Verify all JSON files are valid and parseable."""
    json_files = [
        "products-data/catalogue.json",
        "products-data/sku-base.json",
        "products-data/sku-presentations.json",
        "products-data/data-manifest.json",
    ]

    for json_file in json_files:
        json_path = ROOT / json_file
        assert json_path.exists(), f"{json_file} not found"

        with open(json_path) as f:
            data = json.load(f)

        assert data is not None, f"{json_file} is empty or invalid"


def test_hero_image_naming_convention():
    """Verify all hero images follow the naming convention."""
    import re

    hero_images = (ROOT / "assets/products-images").rglob("hero/*.png")

    # Expected pattern: fmt-[collection]-[code]-2025-hero.png
    pattern = re.compile(r"^fmt-[a-z]{2,4}-[a-z]{2,4}-2025-hero\.png$")

    invalid_names = []
    for img in hero_images:
        if not pattern.match(img.name):
            invalid_names.append(img.name)

    assert len(invalid_names) == 0, f"Invalid naming: {invalid_names}"
