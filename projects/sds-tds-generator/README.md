# SDS/TDS Document Generator

Automated generation of Safety Data Sheets (SDS) and Technical Data Sheets (TDS) for all Forestal MT products using the repository as single source of truth.

---

## Status: Blueprint Phase

This project is currently in the **planning stage**. The blueprint and source files manifest have been created and are ready for implementation.

---

## Project Documents

| Document | Purpose | Status |
|----------|---------|--------|
| **[sds-tds-generator-blueprint.md](sds-tds-generator-blueprint.md)** | Complete implementation plan with 7 phases | ✓ Complete |
| **[source-files-manifest.md](source-files-manifest.md)** | Inventory of all input files from repository | ✓ Complete |
| **README.md** | This file - project overview | ✓ Complete |

---

## What This Generator Will Do

### Input (From Repository)
- ✓ 46 SKUs from `products-data/sku-base.json`
- ✓ Typography specs from `docs/brand/typography.md`
- ✓ Company info from `docs/company/company-profile.md`
- ✓ Letterhead template from `assets/templates/official-letterhead/`
- ✓ Brand fonts from `assets/fonts/`

### Process
1. Clone official letterhead template (DOCX)
2. Apply brand typography (Garamond, colors, spacing)
3. Populate SDS sections (16 GHS-compliant sections)
4. Populate TDS sections (technical specifications)
5. Export to DOCX and PDF formats

### Output
- **184 print-ready documents**
  - 46 SKUs × 2 document types (SDS + TDS) × 2 formats (DOCX + PDF)
  - Located in `outputs/sds/` and `outputs/tds/`
  - 100% brand-compliant typography
  - Professional, regulatory-ready

---

## Quick Start (When Implemented)

```bash
# Install dependencies
pip install -r requirements.txt

# Generate all documents
python generator.py

# Generate specific SKU
python generator.py --sku FMT-BO-RBO-2025

# Generate only SDS documents
python generator.py --doc-type sds

# Generate only DOCX format
python generator.py --format docx
```

---

## Implementation Timeline

| Phase | Task | Time | Status |
|-------|------|------|--------|
| **Phase 1** | Project setup & dependencies | 2-3 hrs | ⏳ Not started |
| **Phase 2** | Typography system | 1-2 hrs | ⏳ Not started |
| **Phase 3** | Template system | 2-3 hrs | ⏳ Not started |
| **Phase 4** | Data integration | 1-2 hrs | ⏳ Not started |
| **Phase 5** | Bulk generation | 1 hr | ⏳ Not started |
| **Phase 6** | Quality assurance | 1 hr | ⏳ Not started |
| **Phase 7** | Documentation | 1 hr | ⏳ Not started |
| **Total** | **9-13 hours** | | |

---

## Business Value

### Time Savings
- **Before:** 2-4 hours per product × 46 SKUs = **92-184 hours**
- **After:** 5 minutes for all 46 products
- **Savings:** ~180 hours (**$9,000-18,000 at $50/hr**)

### Quality Improvements
- ✓ 100% brand consistency (typography, colors, layout)
- ✓ Zero human error (automated data population)
- ✓ Instant updates (edit JSON → regenerate all docs)
- ✓ Regulatory compliance (GHS format, complete sections)

### Strategic Benefits
- ✓ Faster partner onboarding (instant document delivery)
- ✓ Professional credibility (polished, consistent docs)
- ✓ Scalability (add products → auto-generate docs)
- ✓ Export readiness (documents ready for customs, compliance)

**Estimated ROI:** $25K-50K/year

---

## Technical Stack

### Core Dependencies
```
python-docx>=0.8.11         # DOCX creation & manipulation
docx2pdf>=0.1.8             # PDF export
openpyxl>=3.1.0             # Excel parsing (already installed)
pyyaml>=6.0                 # YAML frontmatter parsing
pillow>=10.0.0              # Image handling
tqdm>=4.66.0                # Progress bars
click>=8.1.0                # CLI interface
```

### System Requirements
- Python 3.10+ (3.11 recommended)
- Cormorant Garamond font installed (from `assets/fonts/`)
- PDF engine: docx2pdf (Windows/macOS) or pandoc (Linux)

---

## Architecture

```
Repository (Source of Truth)
    │
    ├── Product Data (JSON)
    ├── Typography Specs (MD)
    ├── Company Info (MD)
    ├── Templates (DOCX)
    └── Fonts & Assets
         ↓
    Generator (Python)
         │
         ├── Load & Parse Data
         ├── Clone Template
         ├── Apply Typography
         ├── Populate Sections
         └── Export DOCX + PDF
              ↓
         Outputs
         │
         ├── outputs/sds/ (92 files)
         └── outputs/tds/ (92 files)
```

---

## Example Output

### SDS Document Structure (16 Sections)
1. Identification - Product name, SKU, company info
2. Hazard Identification - GHS classification
3. Composition/Ingredients - Botanical source, ingredients
4. First-Aid Measures - Emergency procedures
5. Fire-Fighting Measures - Extinguishing methods
6. Accidental Release Measures - Spill cleanup
7. Handling and Storage - Safe practices
8. Exposure Controls/PPE - Protective equipment
9. Physical/Chemical Properties - Appearance, pH, etc.
10. Stability and Reactivity - Chemical stability
11. Toxicological Information - Health effects
12. Ecological Information - Environmental impact
13. Disposal Considerations - Waste disposal
14. Transport Information - Shipping classification
15. Regulatory Information - Compliance status
16. Other Information - Revision date, sources

### TDS Document Structure (10 Sections)
1. Product Identity - Name, SKU, botanical source
2. Product Description - Heritage narrative
3. Technical Specifications - Physical properties
4. Quality Standards - Purity, testing
5. Traditional Uses - Ethnobotanical applications
6. Processing Method - Manufacturing steps
7. Storage & Shelf Life - Conditions, duration
8. Regulatory Compliance - HS code, certifications
9. Applications - Usage guidelines
10. Company Information - Contact details

---

## Next Steps

1. **Review Blueprint** - Read `sds-tds-generator-blueprint.md`
2. **Confirm Requirements** - Verify SDS/TDS sections with regulatory team
3. **Begin Phase 1** - Set up project structure
4. **Generate Test Document** - Create one SKU to validate approach
5. **Iterate & Deploy** - Refine and generate all 184 documents

---

## Questions?

For detailed implementation steps, see:
- **[Blueprint](sds-tds-generator-blueprint.md)** - Full technical specification
- **[Source Files Manifest](source-files-manifest.md)** - Input file inventory
- **Main Repository README** - `../../README.md`

---

**Project Status:** Blueprint Complete, Ready for Implementation
**Created:** 2025-11-11
**Version:** 1.0.0
