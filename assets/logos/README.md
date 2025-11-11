---
id: assets-logos-readme
title: Forestal MT Logos
filename: README.md
path: assets/logos/README.md
canonical: true
owner: nerymurillohn
description: Source of truth for brand logo assets, their usage, and export specs.
last_reviewed: 2025-11-09
status: published
---

# Forestal MT Logo Assets

## Directory
| Variant | File | Notes |
|---------|------|-------|
| Primary PNG | forestal-mt-logo-primary.png | Full-color default mark |
| Primary PNG (Circled) | forestal-mt-logo-primary-circled-variation.png | Badge layout for avatars/stamps |
| Monochrome Dark PNG | forestal-mt-logo-dark.png | Use on light backgrounds |
| Monochrome Dark PNG (Circled) | forestal-mt-logo-dark-circled-variation.png | Badge for light backgrounds |
| Monochrome Light PNG | forestal-mt-logo-light.png | Use on dark backgrounds |
| Monochrome Light PNG (Circled) | forestal-mt-logo-light-circled-variation.png | Badge for dark backgrounds |
| Primary SVG | source/forestal-mt-logo-primary-svg.svg | Master vector |
| Monochrome Dark SVG | source/forestal-mt-logo-dark-svg.svg | Master vector |
| Monochrome Light SVG | source/forestal-mt-logo-light-svg.svg | Master vector |

> All PNGs are 1000x1000 with transparent backgrounds and centered artwork; treat them as ready-to-use square assets.

## Usage Guidance
- Keep PNGs at native resolution for master copies; create derivatives (webp, svg badges) in distribution repos, not here.
- Vector files live in `assets/logos/source/` and should be edited there before exporting new PNGs.
- Circled SVGs do not exist yet; generate from the master vector when design updates require them.

## Suggested Workflow
1. Edit vectors (`source/*.svg`) in your preferred design tool.
2. Export PNGs into this directory with consistent naming to maintain backward compatibility.
3. Record palette or brand guidelines inside `docs/brand/logo.md` and reference file paths there when documenting usage rules.
