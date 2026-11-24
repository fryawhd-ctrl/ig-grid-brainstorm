---
name: ig-grid-brainstorm
description: >-
  Brainstorm a single anchor image into a cohesive 6-post Instagram Grid (2 rows x 3 columns).
  Use this skill whenever the user provides an image (or image concept/path) and asks to create,
  plan, or brainstorm an Instagram grid, feed layout, 6 matching posts, or a cohesive visual campaign
  sharing the same color tone, consistent typography, and individual standalone captions.
---

# Instagram Grid Brainstormer (`ig-grid-brainstorm`)

Transform a single anchor image into an aesthetic, high-converting 6-tile Instagram profile grid (2 rows × 3 columns).

Each post works as a high-value standalone post while harmonizing into a unified visual identity on the user's profile feed—sharing an extracted color palette, consistent typography pairings, and structured individual captions.

---

## The 6-Tile Instagram Grid Architecture

Instagram feeds display posts in 3 columns. A 6-post grid occupies two complete rows:

```text
+-------------------+-------------------+-------------------+
|      TILE 1       |      TILE 2       |      TILE 3       |  <-- ROW 1 (Top Row on Profile)
|    [Top-Left]     |   [Top-Center]    |    [Top-Right]    |
+-------------------+-------------------+-------------------+
|      TILE 4       |      TILE 5       |      TILE 6       |  <-- ROW 2 (Bottom Row on Profile)
|   [Bottom-Left]   |  [Bottom-Center]  |  [Bottom-Right]   |
+-------------------+-------------------+-------------------+
```

### Critical Upload Sequencing (Reverse-Chronological)
Instagram pushes older posts to the right and down as new ones are published. To ensure the final profile view renders correctly:

1. **Upload #1** ➔ **Tile 6** (Bottom-Right)
2. **Upload #2** ➔ **Tile 5** (Bottom-Center)
3. **Upload #3** ➔ **Tile 4** (Bottom-Left)
4. **Upload #4** ➔ **Tile 3** (Top-Right)
5. **Upload #5** ➔ **Tile 2** (Top-Center)
6. **Upload #6** ➔ **Tile 1** (Top-Left)

---

## Step-by-Step Procedure

### Step 1: Anchor Image Ingestion & Aesthetic Analysis
When the user supplies an image (file path, uploaded image, or detailed visual description):

1. **Category Detection**: Identify the image genre:
   - **Product / E-commerce** (physical goods, packaging, craftsmanship)
   - **Personal Brand / Creator** (portraits, speaking, lifestyle, behind-the-scenes)
   - **Lifestyle / Hospitality / Travel** (interiors, food, destinations, atmosphere)
   - **Educational / B2B / SaaS** (diagrams, workspaces, books, workflows)
   - **Artistic / Portfolio** (photography, illustration, architecture, fine art)
2. **Atmosphere & Lighting**: Note the mood (e.g., warm golden hour, moody low-key, airy Scandinavian, high-contrast brutalist, vibrant neon).
3. **Core Subject & Narrative Anchors**: Identify 3-4 focal elements, textures, or sub-themes in the image that can be magnified into individual post topics.

---

### Step 2: Master Visual System Definition

Establish the design rules that visually unify all 6 posts:

#### 1. Color Palette (60-30-10 Rule)
Extract 5 hex colors directly from the anchor image:
- **Primary Dominant (60%)**: Background/canvas foundation (e.g., `#F4EFEA`)
- **Secondary Structural (30%)**: Secondary elements, containers, cards (e.g., `#3C4A3E`)
- **Accent Focal (10%)**: High-contrast pop for badges, focal points, buttons (e.g., `#E07A5F`)
- **Dark Neutral**: High-readability headline/text color (e.g., `#1E201E`)
- **Light Neutral**: Clean highlight / high-contrast text on dark backgrounds (e.g., `#FAF8F5`)

*(Allow the user to override with their existing brand palette if desired).*

#### 2. Consistent Typography Pairings
Provide two curated font pairing options matching the image mood (refer to [Typography Pairings Library](./references/typography-pairings.md)):
- **Option A (Primary Recommendation)**: Headline Font + Body Font
- **Option B (Alternative Mood)**: Headline Font + Body Font
- Specify exact weights, capitalization rules (e.g., ALL CAPS headers vs. sentence case editorial), and letter-spacing for on-image graphics.

#### 3. Visual Rhythm & Motif Rules
Ensure variety across the 6 tiles so the grid does not look monolithic. Balance:
- **Macro / Detail shot** vs. **Wide scene**
- **Bold typography-heavy tile** vs. **Clean image-dominant tile**
- **Negative space breathing room** across alternating columns.

---

### Step 3: Adaptive 6-Tile Angle Brainstorming

Formulate the 6 post angles based on the detected category (refer to [Grid Content Archetypes](./references/grid-archetypes.md)):

- **Tile 1 (Top-Left / Upload #6)**: Hero Statement / The Big Vision
- **Tile 2 (Top-Center / Upload #5)**: Deep-Dive Detail / The Anatomy / Macro Focus
- **Tile 3 (Top-Right / Upload #4)**: Actionable Guide / Quick How-To / Process
- **Tile 4 (Bottom-Left / Upload #3)**: Philosophy / Mindset / Evocative Quote
- **Tile 5 (Bottom-Center / Upload #2)**: Mistake / Contrarian Take / The "Before vs After"
- **Tile 6 (Bottom-Right / Upload #1)**: Community Conversation / Discussion Starter / CTA

---

### Step 4: Individual Post Blueprint Generation

For every tile from 1 to 6, generate a complete blueprint adhering strictly to this schema:

```markdown
### Tile [N]: [Catchy Tile Name]
- **Grid Position**: [Row X, Column Y] | **Upload Order**: Upload #[M] of 6
- **Content Angle**: [Hero / Detail / Guide / Quote / Contrarian / Conversation]

#### Visual & Graphic Direction
- **Composition & Framing**: [Exact description of visual layout, background, focal object]
- **Color Distribution**: [Which extracted hex codes are used for background, accents, subject]
- **On-Image Text Overlay**:
  - *Headline*: "[Bold Short Text]" ([Font Name], [Weight], [Color Hex])
  - *Subtext / Label*: "[Supporting Label]" ([Font Name], [Weight], [Color Hex])
  - *Visual Cue*: [Arrow, icon, badge, border treatment]

#### Individual Caption (Minimalist High-Converting Formula)
**[Hook Line <125 characters that stops the scroll before the 'more' fold]**

[1-3 concise, punchy paragraphs or bullet points delivering immediate takeaway/context]

[Clear single-action CTA or engagement question]

---
**Hashtags**: #[tag1] #[tag2] #[tag3] #[tag4] #[tag5] #[tag6] #[tag7]
**Instagram Alt-Text**: [Descriptive, SEO-rich visual description for accessibility]
```

---

### Step 5: Visual Matrix & Upload Checklist Summary

Conclude every execution with:
1. **The ASCII/Markdown Grid Matrix**: A quick-reference visual preview showing which post sits where on the 3x2 grid.
2. **Reverse-Chronological Upload Checklist**: Clear, foolproof upload sequence (1 to 6) to avoid posting out of order.
3. **Design Handoff Tips**: Quick guidance for assembling in Canva, Photoshop, or Figma (canvas dimensions `1080x1080` square or `1080x1350` 4:5 portrait, keeping key visual elements within the 1:1 center crop for feed view).

---

## References & Examples

- **[Typography Pairings Reference](./references/typography-pairings.md)**: Curated font pairings by aesthetic mood.
- **[Content Archetypes Reference](./references/grid-archetypes.md)**: Category-specific 6-angle matrix variations.
- **[Complete Sample Blueprint](./examples/sample-grid-output.md)**: End-to-end demonstration from input image to finished 6-post grid.
