#!/usr/bin/env python3
"""Builds Forestal MT product data artifacts from the Excel masters."""
from __future__ import annotations

import csv
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_DIR = ROOT / "products-data"
CATALOG_XLSX = PRODUCTS_DIR / "forestal-mt-products-catalogue-46-skus.xlsx"
RETAIL_XLSX = PRODUCTS_DIR / "forestal-mt-products-retail-presentations-and-pricing.xlsx"
WHOLESALE_XLSX = PRODUCTS_DIR / "forestal-mt-products-wholesale-presentations-and-pricing.xlsx"

CATALOG_JSON = PRODUCTS_DIR / "catalogue.json"
SKU_BASE_JSON = PRODUCTS_DIR / "sku-base.json"
SKU_PRESENTATIONS_JSON = PRODUCTS_DIR / "sku-presentations.json"
RETAIL_CSV = PRODUCTS_DIR / "retail.csv"
WHOLESALE_CSV = PRODUCTS_DIR / "wholesale.csv"

METADATA = OrderedDict(
    repository="forestal-mt-suite",
    owner="nerymurillohn",
    type="Brand and Product Data Repository",
    company="Forestal MT (Forestal Murillo Tejada S. de R.L. de C.V.)",
    country="Honduras",
    industry="Artisan Furniture Manufacturing",
)

CATALOG_HEADERS = (
    "SKU",
    "Product Name",
    "Seal",
    "Collection",
    "Botanical Source",
    "HS Code",
    "Part Used",
    "Product Description",
    "Ingredients",
    "Traditional Uses",
    "Processing Method",
    "Country of Origin",
    "Hero Image Reference",
    "Doc Reference",
)

RETAIL_HEADERS = [
    "SKU",
    "Product Name",
    "Collection",
    "Retail Presentation",
    "Presentation Type",
    "Measurement",
    "Unit",
    "Currency",
    "Price",
]

WHOLESALE_HEADERS = [
    "SKU",
    "Product Name",
    "Collection",
    "Wholesale Presentation",
    "Presentation Type",
    "Measurement",
    "Unit",
    "Currency",
    "Price",
]


def _load_rows(path: Path) -> Iterable[Dict[str, object]]:
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb.active
    header_row = next(ws.iter_rows(min_row=1, max_row=1, values_only=True))
    headers = [str(value).strip() if value else "" for value in header_row]
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not any(row):
            continue
        values = []
        for value in row:
            if isinstance(value, str):
                cleaned = value.replace("\u0007", "•")
                values.append(cleaned.strip())
            else:
                values.append(value)
        data = {headers[i]: values[i] for i in range(min(len(headers), len(values)))}
        yield data


def build_base_catalog() -> Dict[str, Dict[str, object]]:
    base: Dict[str, Dict[str, object]] = {}
    for row in _load_rows(CATALOG_XLSX):
        sku = str(row["SKU"]).strip()
        if not sku:
            continue
        if sku not in base:
            base[sku] = {
                "sku": sku,
                "product_name": row.get("Product Name", ""),
                "seal": row.get("Seal", ""),
                "collection": row.get("Collection", ""),
                "botanical_source": row.get("Botanical Source", ""),
                "hs_code": int(row["HS Code"]) if isinstance(row.get("HS Code"), (int, float)) else row.get("HS Code"),
                "part_used": row.get("Part Used", ""),
                "product_description": row.get("Product Description", ""),
                "ingredients": row.get("Ingredients", ""),
                "traditional_uses": row.get("Traditional Uses", ""),
                "processing_method": row.get("Processing Method", ""),
                "country_of_origin": row.get("Country of Origin", ""),
                "hero_image_reference": row.get("Hero Image Reference", ""),
                "doc_reference": row.get("Doc Reference", ""),
            }
        else:
            for key in CATALOG_HEADERS[1:]:
                normalized_key = {
                    "Product Name": "product_name",
                    "Seal": "seal",
                    "Collection": "collection",
                    "Botanical Source": "botanical_source",
                    "HS Code": "hs_code",
                    "Part Used": "part_used",
                    "Product Description": "product_description",
                    "Ingredients": "ingredients",
                    "Traditional Uses": "traditional_uses",
                    "Processing Method": "processing_method",
                    "Country of Origin": "country_of_origin",
                    "Hero Image Reference": "hero_image_reference",
                    "Doc Reference": "doc_reference",
                }[key]
                current = base[sku][normalized_key]
                new_value = row.get(key)
                if isinstance(new_value, str):
                    new_value = new_value.replace("\u0007", "•").strip()
                if current in (None, "") and new_value:
                    base[sku][normalized_key] = new_value
                elif new_value and current != new_value:
                    raise ValueError(f"Mismatch for {sku} field {normalized_key}: '{current}' vs '{new_value}'")
    return base


def _build_presentations(channel: str, headers: List[str], rows: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    for row in rows:
        sku = str(row.get("SKU", "")).strip()
        if not sku:
            continue
        measurement = row.get("Measurement")
        if isinstance(measurement, float) and measurement.is_integer():
            measurement = int(measurement)
        price = row.get("Price")
        if isinstance(price, float) and price.is_integer():
            price = int(price)
        items.append(
            {
                "sku": sku,
                "channel": channel,
                "presentation": row.get(headers[3], ""),
                "presentation_type": row.get("Presentation Type", ""),
                "measurement": measurement,
                "unit": row.get("Unit", ""),
                "currency": row.get("Currency", ""),
                "price": price,
            }
        )
    items.sort(key=lambda obj: (obj["sku"], obj["channel"], str(obj["presentation"])))
    return items


def write_csv(path: Path, headers: List[str], rows: Iterable[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({header: row.get(header) for header in headers})


def main() -> None:
    base = build_base_catalog()
    retail_rows = list(_load_rows(RETAIL_XLSX))
    wholesale_rows = list(_load_rows(WHOLESALE_XLSX))
    retail_presentations = _build_presentations("retail", RETAIL_HEADERS, retail_rows)
    wholesale_presentations = _build_presentations("wholesale", WHOLESALE_HEADERS, wholesale_rows)

    write_csv(RETAIL_CSV, RETAIL_HEADERS, retail_rows)
    write_csv(WHOLESALE_CSV, WHOLESALE_HEADERS, wholesale_rows)

    base_list = [base[sku] for sku in sorted(base.keys())]
    presentations = retail_presentations + wholesale_presentations

    for path, payload in (
        (SKU_BASE_JSON, base_list),
        (SKU_PRESENTATIONS_JSON, presentations),
    ):
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalogue_payload = OrderedDict(METADATA)
    catalogue_payload["generated_at"] = datetime.now(timezone.utc).isoformat()
    catalogue_payload["products"] = base_list
    catalogue_payload["presentations"] = presentations
    CATALOG_JSON.write_text(json.dumps(catalogue_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
