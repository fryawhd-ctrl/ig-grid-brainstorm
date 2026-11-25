# Autonomous Quality Control & Gate Check (`quality-control.md`)

This reference defines the **autonomous, zero-human-interference quality control gate** for `ig-grid-brainstorm`. Before presenting any grid strategy, blueprints, or captions to the user, the executing agent (whether Claude, ChatGPT, Gemini CLI, Antigravity, or custom agents) must internally evaluate its draft against this rubric and self-correct any non-compliant components.

---

## 1. The 6 Non-Negotiable Compliance Gates

### Gate 1: Mandatory Stage Enforcement (Anti-Skipping)
- **Rule**: The agent must NEVER skip directly to image prompts.
- **Verification**:
  - [x] Step 1 Research executed (keywords, pain points, trending hashtags identified).
  - [x] Step 2 Visual Blueprints formulated (palette, typography, 6 distinct surreal concepts).
  - [x] Step 3 Full Captions drafted for all 6 tiles.
- **Failure Trigger**: Jumping straight to image generation prompts without presenting the visual system, keyword research, or full post captions.

### Gate 2: Strict 3 × 2 Grid Composition & Reverse-Chronological Upload
- **Rule**: Exactly 6 tiles arranged in a 2-row by 3-column feed profile grid.
- **Verification**:
  - [x] **Row 1 (Top Row on Profile)**: Tile 1 (Top-Left), Tile 2 (Top-Center), Tile 3 (Top-Right).
  - [x] **Row 2 (Bottom Row on Profile)**: Tile 4 (Bottom-Left), Tile 5 (Bottom-Center), Tile 6 (Bottom-Right).
  - [x] **Reverse-Chronological Upload Order**:
    - Upload #1 ➔ Tile 6 (Bottom-Right)
    - Upload #2 ➔ Tile 5 (Bottom-Center)
    - Upload #3 ➔ Tile 4 (Bottom-Left)
    - Upload #4 ➔ Tile 3 (Top-Right)
    - Upload #5 ➔ Tile 2 (Top-Center)
    - Upload #6 ➔ Tile 1 (Top-Left)
- **Failure Trigger**: Outputting 3, 4, 5, or 9 tiles; omitting upload sequence numbers; confusing feed position with upload order.

### Gate 3: 100% Complete Instagram Captions (Zero Placeholders)
- **Rule**: Every single tile (Tile 1 through Tile 6) MUST have a full, publication-ready caption.
- **Verification**:
  - [x] **Opening Hook**: Under 125 characters, includes primary SEO keyword naturally before the truncation fold.
  - [x] **Value Body**: 1–3 punchy paragraphs without fluff, delivering genuine narrative or educational value.
  - [x] **Single-Action CTA**: Direct call to action (save, comment, share, or click link).
  - [x] **3-Tier Hashtags (8–12 Total)**:
    - 2–3 Broad category tags
    - 4–5 Mid-volume niche & buyer-intent tags
    - 2–3 Hyper-specific or branded tags
  - [x] **Instagram SEO Alt-Text**: Included for search indexing and accessibility.
- **Failure Trigger**: Writing "Caption: [Insert caption here]", summarizing tiles with 1-line descriptions, omitting hashtags, or providing captions for only 2 or 3 tiles.

### Gate 4: Checkerboard Contrast Rhythm
- **Rule**: Adjacent tiles must strictly alternate between dark/saturated backgrounds and light/clean negative-space backgrounds.
- **Verification**:
  - [x] **Row 1**: Tile 1 (Dark) ➔ Tile 2 (Light) ➔ Tile 3 (Dark).
  - [x] **Row 2**: Tile 4 (Light) ➔ Tile 5 (Dark) ➔ Tile 6 (Light).
  - [x] No two horizontally or vertically adjacent tiles share the same background tone.
- **Failure Trigger**: Consecutive dark or consecutive light tiles; monochrome flat backgrounds across the entire grid.

### Gate 5: Surreal Metaphor & Scale Diversity (Anti-Tabletop)
- **Rule**: Zero repeated camera angles or catalog studio setups. The physical product must match the reference image 100%, but its environment must be conceptual.
- **Verification**:
  - [x] **Extreme Scale Variance**: At least ONE tile scales the product to <15% of the frame surrounded by vast negative space (Lens 6), and at least ONE tile features a macro hero perspective.
  - [x] **Zero Tabletop Repetition**: No default studio podiums, countertop displays, or standard flat-lays.
  - [x] **Distinct Conceptual Lenses**: Each tile utilizes a different lens from `references/grid-archetypes.md`.
- **Failure Trigger**: Two or more tiles using the same camera angle, prop logic, or sitting on a flat surface.

### Gate 6: On-Image Micro-Copy & Anti-AI-Slop
- **Rule**: On-image text overlays must be ultra-concise (<6 words) and written in natural, sharp human language.
- **Verification**:
  - [x] **Word Count**: Every on-image micro-copy string is strictly **5 words or fewer** (strictly under 6 words).
  - [x] **No Banned AI Words**: Zero instances of `delve`, `foster`, `leverage`, `utilize`, `streamline`, `robust`, `cutting-edge`, `paradigm shift`, `game-changer`, `tapestry`, `realm`, `beacon`, `elevate`, `supercharge`, `harness`, or `meticulous`.
  - [x] **No Binary Contrasts**: No *"It's not X. It's Y."*
  - [x] **No Colon Reveals or Em-Dash Overuse**: Direct assertions only.
- **Failure Trigger**: Micro-copy exceeding 6 words; generic slogans like *"Unleash Your True Potential"*; sentences starting with *"In a world where..."*.

---

## 2. Autonomous Pre-Flight Self-Audit Rubric

Before outputting to the user, the agent evaluates this internal binary checklist:

| Check Item | Target Standard | Pass Condition |
| :--- | :--- | :---: |
| **Stage Completeness** | Steps 1, 2, 3 fully drafted | `PASS` |
| **Grid Cardinality** | Exactly 6 tiles in 3×2 layout | `PASS` |
| **Upload Sequence** | Upload #1 (Tile 6) to #6 (Tile 1) mapped | `PASS` |
| **Checkerboard Rhythm** | Row 1: D-L-D / Row 2: L-D-L alternating | `PASS` |
| **Scale Diversity** | At least one <15% scale negative-space tile | `PASS` |
| **Zero Catalog Setup** | 6 distinct conceptual/surreal metaphors | `PASS` |
| **Micro-Copy Limit** | Strictly under 6 words per tile | `PASS` |
| **Full Captions** | 6 complete captions with hooks, CTAs, tags, alt-text | `PASS` |
| **Anti-Slop Cleanliness** | Zero banned words, binary contrasts, colon reveals | `PASS` |

---

## 3. Autonomous Self-Healing Directive

If ANY item in the pre-flight audit evaluates to `FAIL`:
1. **DO NOT emit the failed response to the user.**
2. **Isolate the defect**:
   - *If captions are truncated or missing*: Draft the missing full-funnel captions immediately before completing the turn.
   - *If micro-copy is >= 6 words*: Rewrite the overlay to be punchy, colloquial, and 3–5 words.
   - *If two tiles share tabletop podiums*: Replace one with a gravity-defying, container-swap, or UI-play lens.
   - *If checkerboard rhythm is broken*: Flip the background tone of the offending tile to restore the dark/light pattern.
3. **Re-audit silently**: Once all 9 checks pass, proceed to Step 4 presentation.
