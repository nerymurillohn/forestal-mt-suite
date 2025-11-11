# FORESTAL MT CATALOGUE BUILD - REQUIRED FILES

## PRODUCT DATA (Core)
```
products-data/forestal-mt-products-catalogue-46-skus.xlsx
products-data/forestal-mt-products-retail-presentations-and-pricing.xlsx
products-data/forestal-mt-products-wholesale-presentations-and-pricing.xlsx
```

**Build step:** run `python tools/build_product_data.py` from the repo root.  
This regenerates the machine-readable artifacts:
- `products-data/catalogue.json` → metadata + `products[]` (46 SKUs) + `presentations[]` (retail & wholesale)
- `products-data/sku-base.json` and `products-data/sku-presentations.json`
- `products-data/retail.csv` and `products-data/wholesale.csv`

When consuming the JSON, load it as:
```js
const { products, presentations } = require("../products-data/catalogue.json");
```
Then join on `presentation.sku` to avoid duplicating long-form copy across pack sizes.

## PRODUCT IMAGES (46 hero images)

### Batana Oil Collection (4 images)
```
assets/products-images/batana-oil/hero/fmt-bo-co-2025-hero.png
assets/products-images/batana-oil/hero/fmt-bo-rbo-2025-hero.png
assets/products-images/batana-oil/hero/fmt-bo-sb-2025-hero.png
assets/products-images/batana-oil/hero/fmt-bo-sh-2025-hero.png
```

### Stingless Bee Honey Collection (1 image)
```
assets/products-images/stingless-bee-honey/hero/fmt-sbh-jm-2025-hero.png
```

### Traditional Herbs Collection (41 images)
```
assets/products-images/traditional-herbs/hero/fmt-th-al-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-bl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-by-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ca-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-cc-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-cd-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-cf-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ci-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-cr-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ct-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-cw-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-db-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-df-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-do-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-eu-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-gl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-glb-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-gu-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-hf-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-hg-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ht-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-kr-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-lg-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-lv-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ma-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ml-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-mo-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-mu-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-nl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-nm-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-pc-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-pg-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-pl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-pn-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-ps-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-sl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-sn-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-sp-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-sr-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-tl-2025-hero.png
assets/products-images/traditional-herbs/hero/fmt-th-tt-2025-hero.png
```

## BRAND ASSETS

### Logos
```
assets/logos/forestal-mt-logo-primary.png
assets/logos/forestal-mt-logo-primary-circled-variation.png
assets/logos/forestal-mt-logo-dark.png
assets/logos/forestal-mt-logo-dark-circled-variation.png
assets/logos/forestal-mt-logo-light.png
assets/logos/forestal-mt-logo-light-circled-variation.png
assets/logos/source/forestal-mt-logo-primary-svg.svg
assets/logos/source/forestal-mt-logo-dark-svg.svg
assets/logos/source/forestal-mt-logo-light-svg.svg
```

### Fonts
```
assets/fonts/source/Cinzel/Cinzel-VariableFont_wght.ttf
assets/fonts/source/Cinzel/static/Cinzel-Bold.ttf
assets/fonts/source/Cinzel/static/Cinzel-Regular.ttf
assets/fonts/source/CormorantGaramond/CormorantGaramond-VariableFont_wght.ttf
assets/fonts/source/CormorantGaramond/static/CormorantGaramond-Bold.ttf
assets/fonts/source/CormorantGaramond/static/CormorantGaramond-Regular.ttf
assets/fonts/source/LibreBaskerville/LibreBaskerville-Bold.ttf
assets/fonts/source/LibreBaskerville/LibreBaskerville-Regular.ttf
assets/fonts/source/PlayfairDisplay/PlayfairDisplay-VariableFont_wght.ttf
assets/fonts/source/PlayfairDisplay/static/PlayfairDisplay-Bold.ttf
assets/fonts/source/PlayfairDisplay/static/PlayfairDisplay-Regular.ttf
```

## BRAND DOCUMENTATION

### Brand Identity
```
docs/brand/overview.md
docs/brand/voice.md
docs/brand/colors.md
docs/brand/typography.md
docs/brand/logo.md
docs/brand/contacts.md
docs/brand/founders.md
docs/brand/history.md
```

### Collection Descriptions
```
docs/collections/batana-oil.md
docs/collections/stingless-bee-honey.md
docs/collections/traditional-herbs.md
```

### Company Information
```
docs/company/company-profile.md
docs/company/authenticity-chain.md
docs/company/business-hours.md
docs/company/shipping.md
docs/company/returns-policy.md
```

## TEMPLATE ASSETS (Optional but recommended)
```
assets/templates/official-letterhead/docx/forestal-mt-letterhead.docx
assets/templates/official-letterhead/pdf/forestal-mt-letterhead.pdf
```

---

## FILE COUNT SUMMARY
- Excel files: 3
- Product images: 46
- Logo files: 9
- Font files: 11 (core weights)
- Brand documentation: 8
- Collection docs: 3
- Company docs: 5
- Template files: 2

**TOTAL: 87 files**

## CRITICAL FILES (Minimum viable catalogue)
If building minimal catalogue, these are essential:
1. forestal-mt-products-catalogue-46-skus.xlsx (product data)
2. All 46 hero images (product visuals)
3. forestal-mt-logo-primary.png (brand identity)
4. colors.md (design system)
5. typography.md (formatting rules)
6. company-profile.md (legal/contact info)
7. Collections docs (3 files for context)

**MINIMUM: 54 files**
