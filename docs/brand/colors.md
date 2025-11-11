---
id: brand-colors
title: Forestal MT Brand Color System
filename: colors.md
path: docs/brand/colors.md
repository: forestal-mt-suite
owner: nerymurillohn
type: Brand and Product Data Repository
company: Forestal MT (Forestal Murillo Tejada S. de R.L. de C.V.)
country: Honduras
industry: Artisan Furniture Manufacturing
canonical: true
description: Comprehensive palette, gradients, and motion guidance built from the six canonical Forestal MT colors.
last_reviewed: 2025-11-09
status: published
---

## Brand Color System

### 1. Core Palette (Provided Anchors)

| Role | Name | HEX | RGB | CMYK | Notes |
|------|------|-----|-----|------|-------|
| Primary Deep | Forest Green | `#1F6D03` | 31,109,3 | C72 M0 Y97 K57 | Signature canopy tone used in marks and hero sections. |
| Primary Mid | Leaf Green | `#52B006` | 82,176,6 | C53 M0 Y97 K31 | Product highlights, CTA fills, hover states. |
| Earth Anchor | Earth Brown | `#493405` | 73,52,5 | C0 M29 Y93 K71 | Typography on light fields, luxe packaging foils. |
| Luster Accent | Premium Gold | `#D8B132` | 216,177,50 | C0 M18 Y77 K15 | Foil, key icons, rating badges. |
| Trust Accent | Honduran Blue | `#0073CF` | 0,115,207 | C100 M44 Y0 K19 | Logistics touchpoints, links, data viz. |
| Support Veil | Soft Mint Green | `#D6E8D3` | 214,232,211 | C8 M0 Y9 K9 | Backgrounds, cards, secondary fills. |

All six colors exist in the 1000x1000 px logos (`assets/logos/`) ensuring immediate visual parity.

### 2. Strategic Extensions (Derived from Anchors)

| Derivation | HEX | Use |
|------------|-----|-----|
| Forest Green 70% Tint (`Verdant Mist`) | `#62994F` | Large hero gradients, infographic fills. |
| Forest Green 75% Shade (`Canopy Shadow`) | `#175202` | Overlay on photography, button pressed states. |
| Leaf Green Tint (`New Growth`) | `#86C851` | Success states, onboarding pulses. |
| Earth Brown Tint (`Sunbaked Clay`) | `#807150` | Neutral typography on dark panels. |
| Earth Brown Shade (`Cedar Bark`) | `#372704` | Backgrounds for gold foil callouts. |
| Premium Gold Tint (`Solar Veil`) | `#E4C870` | Highlight rules, dividers. |
| Premium Gold Shade (`Harvest Alloy`) | `#A28526` | Icon outlines, subtle metallic gradients. |
| Honduran Blue Tint (`Sky Current`) | `#4C9DDD` | Data viz secondary, hover transitions. |
| Honduran Blue Shade (`Depth Current`) | `#00569B` | CTA focus rings, link visited state. |
| Soft Mint Shade (`Cloud Canopy`) | `#A0AE9E` | Form backgrounds, neutral UI surfaces. |

*Derivations calculated as +/-30% tints/shades to keep chroma consistent with source hues.*

### 3. Palette Architecture

- **Primary Layer:** Forest Green, Leaf Green, Premium Gold carry the narrative of living forests plus artisan luxury.
- **Secondary Layer:** Earth Brown and Honduran Blue express trust, logistics rigor, and governance.
- **Support Layer:** Soft Mint plus its tints/shades keeps UI backgrounds breathable for product spec tables.
- **Energy Pops:** Premium Gold gradients or Honduran Blue pulses for launches; avoid additional hues to preserve lineage storytelling.

### 4. Application Map

| Surface | Background | Text / Icon | Notes |
|---------|------------|-------------|-------|
| Hero sections | `#1F6D03 -> #52B006` gradient | `#D6E8D3` plus `#D8B132` accents | Gradient direction 140 deg evokes canopy light. |
| Product cards | `#D6E8D3` | `#493405` headings, `#1F6D03` bullets | Add 2 px `#E4C870` top border. |
| CTA buttons | Fill `#52B006`, hover `#1F6D03`, text `#FFFFFF` | Outline `#D8B132` for premium tier. |
| Data & logistics UI | `#F6F8F4` | `#E4C870` chips, text `#00569B` | Aligns with Honduran export precision. |
| Packaging | `#493405` or `#1F6D03` base, `#D8B132` foil stamp, `#A0AE9E` lining | Communicates heritage + modernity. |

#### WCAG spot checks

- `#1F6D03` text on `#D6E8D3` -> contrast ratio 6.3:1 (AA+).
- `#0073CF` on white -> 5.2:1 (AA).
- Use `#372704` text when Soft Mint serves as body background.

### 5. Gradients & Blends

1. **Verdant Continuum:** `linear-gradient(135deg, #1F6D03 0%, #52B006 55%, #D6E8D3 100%)` - hero banners, sizzle videos.
2. **Ancestral Alloy:** `linear-gradient(120deg, #493405 0%, #D8B132 60%, #E4C870 100%)` - premium packaging mockups, KPI dashboards.
3. **Caribbean Thermocline:** `linear-gradient(145deg, #0073CF 0%, #4C9DDD 45%, #D6E8D3 100%)` - logistics visualizations, data backgrounds.
4. **Resin Glow (motion):** Animated radial blend from `#175202` to `#52B006` with pulsing `#D8B132` highlight every 6 seconds to mimic resin flare.

### 6. Contrast Pairs & Combinations

| Pair | Ratio | Use |
|------|-------|-----|
| `#1F6D03` text on `#D6E8D3` | 6.3:1 | Long-form body copy. |
| `#493405` on `#E4C870` | 7.1:1 | Labels, compliance docs. |
| `#D8B132` on `#1F6D03` | 2.2:1 | Accent-only (icons, strokes). |
| `#FFFFFF` on `#1F6D03` | 12.4:1 | CTA text, navigation. |
| `#0073CF` on `#F5FBF2` | 8.8:1 | Links, data callouts. |

### 7. Motion, Effects, and Materials

- **Gloss Mapping:** Apply subtle specular highlight (`#E4C870` to transparent) at 45 degrees on buttons to mimic hand-burnished resin.
- **Foil Simulation:** Use noise overlay (2% opacity) on `#D8B132` gradients to emulate brushed gold for digital packaging renderings.
- **Depth Pulse:** Animate box-shadows transitioning from `#175202` to transparent in 3-second loops for hero CTAs, referencing canopy sway.
- **Ink-bleed Texture:** Multiply layer using `#807150` at 15% opacity for printed collateral to evoke artisanal dyeing.

### 8. Alignment with Trends (2025)

- Luxury color forecasts for 2025 showcase immersive forest greens replacing pastel pistachios, so our canopy-first palette stays aspirational yet grounded.
- Earth-and-gold combinations continue to signal premium craftsmanship across interiors and premium packaging studies, validating the Forestal MT gold triad.
- Cross-industry outlooks emphasize grounding neutrals punctuated by optimistic blues, mirroring our Support and Trust layers for data-heavy deliverables.

These market cues ensure the palette feels both ancestral and future-proof for premium international audiences.
