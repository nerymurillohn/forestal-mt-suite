# SDS/TDS Generator — Source Files Manifest

**Project:** sds-tds-generator
**Version:** 1.0.0
**Purpose:** Inventory of all repository files consumed by the document generator

---

## Overview

This manifest documents the **exact files** the SDS/TDS generator reads from the repository to produce print-ready documents. It serves as a dependency map and ensures no file is overlooked.

---

## Input Files (From Repository)

### Product Data (Primary Source)

| File | Purpose | Format | Size | SKUs |
|------|---------|--------|------|------|
| `products-data/sku-base.json` | Complete product specifications | JSON | 137 KB | 46 |
| `products-data/catalogue.json` | Full catalogue with descriptions | JSON | 195 KB | 46 |
| `products-data/data-manifest.json` | Asset references & checksums | JSON | 19 KB | 46 |

**Fields Used:**
- `sku` - Product identifier
- `product_name` - Official product name
- `collection` - Product line (Batana Oil, Traditional Herbs, etc.)
- `botanical_source` - Latin name for ingredient
- `hs_code` - Harmonized System tariff code
- `part_used` - Plant part (leaf, seed, kernel, etc.)
- `product_description` - Heritage narrative
- `ingredients` - Chemical composition
- `traditional_uses` - Ethnobotanical applications
- `processing_method` - Manufacturing steps
- `country_of_origin` - Honduras
- `seal` - Quality seal (Pure & Unrefined, etc.)

---

### Brand Guidelines

| File | Purpose | Sections Used |
|------|---------|---------------|
| `docs/brand/typography.md` | Document formatting rules | All 8 hierarchy levels, color codes, spacing |
| `docs/brand/colors.md` | Brand color palette | Forest Green #1F6D03, Leaf Green #52B006 |
| `docs/brand/voice.md` | Tone & messaging | Company narrative, brand values |
| `docs/brand/overview.md` | Company mission/vision | Slogan, promise, essence |

**Typography Specifications Used:**
- Level 1: Document Title (18pt, Forest Green, Bold, ALL CAPS)
- Level 2: Product Name (16pt, Leaf Green, Bold, Title Case)
- Level 3: Section Headers (14pt, Forest Green, Bold, ALL CAPS)
- Level 4-6: Subsections & labels (12pt, various weights)
- Line height: 1.5 for all text
- Spacing: 18pt before headers, 4pt after

---

### Company Information

| File | Purpose | Fields Used |
|------|---------|-------------|
| `docs/company/company-profile.md` | Legal entity details | Legal name, RTN, location |
| `docs/company/business-hours.md` | Contact information | Operating hours |
| `docs/company/shipping.md` | Logistics details | Shipping methods, lead times |
| `docs/company/authenticity-chain.md` | Supply chain | Sourcing transparency |

**Company Data Used:**
- Legal Name: Forestal Murillo Tejada S. de R.L. de C.V.
- Brand Name: Forestal MT
- RTN: 08019009246972
- Location: Barrio Arriba, San Francisco de la Paz, Olancho, Honduras
- Year Established: 2009

---

### Templates & Assets

| File | Purpose | Size | Format |
|------|---------|------|--------|
| `assets/templates/official-letterhead/docx/forestal-mt-letterhead.docx` | Base template with header/footer | 2.5 MB | DOCX |
| `assets/templates/official-letterhead/pdf/forestal-mt-letterhead.pdf` | Reference for QA | 69 KB | PDF |
| `assets/logos/forestal-mt-logo-primary.png` | Logo for embedding | 131 KB | PNG |
| `assets/fonts/source/CormorantGaramond/` | Typography assets | Various | TTF |

**Template Usage:**
1. Clone `forestal-mt-letterhead.docx` as base
2. Preserve embedded header/footer graphics
3. Apply typography styles to body content
4. Export to DOCX and PDF

---

### Collection Documentation

| File | Purpose | Data Points |
|------|---------|-------------|
| `docs/collections/batana-oil.md` | Batana Oil collection info | Tagline, sourcing, quality seal |
| `docs/collections/stingless-bee-honey.md` | Honey collection info | Species, traditional significance |
| `docs/collections/traditional-herbs.md` | Herbs collection info | Heritage, wildcrafting practices |

**Collection Metadata Used:**
- Tagline (e.g., "Ancestral Miskito Elixir")
- Sourcing location (La Mosquitia, Honduras)
- Quality seal (Pure & Unrefined, Raw & Unfiltered, etc.)
- Primary uses (hair care, wellness, traditional medicine)

---

## File Dependency Graph

```
┌─────────────────────────────────────────────────────────────┐
│                  SDS/TDS Generator                          │
└─────────────────────────────────────────────────────────────┘
                        ↓
    ┌──────────────────────────────────────────────┐
    │                                              │
┌───▼──────┐  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐
│ Products │  │  Brand   │  │ Company  │  │Templates │
│   Data   │  │  Guides  │  │   Info   │  │ & Assets │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
    │             │             │             │
    ├─ sku-base.json          company-       letterhead.docx
    ├─ catalogue.json         profile.md     letterhead.pdf
    └─ data-manifest.json     business-      logos/
                               hours.md       fonts/
         typography.md
         colors.md
         voice.md
         overview.md

         batana-oil.md
         stingless-bee-honey.md
         traditional-herbs.md
```

---

## Data Flow

### SDS Generation
```
1. Load product from sku-base.json
2. Load company from company-profile.md
3. Clone letterhead.docx template
4. Apply typography styles from typography.md
5. Populate 16 GHS sections:
   - Section 1: product_name, sku, botanical_source, company info
   - Section 3: ingredients, botanical_source, part_used
   - Section 9: Physical properties (inferred from product type)
   - Section 14: hs_code for transport classification
   - Section 15: country_of_origin for regulatory compliance
6. Save as {SKU}-SDS.docx
7. Convert to {SKU}-SDS.pdf
```

### TDS Generation
```
1. Load product from sku-base.json
2. Load collection from docs/collections/{collection}.md
3. Clone letterhead.docx template
4. Apply typography styles from typography.md
5. Populate TDS sections:
   - Product Identity: sku, product_name, collection, seal, botanical_source
   - Description: product_description (heritage narrative)
   - Traditional Uses: traditional_uses (bulleted list)
   - Processing Method: processing_method (step-by-step)
   - Technical Specs: ingredients, hs_code, part_used
   - Regulatory: hs_code, country_of_origin
6. Save as {SKU}-TDS.docx
7. Convert to {SKU}-TDS.pdf
```

---

## Missing Data Points (To Be Added)

### For SDS Compliance

| Section | Required Data | Current Status | Solution |
|---------|---------------|----------------|----------|
| Section 9 | Physical properties (pH, viscosity, density) | ❌ Not in JSON | Add to Excel master or use defaults by product type |
| Section 11 | Toxicological data | ❌ Not available | Use "No data available" or "Not classified" |
| Section 12 | Ecological data | ❌ Not available | Add "Biodegradable, plant-based" for all products |
| Section 14 | UN numbers for transport | ❌ Not in JSON | Map HS codes to UN numbers or use "Not regulated" |
| Section 15 | OSHA/EPA regulations | ❌ Not available | Add "Not regulated under OSHA/EPA" for cosmetics |

### For TDS Enhancement

| Section | Desired Data | Current Status | Solution |
|---------|--------------|----------------|----------|
| Microbiological specs | Total plate count, E. coli | ❌ Not available | Add to quality standards section in Excel |
| Shelf life | Storage duration | ❌ Not available | Add "24 months from manufacture date" default |
| Certifications | Organic, Fair Trade, etc. | ❌ Not available | Add certifications field to Excel |
| Applications | Formulation guidance | ⚠️ Partial (traditional_uses) | Expand with dosage, blending recommendations |

---

## Validation Rules

### Required Fields (Must Not Be Null)

```python
REQUIRED_FIELDS = [
    "sku",                    # Product identifier
    "product_name",           # Official name
    "botanical_source",       # Latin name
    "ingredients",            # Composition
    "country_of_origin",      # Manufacturing location
    "hs_code",               # Tariff classification
]
```

### Optional Fields (Graceful Degradation)

```python
OPTIONAL_FIELDS = [
    "seal",                   # Default to "Traditional Quality"
    "processing_method",      # Use "Traditional methods" if missing
    "traditional_uses",       # Skip section if missing
    "part_used",             # Default to "whole plant"
]
```

### Typography Validation

```python
TYPOGRAPHY_CHECKS = [
    ("title_font_size", 18),           # Document title
    ("title_color", "#1F6D03"),        # Forest Green
    ("header_font_size", 14),          # Section headers
    ("header_color", "#1F6D03"),       # Forest Green
    ("body_font_size", 12),            # Body text
    ("line_height", 1.5),              # All text
]
```

---

## Version Control

### File Change Monitoring

Track changes to source files that trigger document regeneration:

```bash
# Monitor product data
git diff products-data/sku-base.json

# Monitor typography changes
git diff docs/brand/typography.md

# Monitor company info
git diff docs/company/company-profile.md

# Trigger regeneration if any changed
python projects/sds-tds-generator/generator.py
```

### Regeneration Triggers

| Change Type | Affected Documents | Action |
|-------------|-------------------|--------|
| Product data updated | Specific SKU's SDS/TDS | Regenerate that SKU only |
| Typography.md changed | All documents | Regenerate all 184 files |
| Company info changed | All documents | Regenerate all 184 files |
| Template changed | All documents | Regenerate all 184 files |

---

## Quality Assurance Checklist

### Pre-Generation
- [ ] All 46 SKUs present in sku-base.json
- [ ] No null values in required fields
- [ ] Typography.md specifications are current
- [ ] Company-profile.md has current contact info
- [ ] Letterhead template is up-to-date

### Post-Generation
- [ ] 184 files created (46 SKUs × 2 types × 2 formats)
- [ ] All DOCX files open without errors
- [ ] All PDFs render correctly
- [ ] Typography matches typography.md
- [ ] Company info is accurate
- [ ] Product names match SKU codes

### Visual Inspection (Sample)
- [ ] Letterhead header/footer visible
- [ ] Forest Green #1F6D03 applied to titles
- [ ] Leaf Green #52B006 applied to product names
- [ ] Garamond/Cormorant Garamond font used
- [ ] Line spacing is 1.5
- [ ] Section spacing is 18pt before headers
- [ ] Bullet lists have proper indentation

---

## Integration Points

### Automation Scripts

| Script | Purpose | Input Files |
|--------|---------|-------------|
| `tools/build_product_data.py` | Generate JSON from Excel | Excel masters |
| `tools/verify_product_assets.py` | Validate asset references | data-manifest.json, hero images |
| `projects/sds-tds-generator/generator.py` | Generate documents | All listed above |
| `tools/generate_inventory.py` | Update repo metadata | All repository files |

### CI/CD Pipeline

```yaml
# .github/workflows/validate-repo.yml
- name: Generate sample documents
  run: |
    cd projects/sds-tds-generator
    python generator.py --sku FMT-BO-RBO-2025 --format pdf
    # Verify PDF created successfully
    test -f outputs/sds/FMT-BO-RBO-2025-SDS.pdf
    test -f outputs/tds/FMT-BO-RBO-2025-TDS.pdf
```

---

## Usage Examples

### Generate All Documents
```bash
cd projects/sds-tds-generator
python generator.py
# Output: 184 files in outputs/
```

### Generate Single SKU
```bash
python generator.py --sku FMT-BO-RBO-2025
# Output: 4 files (2 doc types × 2 formats)
```

### Generate Only SDS
```bash
python generator.py --doc-type sds
# Output: 92 files (46 SKUs × 2 formats)
```

### Generate DOCX Only
```bash
python generator.py --format docx
# Output: 92 files (46 SKUs × 2 doc types)
```

### Test Typography Changes
```bash
# Edit typography specifications
vim ../../docs/brand/typography.md

# Regenerate one SKU to test
python generator.py --sku FMT-BO-RBO-2025 --format pdf

# Review output
open outputs/sds/FMT-BO-RBO-2025-SDS.pdf
```

---

## File Locations Summary

```
Repository Root: /home/user/forestal-mt-suite/

Input Files:
  products-data/sku-base.json
  products-data/catalogue.json
  products-data/data-manifest.json
  docs/brand/typography.md
  docs/brand/colors.md
  docs/brand/voice.md
  docs/brand/overview.md
  docs/company/company-profile.md
  docs/company/business-hours.md
  docs/company/shipping.md
  docs/company/authenticity-chain.md
  docs/collections/batana-oil.md
  docs/collections/stingless-bee-honey.md
  docs/collections/traditional-herbs.md
  assets/templates/official-letterhead/docx/forestal-mt-letterhead.docx
  assets/templates/official-letterhead/pdf/forestal-mt-letterhead.pdf
  assets/logos/forestal-mt-logo-primary.png
  assets/fonts/source/CormorantGaramond/

Project Files:
  projects/sds-tds-generator/generator.py
  projects/sds-tds-generator/templates/sds_template.py
  projects/sds-tds-generator/templates/tds_template.py
  projects/sds-tds-generator/styles/typography.py
  projects/sds-tds-generator/requirements.txt

Output Files:
  projects/sds-tds-generator/outputs/sds/*.docx
  projects/sds-tds-generator/outputs/sds/*.pdf
  projects/sds-tds-generator/outputs/tds/*.docx
  projects/sds-tds-generator/outputs/tds/*.pdf
```

---

**Manifest Version:** 1.0.0
**Created:** 2025-11-11
**Purpose:** Document all repository dependencies for SDS/TDS generator
**Status:** Complete
