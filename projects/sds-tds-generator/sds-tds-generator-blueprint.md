# SDS/TDS Document Generator — Blueprint

---

**Project ID:** `sds-tds-generator`
**Version:** 1.0.0
**Created:** 2025-11-11
**Status:** Blueprint
**Purpose:** Automated generation of print-ready Safety Data Sheets (SDS) and Technical Data Sheets (TDS) using repository data as single source of truth

---

## Executive Summary

This project validates the Forestal MT Suite as a true **source-of-truth** by automatically generating regulatory-compliant, print-ready SDS and TDS documents for all 46 SKUs. The generator consumes structured product data (JSON), applies official brand typography, embeds letterhead templates, and outputs professional DOCX/PDF documents suitable for B2B partners, customs, and regulatory submissions.

### Business Value

- **Time Savings:** Reduce document creation from 2-4 hours per product → 5 minutes for all 46 products
- **Consistency:** 100% brand compliance (typography, colors, layout)
- **Scalability:** Add new products → regenerate entire document library in seconds
- **Regulatory Ready:** SDS format follows GHS standards; TDS includes technical specifications
- **Revenue Impact:** $25K-50K/year (faster partner onboarding, reduced errors, professional documentation)

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    FORESTAL MT SUITE (Source of Truth)          │
├─────────────────────────────────────────────────────────────────┤
│ products-data/sku-base.json          → Product specifications   │
│ docs/brand/typography.md             → Document formatting      │
│ docs/brand/colors.md                 → Brand palette            │
│ docs/company/company-profile.md      → Company info             │
│ assets/templates/official-letterhead → Base templates           │
│ assets/fonts/                        → Typography assets        │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                  SDS/TDS GENERATOR (Python)                     │
├─────────────────────────────────────────────────────────────────┤
│ 1. Load product data (46 SKUs)                                 │
│ 2. Load typography specs & company info                        │
│ 3. For each SKU:                                               │
│    a. Clone letterhead template                                │
│    b. Apply typography styles (Garamond, colors, sizes)       │
│    c. Populate SDS sections (GHS format)                       │
│    d. Populate TDS sections (technical specs)                  │
│    e. Export to DOCX & PDF                                     │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                     OUTPUT (Print-Ready Docs)                   │
├─────────────────────────────────────────────────────────────────┤
│ outputs/sds/FMT-BO-RBO-2025-SDS.docx                          │
│ outputs/sds/FMT-BO-RBO-2025-SDS.pdf                           │
│ outputs/tds/FMT-BO-RBO-2025-TDS.docx                          │
│ outputs/tds/FMT-BO-RBO-2025-TDS.pdf                           │
│ ... (46 SKUs × 2 doc types × 2 formats = 184 files)           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Document Specifications

### SDS (Safety Data Sheet) - GHS Format

Based on Globally Harmonized System (GHS) Rev. 7, 16 sections:

1. **Identification** - Product name, SKU, company info, emergency contact
2. **Hazard Identification** - GHS classification, pictograms, signal words
3. **Composition/Ingredients** - Botanical source, chemical composition, CAS numbers
4. **First-Aid Measures** - Eye, skin, inhalation, ingestion
5. **Fire-Fighting Measures** - Extinguishing media, special hazards
6. **Accidental Release Measures** - Spill containment, cleanup
7. **Handling and Storage** - Safe handling, storage conditions
8. **Exposure Controls/PPE** - Occupational limits, protective equipment
9. **Physical/Chemical Properties** - Appearance, pH, melting point, etc.
10. **Stability and Reactivity** - Chemical stability, incompatibilities
11. **Toxicological Information** - Acute/chronic effects, routes of exposure
12. **Ecological Information** - Aquatic toxicity, biodegradability
13. **Disposal Considerations** - Waste disposal methods
14. **Transport Information** - UN number, shipping class, packing group
15. **Regulatory Information** - OSHA, EPA, EU regulations
16. **Other Information** - Revision date, sources, disclaimer

### TDS (Technical Data Sheet)

Product-focused technical specifications:

1. **Product Identity** - Name, SKU, botanical source, seal
2. **Product Description** - Heritage narrative, key benefits
3. **Technical Specifications**
   - Appearance (color, texture, odor)
   - Physical properties (density, viscosity, pH)
   - Chemical composition (fatty acid profile, vitamins)
   - Microbiological standards (total plate count, E. coli)
4. **Quality Standards** - Purity, heavy metals, pesticides, GMO status
5. **Traditional Uses** - Ethnobotanical applications
6. **Processing Method** - Harvesting, extraction, quality control
7. **Storage & Shelf Life** - Conditions, duration, packaging
8. **Regulatory Compliance** - HS code, certifications, country of origin
9. **Applications** - Recommended uses, dosage, formulation guidance
10. **Company Information** - Contact, manufacturing site, certifications

---

## Typography Implementation

### Document Hierarchy (from typography.md)

| Element | Font | Size | Color | Weight | Case |
|---------|------|------|-------|--------|------|
| Document Title (SDS/TDS) | Garamond | 18pt | Forest Green #1F6D03 | Bold | ALL CAPS |
| Product Name | Garamond | 16pt | Leaf Green #52B006 | Bold | Title Case |
| Section Headers | Garamond | 14pt | Forest Green #1F6D03 | Bold | ALL CAPS |
| Subsection Headers | Garamond | 12pt | Black #000000 | Bold | Title Case |
| Data Labels | Garamond | 12pt | Black #000000 | Bold | Sentence |
| Body Text | Garamond | 12pt | Black #000000 | Regular | Sentence |
| Bullets/Lists | Garamond | 12pt | Black #000000 | Regular | Sentence |

### Line Height & Spacing
- Line height: 1.5 for all text
- Section spacing: 18pt before, 4pt after headers
- List spacing: 4pt before/after items
- Paragraph spacing: 0pt (text justified)

---

## Technical Stack

### Core Dependencies

```python
# Document generation
python-docx>=0.8.11         # DOCX creation & manipulation
docx2pdf>=0.1.8             # PDF export (Windows/macOS)
# OR
pypandoc>=1.11              # PDF export (cross-platform via pandoc)

# Data processing
openpyxl>=3.1.0             # Already installed
pyyaml>=6.0                 # Parse YAML frontmatter

# Typography & styling
python-docx-template>=0.16  # Template variables
pillow>=10.0.0              # Image handling

# Utilities
tqdm>=4.66.0                # Progress bars for bulk generation
click>=8.1.0                # CLI interface
```

### System Requirements

- **Python:** 3.10+ (3.11 recommended per .python-version)
- **Fonts:** Garamond/Cormorant Garamond (from assets/fonts/)
- **PDF Engine:**
  - Windows: Uses MS Word COM automation via docx2pdf
  - macOS: Uses LibreOffice via docx2pdf
  - Linux: Requires pandoc or LibreOffice headless

---

## Implementation Roadmap

### Phase 1: Foundation (2-3 hours)

**Step 1.1: Setup Project Structure**
```bash
projects/sds-tds-generator/
├── blueprint.md                    # This document
├── source-files-manifest.md        # Input file inventory
├── generator.py                    # Main script
├── templates/
│   ├── sds_template.py            # SDS section builders
│   └── tds_template.py            # TDS section builders
├── styles/
│   └── typography.py              # Style definitions from typography.md
├── outputs/
│   ├── sds/                       # Generated SDS docs
│   └── tds/                       # Generated TDS docs
├── requirements.txt               # Project dependencies
└── README.md                      # Usage instructions
```

**Step 1.2: Install Dependencies**
```bash
cd projects/sds-tds-generator
pip install -r requirements.txt
```

**Step 1.3: Font Setup**
- Install Cormorant Garamond from `../../assets/fonts/source/`
- Verify font availability on system
- Configure fallback to Georgia if Garamond unavailable

---

### Phase 2: Typography System (1-2 hours)

**Step 2.1: Parse typography.md**
Create `styles/typography.py` that programmatically reads `docs/brand/typography.md` and converts to python-docx style objects:

```python
# styles/typography.py
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

class ForestalTypography:
    """Typography system from docs/brand/typography.md"""

    # Colors from brand palette
    FOREST_GREEN = RGBColor(31, 109, 3)      # #1F6D03
    LEAF_GREEN = RGBColor(82, 176, 6)        # #52B006
    BLACK = RGBColor(0, 0, 0)                # #000000

    # Font family
    FONT_FAMILY = "Cormorant Garamond"  # Fallback to Georgia

    @staticmethod
    def apply_document_title(paragraph):
        """Level 1: Document Title - 18pt, Forest Green, Bold, ALL CAPS"""
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
        run.font.name = ForestalTypography.FONT_FAMILY
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = ForestalTypography.FOREST_GREEN
        paragraph.paragraph_format.line_spacing = 1.5
        return paragraph

    @staticmethod
    def apply_product_name(paragraph):
        """Level 2: Product Name - 16pt, Leaf Green, Bold, Title Case"""
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
        run.font.name = ForestalTypography.FONT_FAMILY
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = ForestalTypography.LEAF_GREEN
        paragraph.paragraph_format.line_spacing = 1.5
        return paragraph

    # ... (continue for all 8 levels)
```

**Step 2.2: Test Typography**
Create test document with all 8 hierarchy levels to verify visual consistency.

---

### Phase 3: Template System (2-3 hours)

**Step 3.1: Clone Letterhead Template**
```python
# generator.py
from docx import Document
import shutil
from pathlib import Path

def clone_letterhead_template():
    """Clone the official letterhead DOCX as base template"""
    template_path = Path("../../assets/templates/official-letterhead/docx/forestal-mt-letterhead.docx")
    temp_doc = Document(template_path)
    return temp_doc
```

**Step 3.2: Build SDS Sections**
```python
# templates/sds_template.py
def build_sds(doc, product_data, company_data):
    """Build 16-section GHS SDS document"""

    # Section 1: Identification
    add_section_header(doc, "1. IDENTIFICATION")
    add_data_field(doc, "Product Name:", product_data["product_name"])
    add_data_field(doc, "Product Code:", product_data["sku"])
    add_data_field(doc, "Botanical Source:", product_data["botanical_source"])
    add_data_field(doc, "Manufacturer:", company_data["legal_name"])
    add_data_field(doc, "Address:", company_data["address"])
    add_data_field(doc, "Emergency Contact:", "+504-XXXX-XXXX")
    doc.add_paragraph()  # Spacing

    # Section 2: Hazard Identification
    add_section_header(doc, "2. HAZARD IDENTIFICATION")
    add_paragraph(doc, "GHS Classification: Not classified as hazardous")
    add_paragraph(doc, "Signal Word: None")
    add_paragraph(doc, "Hazard Statements: None")
    add_paragraph(doc, "Precautionary Statements: Keep out of reach of children. For external use only.")
    doc.add_paragraph()

    # Section 3: Composition/Ingredients
    add_section_header(doc, "3. COMPOSITION/INGREDIENTS")
    add_data_field(doc, "Ingredient:", product_data["ingredients"])
    add_data_field(doc, "Botanical Name:", product_data["botanical_source"])
    add_data_field(doc, "Part Used:", product_data["part_used"])
    add_data_field(doc, "CAS Number:", "N/A (natural botanical extract)")
    doc.add_paragraph()

    # ... (continue for all 16 sections)

    return doc
```

**Step 3.3: Build TDS Sections**
```python
# templates/tds_template.py
def build_tds(doc, product_data, company_data):
    """Build technical data sheet with product specs"""

    # Section 1: Product Identity
    add_section_header(doc, "PRODUCT IDENTITY")
    add_data_field(doc, "Product Name:", product_data["product_name"])
    add_data_field(doc, "SKU:", product_data["sku"])
    add_data_field(doc, "Collection:", product_data["collection"])
    add_data_field(doc, "Seal:", product_data["seal"])
    add_data_field(doc, "Botanical Source:", product_data["botanical_source"])
    add_data_field(doc, "HS Code:", product_data["hs_code"])
    doc.add_paragraph()

    # Section 2: Product Description
    add_section_header(doc, "PRODUCT DESCRIPTION")
    add_paragraph(doc, product_data["product_description"])
    doc.add_paragraph()

    # Section 3: Traditional Uses
    add_section_header(doc, "TRADITIONAL USES")
    for line in product_data["traditional_uses"].split("\n"):
        add_bullet(doc, line.strip("• "))
    doc.add_paragraph()

    # Section 4: Processing Method
    add_section_header(doc, "PROCESSING METHOD")
    for line in product_data["processing_method"].split("\n"):
        add_bullet(doc, line.strip("• "))
    doc.add_paragraph()

    # ... (continue for all sections)

    return doc
```

---

### Phase 4: Data Integration (1-2 hours)

**Step 4.1: Load Product Data**
```python
# generator.py
import json
from pathlib import Path

def load_product_data():
    """Load all 46 SKUs from sku-base.json"""
    data_path = Path("../../products-data/sku-base.json")
    with open(data_path) as f:
        products = json.load(f)
    return products

def load_company_data():
    """Parse company info from company-profile.md"""
    profile_path = Path("../../docs/company/company-profile.md")
    # Parse YAML frontmatter + markdown content
    # Return structured company data
    pass
```

**Step 4.2: Create Data Mapper**
```python
# generator.py
def map_product_to_sds(product):
    """Map product JSON fields to SDS sections"""
    return {
        "identification": {
            "product_name": product["product_name"],
            "sku": product["sku"],
            "botanical_source": product["botanical_source"],
            # ...
        },
        "composition": {
            "ingredients": product["ingredients"],
            "part_used": product["part_used"],
            # ...
        },
        # ... map all 16 sections
    }

def map_product_to_tds(product):
    """Map product JSON fields to TDS sections"""
    return {
        "identity": {
            "product_name": product["product_name"],
            "sku": product["sku"],
            "collection": product["collection"],
            "seal": product["seal"],
            # ...
        },
        "description": product["product_description"],
        "traditional_uses": product["traditional_uses"],
        "processing": product["processing_method"],
        # ... map all sections
    }
```

---

### Phase 5: Bulk Generation (1 hour)

**Step 5.1: Main Generation Script**
```python
# generator.py
import click
from tqdm import tqdm
from pathlib import Path

@click.command()
@click.option('--doc-type', type=click.Choice(['sds', 'tds', 'both']), default='both')
@click.option('--format', type=click.Choice(['docx', 'pdf', 'both']), default='both')
@click.option('--sku', default=None, help='Generate for specific SKU (default: all)')
def generate(doc_type, format, sku):
    """Generate SDS/TDS documents for Forestal MT products"""

    # Load data
    products = load_product_data()
    company = load_company_data()

    # Filter by SKU if specified
    if sku:
        products = [p for p in products if p["sku"] == sku]

    # Progress bar
    total_docs = len(products) * (2 if doc_type == 'both' else 1)
    with tqdm(total=total_docs, desc="Generating documents") as pbar:

        for product in products:
            # Generate SDS
            if doc_type in ['sds', 'both']:
                doc = clone_letterhead_template()
                doc = build_sds(doc, product, company)
                save_document(doc, product["sku"], "sds", format)
                pbar.update(1)

            # Generate TDS
            if doc_type in ['tds', 'both']:
                doc = clone_letterhead_template()
                doc = build_tds(doc, product, company)
                save_document(doc, product["sku"], "tds", format)
                pbar.update(1)

    print(f"\n✓ Generated {total_docs} documents")
    print(f"  Location: outputs/{doc_type}/")

def save_document(doc, sku, doc_type, format_type):
    """Save document as DOCX and/or PDF"""
    output_dir = Path(f"outputs/{doc_type}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save DOCX
    if format_type in ['docx', 'both']:
        docx_path = output_dir / f"{sku}-{doc_type.upper()}.docx"
        doc.save(docx_path)

    # Save PDF
    if format_type in ['pdf', 'both']:
        pdf_path = output_dir / f"{sku}-{doc_type.upper()}.pdf"
        convert_to_pdf(docx_path, pdf_path)

if __name__ == "__main__":
    generate()
```

**Step 5.2: CLI Usage**
```bash
# Generate all documents (46 SKUs × 2 types × 2 formats = 184 files)
python generator.py

# Generate only SDS documents
python generator.py --doc-type sds

# Generate only DOCX format
python generator.py --format docx

# Generate for single SKU
python generator.py --sku FMT-BO-RBO-2025

# Generate TDS in PDF only
python generator.py --doc-type tds --format pdf
```

---

### Phase 6: Quality Assurance (1 hour)

**Step 6.1: Visual QA Checklist**
```python
# tools/qa_validator.py
def validate_document(doc_path):
    """Validate generated document against typography.md specs"""
    doc = Document(doc_path)

    issues = []

    # Check document title
    if doc.paragraphs[0].runs[0].font.size != Pt(18):
        issues.append("Title font size incorrect")

    if doc.paragraphs[0].runs[0].font.color.rgb != RGBColor(31, 109, 3):
        issues.append("Title color incorrect")

    # Check section headers
    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            if para.runs[0].font.size != Pt(14):
                issues.append(f"Header size incorrect: {para.text}")

    # ... validate all typography specs

    return issues
```

**Step 6.2: Automated Testing**
```python
# tests/test_document_generator.py
import pytest
from generator import generate_sds, generate_tds

def test_sds_generation():
    """Test SDS document structure"""
    product = load_test_product()
    doc = generate_sds(product)

    # Verify 16 sections exist
    sections = [p.text for p in doc.paragraphs if p.style.name == 'Heading 1']
    assert len(sections) == 16
    assert "1. IDENTIFICATION" in sections[0]
    assert "16. OTHER INFORMATION" in sections[-1]

def test_tds_generation():
    """Test TDS document structure"""
    product = load_test_product()
    doc = generate_tds(product)

    # Verify required sections
    sections = [p.text for p in doc.paragraphs if p.style.name == 'Heading 1']
    assert "PRODUCT IDENTITY" in sections
    assert "TRADITIONAL USES" in sections
    assert "PROCESSING METHOD" in sections

def test_typography_compliance():
    """Test typography matches typography.md"""
    doc = generate_test_document()

    # Validate fonts, sizes, colors, spacing
    assert_typography_compliant(doc)
```

---

### Phase 7: Documentation & Deployment (1 hour)

**Step 7.1: Create README**
```markdown
# SDS/TDS Document Generator

Automated generation of Safety Data Sheets (SDS) and Technical Data Sheets (TDS)
for all Forestal MT products using the repository as single source of truth.

## Quick Start

# Install dependencies
pip install -r requirements.txt

# Generate all documents
python generator.py

# View outputs
ls outputs/sds/
ls outputs/tds/

## Features

- ✓ 100% brand-compliant typography
- ✓ Official letterhead embedded
- ✓ GHS-compliant SDS format (16 sections)
- ✓ Comprehensive TDS specifications
- ✓ Bulk generation (46 SKUs in ~5 minutes)
- ✓ DOCX + PDF export

## Configuration

Edit `config.yaml` to customize:
- Output directory
- Font preferences
- PDF engine
- Template overrides
```

**Step 7.2: Integration with Main Repo**
```bash
# Add generator to main automation scripts
echo "python projects/sds-tds-generator/generator.py" >> tools/build_all_assets.sh

# Add to CI workflow
# .github/workflows/validate-repo.yml
# - name: Generate sample documents
#   run: python projects/sds-tds-generator/generator.py --sku FMT-BO-RBO-2025
```

---

## Expected Outputs

### File Structure
```
outputs/
├── sds/
│   ├── FMT-BO-CO-2025-SDS.docx
│   ├── FMT-BO-CO-2025-SDS.pdf
│   ├── FMT-BO-RBO-2025-SDS.docx
│   ├── FMT-BO-RBO-2025-SDS.pdf
│   └── ... (46 SKUs × 2 formats = 92 files)
└── tds/
    ├── FMT-BO-CO-2025-TDS.docx
    ├── FMT-BO-CO-2025-TDS.pdf
    ├── FMT-BO-RBO-2025-TDS.docx
    ├── FMT-BO-RBO-2025-TDS.pdf
    └── ... (46 SKUs × 2 formats = 92 files)

Total: 184 print-ready documents
```

### Sample SDS Output (FMT-BO-RBO-2025-SDS.pdf)

```
┌──────────────────────────────────────────────────────────────┐
│                    [LETTERHEAD HEADER]                       │
│              Forestal Murillo Tejada Logo                    │
└──────────────────────────────────────────────────────────────┘

                    SAFETY DATA SHEET

              Raw Batana Oil (FMT-BO-RBO-2025)

──────────────────────────────────────────────────────────────

1. IDENTIFICATION

Product Name:      Raw Batana Oil
Product Code:      FMT-BO-RBO-2025
Botanical Source:  Elaeis oleifera
Manufacturer:      Forestal Murillo Tejada S. de R.L. de C.V.
Address:           Barrio Arriba, San Francisco de la Paz,
                   Olancho, Honduras
Emergency Contact: +504-XXXX-XXXX

2. HAZARD IDENTIFICATION

GHS Classification: Not classified as hazardous
Signal Word:        None
Hazard Statements:  None
Precautionary:      Keep out of reach of children.
                    For external use only.

... [continues for all 16 sections]

┌──────────────────────────────────────────────────────────────┐
│                    [LETTERHEAD FOOTER]                       │
│         Exporting Nature Without Borders                     │
└──────────────────────────────────────────────────────────────┘
```

---

## Success Metrics

### Quantitative
- **Generation Speed:** < 5 minutes for all 184 documents
- **Typography Accuracy:** 100% compliance with typography.md
- **Data Coverage:** 46/46 SKUs processed
- **Error Rate:** 0 failed documents

### Qualitative
- **Print Quality:** Professional, regulatory-compliant
- **Brand Consistency:** Matches official letterhead
- **Partner Feedback:** "Looks more professional than competitors"
- **Regulatory Acceptance:** Passes customs/compliance reviews

---

## Future Enhancements

### Phase 8: Advanced Features (Optional)

1. **Multi-language Support**
   - Spanish (Hoja de Datos de Seguridad)
   - Generate from `docs/brand/voice-es.md` when available

2. **QR Code Integration**
   - Embed QR codes linking to product pages
   - Links to `https://forestal-mt.com/products/{sku}`

3. **Digital Signatures**
   - Add digital signature blocks
   - Integration with DocuSign API

4. **Version Control**
   - Track document revisions
   - Auto-increment version numbers
   - Change logs per product

5. **Batch Upload**
   - Auto-upload to Dropbox/Google Drive
   - Partner portal integration

6. **Regulatory Templates**
   - FDA labeling
   - EU REACH compliance
   - Organic certification sheets

---

## Maintenance

### Updating Product Data
```bash
# Edit Excel master
vim products-data/forestal-mt-products-catalogue-46-skus.xlsx

# Regenerate JSON exports
python tools/build_product_data.py

# Regenerate all documents
python projects/sds-tds-generator/generator.py

# Commit changes
git add products-data/ outputs/
git commit -m "Update product data and regenerate SDS/TDS"
git push
```

### Updating Typography
```bash
# Edit typography specifications
vim docs/brand/typography.md

# Regenerate documents with new styles
python projects/sds-tds-generator/generator.py

# QA review
python tools/qa_validator.py outputs/
```

---

## Budget & Timeline

| Phase | Time | Dependencies |
|-------|------|--------------|
| Phase 1: Foundation | 2-3 hrs | Python, pip |
| Phase 2: Typography | 1-2 hrs | python-docx |
| Phase 3: Templates | 2-3 hrs | SDS/TDS research |
| Phase 4: Data Integration | 1-2 hrs | json, yaml |
| Phase 5: Bulk Generation | 1 hr | tqdm, click |
| Phase 6: QA | 1 hr | pytest |
| Phase 7: Documentation | 1 hr | - |
| **Total** | **9-13 hrs** | |

**Cost:** $0 (all open-source tools)
**ROI:** $25K-50K/year (time savings + partner value)

---

## Conclusion

This project transforms your repository from a "passive archive" into an **active manufacturing system** that produces real business value. By generating 184 regulatory-compliant documents in minutes, you validate that:

1. ✓ **Data integrity works** - SKU data flows seamlessly
2. ✓ **Typography system works** - Brand guidelines are enforceable
3. ✓ **Templates work** - Letterhead integrates programmatically
4. ✓ **Automation works** - Bulk operations scale efficiently
5. ✓ **Source-of-truth works** - Single edit → cascading updates

**Next Steps:**
1. Review this blueprint
2. Confirm SDS/TDS section requirements (regulatory team)
3. Begin Phase 1 implementation
4. Generate first test document
5. Iterate and deploy

---

**Blueprint Version:** 1.0.0
**Created:** 2025-11-11
**Author:** Senior Repository & Business-Intelligence Auditor
**Status:** Ready for Implementation
