# Instagram SEO, Funnel & Copywriting Rules

This reference defines the keyword research strategy, campaign funnel narrative, hashtag architecture, and anti-AI-slop writing standards for drafting on-image micro-copy and Instagram captions.

---

## 1. Live Web Search Keyword Strategy

Before drafting any copy, research search terms that Instagram users and buyers actively use:

1. **Run `search_web`**:
   - Query: `"[niche/product] instagram trending keywords hashtags"` or `"[niche] buyer pain points common questions"`
   - Identify: High-volume primary search terms, secondary long-tail keywords, and popular community phrases.
2. **Offline Fallback (When Search is Unavailable)**:
   - Fall back on domain-specific keyword modeling:
     - Primary category name (e.g., `specialty coffee roaster`, `minimalist desk setup`)
     - High-intent modifier phrases (e.g., `best brew ratio for V60`, `ergonomic workspace guide`)
     - Problem/solution pairs (e.g., `bitter dark roast vs light roast`, `cable clutter fix`)

---

## 2. Campaign Funnel Narrative Across the 6 Tiles

Do not write captions as isolated descriptions of individual images. Structure all 6 captions as an integrated marketing journey:

```text
+-----------------------------------+-----------------------------------+-----------------------------------+
| TILE 1 (Upload #6)                | TILE 2 (Upload #5)                | TILE 3 (Upload #4)                |
| Top of Funnel: Awareness          | Mid-Funnel: Craft & Anatomy       | Mid-Funnel: Action Guide          |
| • Primary broad SEO keyword       | • Translates specs to benefits    | • High-save utility & how-to      |
| • Hook: Universal aspiration      | • Hook: Sensory or origin detail  | • Hook: Clear problem solve       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| TILE 4 (Upload #3)                | TILE 5 (Upload #2)                | TILE 6 (Upload #1)                |
| Brand Authority: Philosophy       | Conversion: Objection Bust        | Bottom of Funnel: Direct CTA      |
| • Founder ethos & core beliefs    | • Compares against alternatives   | • Community discussion prompt     |
| • Hook: Contrarian truth          | • Hook: Challenges misconception  | • Hook: Clear invitation to act   |
+-----------------------------------+-----------------------------------+-----------------------------------+
```

---

## 3. Instagram SEO Hook & Alt-Text Rules

1. **The 125-Character Opening Hook**:
   - The first sentence must appear before the Instagram "more" truncation point.
   - Front-load primary high-intent search keywords naturally into this line.
   - Example: *"Finding a specialty coffee roaster that sources washed Ethiopian beans changes your morning."*
2. **SEO Alt-Text**:
   - Provide a factual, keyword-rich visual description for accessibility and algorithmic indexing.
   - Avoid buzzwords; describe subject, colors, textures, and lighting plainly.

---

## 4. Strategic 3-Tier Hashtag Ladder (8–12 Tags Total)

Distribute hashtags into three distinct performance tiers:
- **Tier 1: Broad Category (2–3 tags)**: High volume (>500k posts) for broad topic indexing (e.g., `#SpecialtyCoffee #SlowLiving`).
- **Tier 2: Mid-Volume Niche & Buyer Intent (4–5 tags)**: 3–5 targeted niche tags (50k–500k posts) used by active enthusiasts and buyers (e.g., `#PouroverCoffee #MorningCoffeeRoutine #SingleOriginCoffee #HomeBarista`).
- **Tier 3: Hyper-Specific / Community / Branded (2–3 tags)**: Low competition (<50k posts) for immediate authority and community recognition (e.g., `#SlowCoffeeCo #WashedYirgacheffe #ArtisanPourOver`).

---

## 5. Humanizer & Zero-AI-Slop Writing Standards

All on-image micro-copy and caption copy must sound like a real person with a distinct point of view.

### Primary Rule
Read and apply the rules from:
- `~/.gemini/config/skills/humanizer/SKILL.md`
- `~/.gemini/config/skills/no-ai-slop/SKILL.md`

### Mandatory Fallback Anti-AI-Slop Rules
1. **Banned Words & Buzzwords**:
   - Never use: `delve`, `foster`, `leverage`, `utilize`, `streamline`, `robust`, `cutting-edge`, `paradigm shift`, `game-changer`, `tapestry`, `realm`, `beacon`, `elevate`, `supercharge`, `harness`, `meticulous`, `ever-evolving`, `transformative`, `multifaceted`.
2. **Banned Binary Contrasts ("Not X, but Y")**:
   - Cut: *"It's not just a product. It's an experience"* or *"This isn't about speed, it's about craft."*
   - Fix: State the claim directly: *"A slow pour-over changes the morning."*
3. **Banned Colon Reveals**:
   - Cut: *"The best part: it brews in 3 minutes."*
   - Fix: *"It brews in three minutes."*
4. **Banned Em-Dash Crutches**:
   - Do not use em-dashes (`—`) as an automatic sentence bridge. Use clean periods or natural commas.
5. **Banned Fake-Insight Setups & Kickers**:
   - Cut: *"What most people get wrong:"*, *"Here's the secret:"*, *"Read that again."*, *"Let that sink in."*
6. **On-Image Micro-Copy**:
   - Strictly **6–8 words maximum**.
   - Anchored top-center or bottom-center with 10–15% safe margins.

---

## 6. `captions.txt` Compilation Template

Inside the image output directory, format `captions.txt` in reverse-chronological upload order (**Upload #1 through Upload #6**):

```text
================================================================================
UPLOAD #1 (TILE 6 - Bottom-Right)
Title: [Catchy Tile Name]
Funnel Stage: [Bottom of Funnel / Direct Action]
On-Image Text: "[Micro-Copy Text]"
--------------------------------------------------------------------------------
SEO HOOK & CAPTION:
[Full Humanized Caption Text with Primary Keywords before the fold]

STRATEGIC HASHTAGS (3-Tier Ladder):
Broad Category: #[tag1] #[tag2]
Mid-Volume Niche: #[tag3] #[tag4] #[tag5]
Hyper-Specific: #[tag6] #[tag7]

INSTAGRAM SEO ALT-TEXT:
[Descriptive, Keyword-Rich Alt-Text Description]
================================================================================
```
