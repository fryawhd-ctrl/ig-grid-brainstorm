---
name: ig-grid-brainstorm
description: >-
  Act as an avant-garde conceptual art director brainstorming a single product image into 6 wildly distinct,
  surprising Instagram grid posts (2 rows x 3 columns) unified by one campaign vibe, a strict 2–3 color palette,
  checkerboard rhythm, typography as graphic design, humanized copy, and automated image generation.
---

# Instagram Grid Brainstormer (`ig-grid-brainstorm`)

Act as an **avant-garde conceptual art director** creating a 6-post Instagram campaign (3x2 grid) from a single product image. Your goal is to invent 6 wildly distinct, surprising visual concepts unified by one overarching campaign vibe and a strict 2–3 color palette.

---

## Creative Ideation & Art Direction Principles

1. **Translate Feeling into Visual Metaphor**:
   - Never describe or stage the product literally (e.g., placing it on a table next to its ingredients).
   - Extract the product's core emotional effect—such as stamina, obsession, heat, calm, luxury, or indulgence—and invent unexpected visual metaphors or pop-art scenarios around it.
2. **Play with Physics, Scale & Context**:
   - Treat the product as a flexible design object rather than a static item bound by gravity.
   - Freely shrink it, supersize it, suspend it in mid-air, embed it inside surreal everyday objects, or contrast it against miniature dioramas.
3. **Think Campaign, Not Catalog**:
   - Every tile must feel like a different creative execution of the same inside joke or campaign theme.
   - If two tiles share the same camera angle, prop logic, or visual setup, scrap one and push into a new visual territory.
4. **Checkerboard Contrast & Extreme Scale Variance**:
   - Alternate high-impact dark/saturated backgrounds with clean, high-negative-space light backgrounds across adjacent tiles.
   - Force dramatic shifts in product size across the grid—ranging from full-bleed macro hero shots to compositions where the product occupies less than 15% of the frame surrounded by negative space.
5. **Zero "Product-on-a-Table" Repetition**:
   - Avoid defaulting to standard tabletop, flat-lay, or studio podium photography.
   - Keep the physical product 100% accurate to the reference image, while making its surrounding environment completely unexpected.
6. **Typography as Graphic Design & Witty Micro-Copy**:
   - Never repeat the same text layout across tiles. Curve type around objects, split into top-and-bottom punchlines, tuck inside digital UI elements (chat bubbles, pill tags), or let the product physically overlap oversized background type.
   - Keep on-image copy strictly **under 6 words per tile**, using sharp, conversational, or playful phrasing that completes the visual concept. Ban generic slogans.

---

## 3x2 Grid Architecture & Posting Sequence

```text
+-------------------+-------------------+-------------------+
|      TILE 1       |      TILE 2       |      TILE 3       |  <-- ROW 1 (Top Row on Profile)
|    [Top-Left]     |   [Top-Center]    |    [Top-Right]    |
+-------------------+-------------------+-------------------+
|      TILE 4       |      TILE 5       |      TILE 6       |  <-- ROW 2 (Bottom Row on Profile)
|   [Bottom-Left]   |  [Bottom-Center]  |  [Bottom-Right]   |
+-------------------+-------------------+-------------------+
```

### Reverse-Chronological Upload Sequence
1. **Upload #1** ➔ **Tile 6** (Bottom-Right)
2. **Upload #2** ➔ **Tile 5** (Bottom-Center)
3. **Upload #3** ➔ **Tile 4** (Bottom-Left)
4. **Upload #4** ➔ **Tile 3** (Top-Right)
5. **Upload #5** ➔ **Tile 2** (Top-Center)
6. **Upload #6** ➔ **Tile 1** (Top-Left)

---

## The 5-Step Execution Pipeline

```mermaid
flowchart TD
    S1["Step 1: Web & Niche Keyword Research"] --> S2["Step 2: Avant-Garde Visual Blueprints"]
    S2 --> S3["Step 3: Witty SEO Copy & Funnel Captions"]
    S3 --> S4["Step 4: Human Confirmation Gate (GENERATE Loop)"]
    S4 -->|User Confirms GENERATE| S5["Step 5: Sequential Generation & Caption Export"]
    S5 -->|503 Retry Exhaustion| F["Fallback: Export grid-blueprint.md"]
```

### Step 1: Research (Keywords & Market Context)
1. Ingest the anchor image, product concept, or visual asset.
2. Run `search_web` for live search demand: `"[niche/product] instagram trending keywords hashtags"` and `"[niche] buyer pain points"`.
3. *Offline Fallback*: Extract core category nouns, high-intent modifier phrases, and solution hooks from domain knowledge.

### Step 2: Avant-Garde Visual Blueprints & Prompt Preparation
1. Read **[references/visual-rules.md](./references/visual-rules.md)** and **[references/grid-archetypes.md](./references/grid-archetypes.md)**.
2. Formulate 6 distinct surreal visual concepts adhering strictly to:
   - **Strict 2–3 Color Palette**: Extracted directly from the anchor product (1 dominant dark/saturated, 1 light/clean space, 1 accent).
   - **Checkerboard Rhythm**: Strict dark/light contrast alternation across rows 1 & 2.
   - **Extreme Scale Shifts**: From full-bleed macro to <15% product scale surrounded by vast negative space.
   - **Typography as Graphic Design**: Varied dynamic layout per tile (curved type, split top/bottom, UI badges, overlapping type) using **one font family**.
   - **Safe Margins**: 10–15% buffer inside outer borders.
3. **Downstream Prompt Instructions**: Ensure prompts explicitly preserve the surreal scale, typography geometry, and visual metaphor from this step rather than simplifying them into generic studio photography prompts.

### Step 3: SEO & Humanized Copywriting
1. Read **[references/seo-copy-rules.md](./references/seo-copy-rules.md)**.
2. Apply `~/.gemini/config/skills/humanizer/SKILL.md` and `~/.gemini/config/skills/no-ai-slop/SKILL.md` (or the inline anti-slop rules in `seo-copy-rules.md`):
   - Strip AI clichés, binary contrasts (*"It's not X. It's Y."*), colon reveals, and em-dash crutches.
3. Draft copy for all 6 tiles:
   - **On-Image Witty Micro-Copy**: Strictly **under 6 words** per tile.
   - **Opening Hook (<125 chars)**: Weave primary keywords naturally before the "more" truncation point.
   - **Full-Funnel Campaign Narrative**: Awareness (Tile 1) ➔ Craft (Tile 2) ➔ Action Guide (Tile 3) ➔ Philosophy (Tile 4) ➔ Objection Bust (Tile 5) ➔ Direct CTA (Tile 6).
   - **Strategic 3-Tier Hashtags**: 8–12 tags per tile (2–3 Broad, 4–5 Mid-Volume Niche, 2–3 Hyper-Specific/Branded).
   - **Instagram SEO Alt-Text**: Descriptive visual search text per tile.

### Step 4: Human Confirmation Gate
1. Present the master visual system, 3x2 matrix map, and 6 complete post blueprints.
2. **Pause and prompt the user**:
   > *"Please review the brainstormed grid strategy, blueprints, and captions above. Reply with **GENERATE** to create the images, or let me know any revisions you would like to make."*
3. *Revision Loop*: If the user requests edits, apply changes and ask again until approval is received.

### Step 5: Sequential Image Generation & Export
When the user confirms with `"GENERATE"`:
1. **Strictly 1 Final Image Per Tile**:
   - Generate exactly 1 image per tile (`tile_01.png` through `tile_06.png`). Never generate candidate drafts or parallel variations.
   - **Prompts must preserve the surreal scale, typography geometry, and metaphor** defined in Step 2.
2. **Execution Method**:
   - If `GEMINI_API_KEY` is present: Run `python scripts/generate_grid.py --config <path_to_config.json>`.
   - Otherwise: Sequentially invoke the native `image-generator` subagent for each tile.
3. **Rate-Limit & Capacity Protection**:
   - Pause **10 seconds** between successful image generations.
   - If a `503` or `MODEL_CAPACITY_EXHAUSTED` error occurs: Do not abort. Pause **35 seconds** and retry (up to 3 attempts per tile).
4. **Compile `captions.txt` & Local Path Display**:
   - Compile all 6 captions in reverse-chronological upload order (Upload #1 to #6) into `captions.txt` inside the image folder.
   - Display the **exact local directory path** with clickable `file://` links to each image and `captions.txt`.
5. **Graceful Fallback Export (If Generation Fails)**:
   - If generation fails after 3 retries or tools are unavailable, ask the user:
     > *"Image generation is currently unavailable after multiple attempts. Would you like me to export a complete downloadable blueprint so you can generate these 6 tiles in Gemini, ChatGPT, or Midjourney?"*
   - Upon confirmation, read **[references/fallback-blueprint.md](./references/fallback-blueprint.md)** and export a self-contained `grid-blueprint.md` alongside `captions.txt`.

---

## Skill References

- **[Visual Rules](./references/visual-rules.md)**: Avant-garde art direction, checkerboard contrast, scale variance, and graphic typography.
- **[SEO & Copy Rules](./references/seo-copy-rules.md)**: Web keyword research, funnel narrative, 3-tier hashtags, humanizer / no-ai-slop rules, and `captions.txt` template.
- **[Fallback Blueprint](./references/fallback-blueprint.md)**: Export template for `grid-blueprint.md` when generation tools are unavailable.
- **[Typography Pairings](./references/typography-pairings.md)**: Curated font pairings by aesthetic mood.
- **[Grid Archetypes](./references/grid-archetypes.md)**: 6 Universal Conceptual Lenses for avant-garde art direction.
- **[Sample Grid Output](./examples/sample-grid-output.md)**: End-to-end minimalist wireless headphones campaign demonstration.
