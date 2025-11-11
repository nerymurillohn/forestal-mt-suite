---
id: brand-typography
title: Forestal MT Document Typography
filename: typography.md
path: docs/brand/typography.md
repository: forestal-mt-suite
owner: nerymurillohn
type: Brand and Product Data Repository
company: Forestal MT (Forestal Murillo Tejada S. de R.L. de C.V.)
country: Honduras
industry: Artisan Furniture Manufacturing
canonical: true
description: Formatting rules for official documents (Docs, DOCX, PDF) including hierarchy, fonts, color, and spacing.
last_reviewed: 2025-11-09
status: published
---

## Forestal MT Document Typography

### Overview

Official decks, briefs, proposals, and PDFs must follow this hierarchy so every document mirrors the brand voice while remaining easy to execute in Google Docs, Microsoft Word, and PDF templates. All styles rely on Garamond (or *Cormorant Garamond* where available). If Garamond is unavailable, substitute `Cormorant Garamond` (preferred) or `Georgia` as a temporary fallback.

### Style Guide

| Level | Function | Font | Weight | Color | Size (pt) | Line Height | Spacing (Before/After pt) | Case | Alignment |
|-------|----------|------|--------|-------|-----------|-------------|---------------------------|------|-----------|
| 1 | Document Title | Garamond | Bold | Forest Green `#1F6D03` | 18 | 1.5 | 0 / 0 | ALL CAPS | Center |
| 2 | Product Name (Title) | Garamond | Bold | Leaf Green `#52B006` | 16 | 1.5 | 0 / 0 | Title Case | Center |
| 3 | Main Section Header | Garamond | Bold | Forest Green `#1F6D03` | 14 | 1.5 | 18 / 4 | ALL CAPS | Left |
| 4 | Subsection Header | Garamond | Bold | Black `#000000` | 12 | 1.5 | 0 / 0 | Title Case | Left |
| 5 | Data Label | Garamond | Bold | Black `#000000` | 12 | 1.5 | 0 / 0 | Title/Sentence | Left |
| 6 | Body Text & Data Value | Garamond | Regular | Black `#000000` | 12 | 1.5 | 0 / 0 | Sentence case | Justified |
| 7 | Bulleted List (`-`) | Garamond | Regular | Black `#000000` | 12 | 1.5 | 4 / 4 | Sentence case | Justified |
| 8 | Numbered List (`1.`) | Garamond | Regular | Black `#000000` | 12 | 1.5 | 4 / 4 | Sentence case | Justified |

### Implementation Notes

1. **Template Setup** - Create named styles in Google Docs/Word matching the table above (Title, Heading 1, Heading 2, Normal, Bullet, Numbered). Save as "Forestal MT Master Doc" and duplicate as needed.
2. **Color Application** - Use the exact hex codes from the brand palette (`docs/brand/colors.md`). When Soft Mint (`#D6E8D3`) is used as a background, switch body text to Earth Brown (#372704) for optimal contrast.
3. **Lists** - Bullets use an en dash or custom pine icon with 0.25" indent; numbered lists use decimal format (`1.`) with a 0.25" hanging indent.
4. **Pull Quotes / Callouts** - Playfair Display Italic 14 pt, Leaf Green text, centered with 0.5" left/right indent maintains narrative warmth.
5. **Fallback Fonts** - If collaborators lack Garamond, instruct them to install `Cormorant Garamond` from `assets/fonts/source/` or temporarily switch to `Georgia`.

### Quick Application Checklist

| Step | Google Docs / Word | HTML / CSS |
|------|--------------------|------------|
| 1 | Load `assets/templates/official-letterhead/docx/forestal-mt-letterhead.docx` and immediately “Save As” to preserve the master. | Include `@import url("../assets/fonts/fonts.css");` or copy the declarations from `assets/fonts/fonts.css`. |
| 2 | Create named styles (Title, Heading 1/2, Normal, Bullet, Numbered) using the table values above; lock each style to prevent ad-hoc overrides. | Map the style table to semantic classes: `.fmt-title`, `.fmt-heading`, `.fmt-body`, `.fmt-bullet`, `.fmt-quote`. |
| 3 | Set document default font to Garamond (or `Cormorant Garamond`) with line height 1.5; disable automatic hyphenation. | Define CSS variables for colors (`--forest-green: #1F6D03`, etc.) so the palette matches `docs/brand/colors.md`. |
| 4 | Configure bullets to use en dash (Alt+0150) or the pine icon asset; set indent to 0.25". | Apply `list-style-image` or pseudo-elements for pine bullet icons; preserve 0.25" equivalent padding. |
| 5 | Run a style audit: update the Table of Contents, verify headings use the assigned styles, then export to PDF. | Minify CSS and embed the font declarations so HTML/PDF exports match Docs formatting. |

### HTML / CSS Reference Snippet

```css
@import url("../assets/fonts/fonts.css");

:root {
  --forest-green: #1F6D03;
  --leaf-green: #52B006;
  --earth-brown: #493405;
  --body-font: "Cormorant Garamond", "Georgia", serif;
}

.fmt-title { font: 700 18pt/1.5 "Cinzel", serif; color: var(--forest-green); text-transform: uppercase; text-align: center; }
.fmt-heading { font: 700 14pt/1.5 "Cormorant Garamond", serif; color: var(--forest-green); letter-spacing: 0.04em; }
.fmt-body { font: 400 12pt/1.5 var(--body-font); color: #000; text-align: justify; }
.fmt-bullet { padding-left: 0.25in; text-indent: -0.25in; }
.fmt-quote { font: 400 14pt/1.4 "Playfair Display", serif; color: #52B006; text-align: center; }
```

Use this snippet as the baseline for any web or PDF generator to eliminate guesswork when converting the Word/Google Docs styles into code.

### Assets & References

- Fonts: `assets/fonts/source/` (Cinzel, Cormorant Garamond, Libre Baskerville, Playfair Display).
- CSS Import: `assets/fonts/fonts.css` for HTML/PDF exports.
- Color references: `docs/brand/colors.md`.

Using this system keeps every official document aligned with Forestal MT’s premium editorial tone and ensures motion between Docs, DOCX, and PDF remains frictionless.
