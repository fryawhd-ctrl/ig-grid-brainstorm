# Universal Blueprint & Direct Export Template

This reference defines the provider-agnostic output package used when an environment does not support native image generation, when generation tools are unavailable, or when the user wants ready-to-run prompts for external tools (Google Flow, Midjourney, ChatGPT / DALL-E 3, Gemini / Imagen, Ideogram, Flux).

It provides **both** the single compiled **Master Grid Prompt (12:10 / 6:5)** and the **6 Individual Tile Prompts (4:5)**.

---

## Output Delivery Methods

Depending on the active agent runtime:
- **Chat-First Output (Universal)**: Output this complete blueprint and the `captions.txt` code block directly in the conversation response so the user can immediately copy-paste prompts into their preferred generator.
- **File Export (When Supported)**: If the environment supports local file writing (`write_file`, artifacts, or workspace exports), save this document as `grid-blueprint.md` and save the captions as `captions.txt` in the active project/output directory.

---

## Universal Campaign Blueprint Schema

```markdown
# 6-Tile Instagram Campaign Blueprint

Use these prompts to generate your campaign either as a single compiled 3×2 master grid (`grid_master.png`) or as 6 individual tiles in Google Flow, Midjourney, ChatGPT, Gemini, Ideogram, or Flux.

---

## 1. Global Campaign Specifications

- **Campaign Theme**: [Overarching Campaign Narrative]
- **Master Grid Aspect Ratio**: 12:10 (6:5) landscape (`3240x2700 px`), holding 6 uncropped 4:5 vertical cells (`1080x1350 px` each).
- **Individual Tile Aspect Ratio**: 4:5 Vertical (`1080x1350 px`) with central 1:1 Square Safe Area (`1080x1080 px`).
- **Safe Margins**: All key visual elements, text overlays, and product silhouettes kept 10–15% inside borders.

### Master 2–3 Color Palette (Strict Family)
- **Dominant Saturated Dark (60%)**: `[#HEX]` (Deep contrast / shadow tone)
- **Clean Light Canvas (30%)**: `[#HEX]` (Negative space / airy canvas tone)
- **Graphic Accent (10%)**: `[#HEX]` (Electric pop for badges and typographic punch)

### Checkerboard Grid Layout Rhythm
- **Row 1**: Tile 1 (Dark) — Tile 2 (Light) — Tile 3 (Dark)
- **Row 2**: Tile 4 (Light) — Tile 5 (Dark) — Tile 6 (Light)

### Unified Typography Specs
- **Font Family**: [Single Font Family, e.g., Plus Jakarta Sans / Space Grotesk]
- **Contrast**: Built through extreme weight shifts (Heavy 800 vs. Regular 400).

---

## 2. Unified Master Grid Generation Prompt (Compiled 12:10 Image)

Generate the complete 3×2 profile grid as a single master image (`grid_master.png`):

```text
A professional editorial 3x2 Instagram grid campaign sheet featuring 6 distinct conceptual art-directed scenes of [Exact Product Description], displayed in a clean 3 columns by 2 rows matrix.

LAYOUT & GRID PROPORTIONS:
- Canvas format is strictly 12:10 landscape (6:5 aspect ratio).
- Exactly 3 columns and 2 rows forming 6 identical vertical 4:5 cells (each cell 1080x1350 proportion).
- Cells are separated ONLY by razor-thin, uniform 1px to 2px solid neutral hairline dividers (#333333 or #E0E0E0).
- ZERO thick borders, zero gutters, zero rounded corners, zero drop shadows, zero outer padding or white margins.
- ANTI-CROPPING: Full-bleed edge-to-edge layout. Never stretch, distort, or crop any internal 4:5 cell.
- NEGATIVE LAYOUT CONSTRAINTS: Ban 3x3 grids, ban 2x3 vertical grids, ban bento layouts, ban collages, ban overlapping floating cards.

CELL-BY-CELL ART DIRECTION (Checkerboard Rhythm):
- TOP-LEFT (Row 1, Col 1) [Dark]: [Surreal concept 1, dark background tone #HEX, specific typography placement].
- TOP-CENTER (Row 1, Col 2) [Light]: [Surreal concept 2, clean light background #HEX, specific typography placement].
- TOP-RIGHT (Row 1, Col 3) [Dark]: [Surreal concept 3, dark background tone #HEX, specific typography placement].
- BOTTOM-LEFT (Row 2, Col 1) [Light]: [Surreal concept 4, micro-isolation <15% scale, vast light negative space #HEX].
- BOTTOM-CENTER (Row 2, Col 2) [Dark]: [Surreal concept 5, dark background tone #HEX, specific container/physics swap].
- BOTTOM-RIGHT (Row 2, Col 3) [Light]: [Surreal concept 6, clean light background #HEX, kinetic human interaction].

COLOR PALETTE & LIGHTING:
Strict unified 2-3 color family: Dominant [#HEX], Canvas [#HEX], Accent [#HEX]. Studio directional cinematic lighting with razor-sharp product fidelity matching the reference item 100%.
--ar 12:10
```

---

## 3. 3x2 Profile Grid Map & Posting Order

```text
+-----------------------+-----------------------+-----------------------+
|        TILE 1         |        TILE 2         |        TILE 3         |
|  [Top-Left]           |  [Top-Center]         |  [Top-Right]          |  <-- ROW 1 (Top Row on Feed)
|  (Upload #6)          |  (Upload #5)          |  (Upload #4)          |
|  Background: Dark     |  Background: Light    |  Background: Dark     |
+-----------------------+-----------------------+-----------------------+
|        TILE 4         |        TILE 5         |        TILE 6         |
|  [Bottom-Left]        |  [Bottom-Center]      |  [Bottom-Right]       |  <-- ROW 2 (Bottom Row on Feed)
|  (Upload #3)          |  (Upload #2)          |  (Upload #1)          |
|  Background: Light    |  Background: Dark     |  Background: Light    |
+-----------------------+-----------------------+-----------------------+
```

### Reverse-Chronological Upload Sequence
1. **Upload #1** ➔ **Tile 6** (Bottom-Right)
2. **Upload #2** ➔ **Tile 5** (Bottom-Center)
3. **Upload #3** ➔ **Tile 4** (Bottom-Left)
4. **Upload #4** ➔ **Tile 3** (Top-Right)
5. **Upload #5** ➔ **Tile 2** (Top-Center)
6. **Upload #6** ➔ **Tile 1** (Top-Left)

---

## 4. Individual Tile-by-Tile Prompts & SEO Copy (For One-by-One Generation)

### Tile [N]: [Catchy Tile Name]
- **Grid Position**: Row [X], Column [Y] | **Upload Order**: Upload #[M] of 6
- **Funnel Stage**: [Top of Funnel / Mid-Funnel Craft / Action Guide / Philosophy / Objection / Community CTA]
- **Conceptual Lens**: [Scale & Physics / Container Swap / Kinetic Human / Typographic Architecture / Screen UI / Negative Space Whisper]
- **Background Tone**: [Dark / Light] (Checkerboard Rhythm)

#### Copy-Pasteable Individual Tile Prompt (Google Flow / Midjourney / ChatGPT)
```text
[Universal Prompt formatted for 4:5 vertical portrait:
1. Product Fidelity: The exact physical product subject, materials, surface finish, colors, and proportions matching the reference asset.
2. Surreal Metaphor & Staging: Explicitly preserves the surreal scale, gravity-defying physics, or unexpected environment (e.g. suspended mid-air in zero-G, shrunk inside an emergency glass box, or scaled to <15% in vast negative space). Never simplify into generic tabletop or studio photography.
3. Typography & Graphic Layout: Specifies graphic text placement if rendered directly (curved halo, split punchline, floating UI banner, or overlapping letters).
4. Color Atmosphere: Exact hex color values ([#HEX] dark tone vs [#HEX] light tone).
5. Aspect Ratio & Lighting: 4:5 vertical portrait framing, sharp cinematic directional lighting, clean 15% inner margins.
--ar 4:5]
```

#### On-Image Micro-Copy Overlay
- **Text**: `"[Witty copy strictly under 6 words]"`
- **Graphic Placement**: [Curved around object / Split top-and-bottom / In UI chat bubble / Overlapping background type]

#### SEO Hook & Humanized Caption
**[Opening Hook Line <125 characters with primary keywords before the fold]**

[1-3 concise, punchy paragraphs with zero AI slop, delivering specific value]

[Clear single-action CTA]

#### Strategic Hashtags (3-Tier Ladder)
- **Broad Category**: #[tag1] #[tag2] #[tag3]
- **Mid-Volume Niche**: #[tag4] #[tag5] #[tag6] #[tag7]
- **Hyper-Specific / Branded**: #[tag8] #[tag9] #[tag10]

#### Instagram SEO Alt-Text
[Descriptive, keyword-rich visual description for accessibility and search indexing]
```
