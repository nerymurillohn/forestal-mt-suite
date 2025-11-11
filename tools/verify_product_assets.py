#!/usr/bin/env python3
"""Validates Forestal MT product metadata and asset references."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_DIR = ROOT / "products-data"
MANIFEST_PATH = PRODUCTS_DIR / "data-manifest.json"
CATALOG_PATH = PRODUCTS_DIR / "catalogue.json"


def _hash_file(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), hashlib.sha256(data).hexdigest()


def main() -> int:
    errors: list[str] = []
    manifest = json.loads(MANIFEST_PATH.read_text())
    catalogue = json.loads(CATALOG_PATH.read_text())

    catalogue_file = ROOT / manifest["catalogue_file"]["path"]
    if not catalogue_file.is_file():
        errors.append(f"Missing catalogue Excel file: {catalogue_file}")

    manifest_skus = {entry["sku"] for entry in manifest["skus"]}
    catalogue_skus = {prod["sku"] for prod in catalogue["products"]}
    if manifest_skus != catalogue_skus:
        missing = manifest_skus - catalogue_skus
        extra = catalogue_skus - manifest_skus
        if missing:
            errors.append(f"Catalogue missing SKUs: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"Catalogue has extra SKUs: {', '.join(sorted(extra))}")

    for entry in manifest["skus"]:
        hero_rel = entry["hero_image"]["path"]
        hero_path = ROOT / hero_rel
        if not hero_path.is_file():
            errors.append(f"Missing hero image for {entry['sku']}: {hero_rel}")
            continue
        length, digest = _hash_file(hero_path)
        expected_len = entry["hero_image"].get("bytes")
        if isinstance(expected_len, int) and expected_len != length:
            errors.append(f"Byte mismatch for {hero_rel}: {length} != {expected_len}")
        expected_digest = entry["hero_image"].get("sha256")
        if expected_digest and expected_digest.lower() != digest.lower():
            errors.append(f"SHA mismatch for {hero_rel}: {digest} != {expected_digest}")
        doc_rel = entry.get("doc_reference")
        if doc_rel:
            doc_path = ROOT / doc_rel
            if not doc_path.is_file():
                errors.append(f"Missing doc reference for {entry['sku']}: {doc_rel}")

    if errors:
        for line in errors:
            print(line)
        return 1
    print("All product assets verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
