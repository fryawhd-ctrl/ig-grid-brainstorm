# Universal Blueprint & Direct Export Template

This reference defines the provider-agnostic output package used when an environment does not support native image generation, when generation tools are unavailable, or when the user wants ready-to-run prompts for external tools (Midjourney, ChatGPT / DALL-E 3, Gemini / Imagen, Ideogram, Flux).

---

## Output Delivery Methods

Depending on the active agent runtime:
- **Chat-First Output (Universal)**: Output this complete blueprint and the `captions.txt` code block directly in the conversation response so the user can immediately copy-paste prompts into their preferred generator.
- **File Export (When Supported)**: If the environment supports local file writing (`write_file`, artifacts, or workspace exports), save this document as `grid-blueprint.md` and save the captions as `captions.txt` in the active project/output directory.

---

## Universal Campaign Blueprint Schema

```markdown
# 6-Tile Instagram Campaign Blueprint

Use these self-contained visual prompts and captions to generate your 6-tile grid in Midjourney, ChatGPT, Gemini, Ideogram, or Flux.

---

## 1. Global Campaign Specifications

- **Campaign Theme**: [Overarching Campaign Narrative]
- **Aspect Ratio**: 4:5 Vertical (`1080x1350 px`) with central 1:1 Square Safe Area (`1080x1080 px`)
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

## 2. 3x2 Profile Grid Map & Posting Order

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

## 3. Tile-by-Tile Generation Prompts & SEO Copy

### Tile [N]: [Catchy Tile Name]
- **Grid Position**: Row [X], Column [Y] | **Upload Order**: Upload #[M] of 6
- **Funnel Stage**: [Top of Funnel / Mid-Funnel Craft / Action Guide / Philosophy / Objection / Community CTA]
- **Conceptual Lens**: [Scale & Physics / Container Swap / Kinetic Human / Typographic Architecture / Screen UI / Negative Space Whisper]
- **Background Tone**: [Dark / Light] (Checkerboard Rhythm)

#### Copy-Pasteable Image Generation Prompt
```text
[Universal Prompt formatted for Midjourney / ChatGPT / Gemini / Flux:
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
