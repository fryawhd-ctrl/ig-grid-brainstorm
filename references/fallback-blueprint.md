# Fallback Blueprint Export Template (`grid-blueprint.md`)

This template defines the structure of the standalone Markdown file `grid-blueprint.md` generated when automated image generation fails after retry attempts or when an API key is unavailable.

---

## Output Path & Placement
Save `grid-blueprint.md` alongside `captions.txt` in the local output directory:
- `<Artifact Directory Path>/generated_grid/grid-blueprint.md` (or `<Workspace>/generated_grid/grid-blueprint.md`)

---

## File Contents Template

```markdown
# 6-Tile Instagram Grid Campaign Blueprint

Use this complete blueprint to generate the 6 matching tiles in Gemini, ChatGPT (DALL-E 3), Midjourney, or design tools (Canva/Figma).

---

## 1. Global Campaign Specifications

- **Campaign Theme**: [Overarching Campaign Narrative]
- **Aspect Ratio**: 4:5 Vertical (`1080x1350 px`) with 1:1 Square Center-Crop Safe Area (`1080x1080 px`)
- **Safe Margins**: Keep all product silhouettes, text overlays, and badges at least 10–15% inside borders.

### Extracted 5-Color Palette (60-30-10 Rule)
- **Primary Dominant (60%)**: `[#HEX]` (Canvas Foundation)
- **Secondary Structural (30%)**: `[#HEX]` (Frames, Shadows, Accents)
- **Accent Focal (10%)**: `[#HEX]` (Badges & Highlight Pops)
- **Dark Neutral**: `[#HEX]` (Text on light tiles)
- **Light Neutral**: `[#HEX]` (Text on dark tiles)

### Checkerboard Grid Layout Plan
- **Row 1**: Tile 1 (Dark) — Tile 2 (Light) — Tile 3 (Dark)
- **Row 2**: Tile 4 (Light) — Tile 5 (Dark) — Tile 6 (Light)

### Unified Typography Specs
- **Font Family**: [Single Font Family Name, e.g. Plus Jakarta Sans]
- **Headline**: Bold (700) or Extra-Bold (800)
- **Micro-Copy Overlay**: Semi-Bold (600), Uppercase, tracking `+1.5px`
- **Caption / Body**: Regular (400)

---

## 2. 3x2 Profile Grid Map & Posting Schedule

```text
+-----------------------+-----------------------+-----------------------+
|        TILE 1         |        TILE 2         |        TILE 3         |
|  [Hero Launch]        |  [Craft & Anatomy]    |  [Action How-To]      |  <-- ROW 1 (Top Row on Feed)
|     (Upload #6)       |      (Upload #5)      |      (Upload #4)      |
+-----------------------+-----------------------+-----------------------+
|        TILE 4         |        TILE 5         |        TILE 6         |
|  [Brand Philosophy]   |  [Objection Debunk]   |  [Community CTA]      |  <-- ROW 2 (Bottom Row on Feed)
|     (Upload #3)       |      (Upload #2)      |      (Upload #1)      |
+-----------------------+-----------------------+-----------------------+
```

### Posting Schedule (Reverse-Chronological)
1. **Upload #1** ➔ **Tile 6** (Bottom-Right)
2. **Upload #2** ➔ **Tile 5** (Bottom-Center)
3. **Upload #3** ➔ **Tile 4** (Bottom-Left)
4. **Upload #4** ➔ **Tile 3** (Top-Right)
5. **Upload #5** ➔ **Tile 2** (Top-Center)
6. **Upload #6** ➔ **Tile 1** (Top-Left)

---

## 3. Tile-by-Tile Generation Prompts & Copy

### Tile [N]: [Catchy Tile Name]
- **Grid Position**: Row [X], Column [Y] | **Upload Order**: Upload #[M] of 6
- **Funnel Stage**: [Awareness / Craft / How-To / Philosophy / Objection / Community CTA]
- **Composition Style**: [Hero Shot / Metaphor Placement / Human Element / Minimal Negative Space]
- **Background Tone**: [Dark / Light] (Checkerboard Rhythm)

#### Copy-Pasteable Image Generation Prompt (Gemini / ChatGPT / Midjourney)
```text
[Detailed prompt describing:
1. Product Fidelity: The exact product subject, materials, surface textures, and reflections matching the reference image.
2. Surreal Metaphor & Setting: Preserves the exact surreal scale, physical interactions, and unexpected environment from the concept (e.g. suspended mid-air, embedded in a ring box, miniature diorama, or floating in 80% negative space). Do NOT simplify into generic tabletop or studio product photography.
3. Typography & Graphic Placement: Notes typography geometry if rendered directly (e.g. curved type, split punchline, or UI badge).
4. Color & Contrast: Strict 2-3 color palette enforcement with exact hex values ([#HEX] dark/saturated tone vs [#HEX] light/clean space for checkerboard rhythm).
5. Aspect ratio & margins: --ar 4:5 (portrait 1080x1350) with 10-15% safe inner margin.]
```

#### On-Image Micro-Copy Overlay
- **Text**: `"[Witty micro-copy under 6 words]"`
- **Graphic Placement**: [Curved around object / Split top-and-bottom / In UI chat bubble / Overlapping background type], [Font Family], [Font Weight], [Hex Color]

#### SEO Hook & Humanized Caption
**[Opening Hook Line <125 characters with primary keywords]**

[1-3 concise, punchy paragraphs with zero AI slop]

[Clear single-action CTA]

#### Strategic Hashtags (3-Tier Ladder)
- **Broad Category**: #[tag1] #[tag2] #[tag3]
- **Mid-Volume Niche**: #[tag4] #[tag5] #[tag6] #[tag7]
- **Hyper-Specific / Branded**: #[tag8] #[tag9] #[tag10]

#### Instagram SEO Alt-Text
[Descriptive, keyword-rich visual description for accessibility and search indexing]
```
