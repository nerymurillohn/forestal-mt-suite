# Product Data Changelog

All notable changes to product data will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-11-11

### Added
- Initial release of product data with 46 SKUs
- 3 product collections: Batana Oil, Stingless Bee Honey, Traditional Herbs
- Complete hero images for all products (46/46)
- Documentation for all collections
- Data manifest with metadata and checksums

### Data Structure
- `sku-base.json`: 46 products with complete specifications
- `catalogue.json`: Full catalogue with pricing and variants
- `data-manifest.json`: Metadata, checksums, and cross-references
- `retail.csv`: Retail pricing for all products
- `wholesale.csv`: Wholesale pricing for all products

### Validation
- Industry classification corrected to "Traditional Botanical Products"
- All HS codes validated (6-10 digits)
- All botanical names validated (Latin binomial nomenclature)
- Country of origin: Honduras (all products)

---

## Version Numbering Guidelines

Product data follows **Semantic Versioning (MAJOR.MINOR.PATCH)**:

- **MAJOR**: Breaking changes (SKU format changes, schema breaking changes, removal of products)
- **MINOR**: Backward-compatible additions (new products, new collections, new fields)
- **PATCH**: Backward-compatible fixes (price updates, typo corrections, metadata updates)

### Examples

**MAJOR (1.0.0 → 2.0.0)**:
- Change SKU format from `FMT-XX-XXX-2025` to new format
- Remove entire product collection
- Breaking schema changes

**MINOR (1.0.0 → 1.1.0)**:
- Add new product to existing collection
- Add new product collection
- Add new optional field to product schema

**PATCH (1.0.0 → 1.0.1)**:
- Update product prices
- Fix typos in product descriptions
- Update hero image without changing SKU
- Correct botanical name spelling

---

## Changelog Entry Template

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- List of new products, collections, or fields

### Changed
- List of modifications to existing data

### Deprecated
- List of features/products being phased out

### Removed
- List of products or fields removed

### Fixed
- List of bug fixes or corrections

### Security
- List of security-related changes
```

---

## How to Update Version

1. **Determine version bump type** (MAJOR, MINOR, or PATCH)
2. **Update `products-data/data-manifest.json`**:
   ```json
   {
     "version": "1.1.0",
     ...
   }
   ```
3. **Add entry to this CHANGELOG.md** with changes
4. **Run tests**: `pytest tests/ -v`
5. **Regenerate inventory**: `python tools/generate_inventory.py`
6. **Commit with version tag**:
   ```bash
   git add products-data/ CHANGELOG.md
   git commit -m "Release: product data v1.1.0"
   git tag -a v1.1.0 -m "Product data version 1.1.0"
   git push origin main --tags
   ```

---

## Audit Trail

This changelog provides:
- **Historical tracking** of all data changes
- **Compliance documentation** for regulatory requirements
- **Rollback information** for reverting to previous versions
- **Impact assessment** for downstream systems
- **Communication tool** for stakeholders

**Last Updated**: 2025-11-11
