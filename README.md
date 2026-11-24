# Instagram Grid Brainstormer (`ig-grid-brainstorm`)

An **Antigravity Custom Skill** that transforms a single anchor image into an aesthetic, high-converting 6-tile Instagram profile grid (2 rows × 3 columns) with strict visual consistency rules, checkerboard feed rhythm, humanized zero-AI-slop copywriting, deep Instagram SEO funnel strategy, and automated image generation.

---

## Key Features & Rules

### 1. Visual & Brand Consistency
- **Single Color Family**: Palette extracted directly from the hero product or content, maintaining a tight color family across all 6 tiles.
- **Checkerboard Rhythm**: Alternating dark and light backgrounds across adjacent tiles (e.g., Dark-Light-Dark on row 1, Light-Dark-Light on row 2) for an instantly curated look from afar.
- **Unified Typography**: A single consistent font family across all posts, varying only weights and sizes for hierarchy.
- **Product Preservation**: Core product perspective, lighting direction, materials, and proportions remain identical across every tile to anchor the campaign.

### 2. Creative Concept & Composition
- **One Overarching Campaign Theme**: All 6 tiles unite under a single campaign narrative (e.g., product drop, seasonal moment, lifestyle movement).
- **Scale & Interaction Variety**: Avoids static centered placements by distributing 4 creative styles:
  - *Hero Shot*: Full-size product interacting with surreal or miniature elements.
  - *Metaphor / Object Placement*: Scaled-down product in everyday objects (ring box, claw machine, teacup).
  - *Human Element*: Hands interacting, holding, or gesturing around the product.
  - *Minimalist Negative Space*: Scaled-down product surrounded by 70–80% clean breathing room.

### 3. Humanized Copywriting (Zero AI Slop)
Enforces rules from [`humanizer`](https://github.com/blader/humanizer) and [`no-ai-slop`](https://github.com/petergyang/no-ai-slop):
- **No Banned AI Words**: No `delve`, `foster`, `leverage`, `utilize`, `streamline`, `robust`, `cutting-edge`, `paradigm shift`, `game-changer`, `tapestry`, `realm`, `beacon`, `elevate`, `supercharge`, `harness`, or `meticulous`.
- **No Binary Contrasts**: No *"It's not X. It's Y."*—states claims directly.
- **No Colon Reveals or Em-Dash Crutches**: Eliminates fake-dramatic colons and excessive `—`.
- **Micro-Copy Limits**: On-image text strictly under 6–8 words per tile with 10–15% safe margins.

### 4. Deep Instagram SEO & Campaign Funnel Strategy
- **Pre-Drafting Research**: Analyzes product search volume, buyer intent, and high-converting keywords before drafting.
- **Full-Funnel Campaign Narrative**: Connects the 6 tiles across the grid:
  - *Tile 1 (Upload #6)*: Top of Funnel (Awareness & primary SEO keyword hook).
  - *Tile 2 (Upload #5)*: Mid-Funnel (Craft, materials & technical anatomy).
  - *Tile 3 (Upload #4)*: Mid-Funnel (Action guide & high-save how-to).
  - *Tile 4 (Upload #3)*: Brand Authority (Philosophy & emotional resonance).
  - *Tile 5 (Upload #2)*: Conversion (Objection handling & myth debunking).
  - *Tile 6 (Upload #1)*: Bottom of Funnel (Community discussion & direct CTA).
- **Strategic 3-Tier Hashtag Ladder (8–12 Tags per Tile)**:
  1. *Broad Category* (2–3 tags for algorithmic categorization)
  2. *Mid-Volume Niche & Buyer Intent* (4–5 tags targeting active shoppers)
  3. *Hyper-Specific / Branded* (2–3 tags for high-ranking authority)
- **Instagram SEO Alt-Text**: Included for every tile for search indexing and accessibility.

---

## Generation Workflow

```mermaid
flowchart TD
    A["Brainstorm 6-Tile Blueprints"] --> B["Pause & Ask User: Confirm GENERATE or Request Edits"]
    B -->|User Requests Edits| C["Apply Revisions to Blueprints"]
    C --> B
    B -->|User Confirms GENERATE| D["Generate 6 Images Sequentially (Strictly 1 Final Version per Tile)"]
    D -->|503 or Capacity Error| R["Wait 35s & Retry up to 3x"]
    R --> D
    D -->|Success| E["Save Images & Compile captions.txt into Same Directory"]
    E --> F["Display Exact Local Folder Path & File Links"]
    R -->|Failed After 3 Retries / Unavailable| G["Ask User: Export Complete Blueprint?"]
    G -->|User Agrees| H["Export grid-blueprint.md with Prompts & Specs"]
    H --> F
```

1. **Review Pause**: Present the strategy and 6 post blueprints, then pause for user confirmation.
2. **Revision Loop**: Seamlessly refine angles, copy, or colors until the user replies with `GENERATE`.
3. **Sequential Generation (Strictly 1 Final Image per Tile)**:
   - Generates exactly 1 final image version per tile (`tile_01.png` through `tile_06.png`)—never multiple candidate variations.
   - Enforces a 10-second cooldown between successful tiles and an automatic 35-second retry loop for 503 capacity errors.
   - Compiles all 6 captions into `captions.txt` inside that same folder.
4. **Graceful Fallback Export**: If image generation fails after 3 retries, exports a self-contained `grid-blueprint.md` with copy-pasteable image prompts for Gemini, ChatGPT, or Midjourney alongside `captions.txt`.

---

## Directory Structure

```text
ig-grid-brainstorm/
├── SKILL.md                          # Main skill instruction file with rules & workflow
├── README.md                         # Repository documentation
├── references/
│   ├── grid-archetypes.md            # Category-specific 6-angle matrices
│   ├── typography-pairings.md        # Curated font pairings by aesthetic mood
│   └── instagram-seo-guide.md        # Deep Instagram SEO, funnel & hashtag guide
└── examples/
    └── sample-grid-output.md         # End-to-end sample run (Artisanal Coffee Roastery)
```

---

## Installation

### Global Installation (Accessible in all chats)
```bash
# Windows
git clone https://github.com/fryawhd-ctrl/ig-grid-brainstorm.git "$HOME\.gemini\config\skills\ig-grid-brainstorm"

# macOS / Linux
git clone https://github.com/fryawhd-ctrl/ig-grid-brainstorm.git ~/.gemini/config/skills/ig-grid-brainstorm
```

---

## How to Use

Provide an anchor image in chat and prompt:

> *"Here is an image: `[image path or upload]`. Brainstorm an Instagram grid for it."*
