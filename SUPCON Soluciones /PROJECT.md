# Project: SUPCON Valve Catalog Replication & Spanish Translation

## Architecture
- Dual-track pipeline: Implementation Track and E2E Testing Track.
- The web app will be a standalone, premium, responsive Vanilla HTML/CSS/JS client-side catalog.
- Data Flow:
  - Raw slide/excel text -> Python Extraction Script -> `productos.json` (Structured, Spanish).
  - Web Catalog (SPA) -> Fetches `productos.json` -> Renders Landing Page, Category Sections, Product Detail Views, and Quote Modal.
  - Interactive Filter Engine -> Processes user input to search and filter products in real-time.
  - Verification Script -> Validates `productos.json` coverage and translation quality.

## Code Layout
- `extract.py`: Extraction script that parses data and outputs `productos.json`.
- `productos.json`: Structured database of extracted and translated products.
- `index.html`: Main SPA file for the premium catalog.
- `js/app.js`: Main JavaScript file for rendering, searching, filtering, and modal interaction.
- `css/styles.css`: CSS file for premium styling (dark/light themes, typography, responsiveness).
- `verificar_catalogo.py`: Verification script.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E1 | E2E Test Infra & Tier 1 | E2E Test infrastructure and Tier 1 feature coverage tests | None | IN_PROGRESS (Conv: 22f0611d-7828-44b6-b78d-4eeb3effe021) |
| E2 | E2E Tier 2 & 3 Tests | Boundary cases and cross-feature combination test cases | E1 | PLANNED |
| E3 | E2E Tier 4 Tests | Real-world application scenarios, publishes TEST_READY.md | E2 | PLANNED |
| M1 | Content Extraction | Automated script parsing local dumps to Spanish productos.json | None | IN_PROGRESS (Conv: ca32f3b9-3f84-4911-8f00-71cbba4f808e) |
| M2 | Web Catalog SPA | Modern responsive catalog frontend layout in Spanish | M1 | PLANNED |
| M3 | Search & Filters | Real-time interactive search and filtering logic | M2 | PLANNED |
| M4 | Verification Script | Verification script to check coverage & translation | M1, M3 | PLANNED |
| M5 | E2E Pass & Hardening | Final verification against E2E test suite & white-box hardening | M4, E3 | PLANNED |

## Interface Contracts
### Extraction Script ↔ Web Catalog
- Data schema of `productos.json` (JSON Array of objects):
  - `id`: unique string identifier (e.g. `ln81-globe`)
  - `name`: product name in Spanish (e.g. `Válvula de control neumática de globo de asiento simple serie LN81`)
  - `category`: main category (e.g. `Válvulas de Globo`, `Válvulas de Bola`, `Válvulas de Mariposa`, `Otros Instrumentos`)
  - `description`: product description in Spanish
  - `features`: array of strings with key features in Spanish
  - `specifications`: object containing technical details (e.g. `diámetro_nominal`, `presión_rating`, `fuga_asiento`)
  - `certificates`: array of strings (e.g. `["CE", "ATEX", "SIL3"]`)
  - `image_path`: relative path to a local image or placeholder image

### Web Catalog ↔ Verification Script
- The verification script parses `productos.json` and checks:
  - At least 15 products mapped.
  - Distributed across at least 4 main categories.
  - Spanish translation check: No English technical terms or descriptions in key fields (e.g., "Linear Globe Control Valve", "Zero Leakage", "Fugitive Emission", etc.).
  - Returns exit code 0 on success, non-zero on failure.
