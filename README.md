# Instagram Grid Brainstormer (`ig-grid-brainstorm`)

An **Antigravity Custom Skill** that transforms a single anchor image into an aesthetic, high-converting 6-tile Instagram profile grid (2 rows × 3 columns).

---

## Features

- **6-Tile Cohesive Thematic Grid**: Plans 6 individual standalone posts that look stunning together on your Instagram profile feed.
- **Master Visual System**:
  - **Automated Color Extraction**: Extracts a 5-color Hex palette using the **60-30-10 distribution rule** (Primary Base, Secondary, Accent, Dark Neutral, Light Neutral) matching the mood and lighting of your anchor image.
  - **Consistent Typography Pairings**: Curated font pairings (Google Fonts & Canva/Figma equivalents) with exact hierarchy and letter-spacing rules.
- **Adaptive Content Angles**: Dynamic 6-angle framework tailored to your image domain (Product, Lifestyle, Personal Brand, Educational, or Artistic):
  - **Tile 1 (Top-Left / Upload #6)**: Hero Statement & Big Vision
  - **Tile 2 (Top-Center / Upload #5)**: Macro Texture, Detail & Craftsmanship
  - **Tile 3 (Top-Right / Upload #4)**: Actionable Guide / Practical How-To
  - **Tile 4 (Bottom-Left / Upload #3)**: Philosophy / Mindset Reflection
  - **Tile 5 (Bottom-Center / Upload #2)**: Contrarian Take / Common Myth
  - **Tile 6 (Bottom-Right / Upload #1)**: Community Conversation & Engagement
- **Reverse-Chronological Upload Sequence**: Foolproof upload sequence (1 to 6) so your profile grid aligns properly as new uploads push older posts to the right.
- **Minimalist High-Converting Captions**:
  - Scroll-stopping hook (<125 characters, before the fold).
  - Skimmable value body.
  - Single-action CTA or discussion question.
  - 5–8 targeted hashtags (niche + topic).
  - Instagram SEO Alt-Text for accessibility and search indexing.

---

## Directory Structure

```text
ig-grid-brainstorm/
├── SKILL.md                          # Main skill instruction file with frontmatter
├── README.md                         # Repository documentation
├── LICENSE                           # MIT License
├── references/
│   ├── grid-archetypes.md            # Category-specific 6-angle matrices
│   └── typography-pairings.md        # Curated font pairings by aesthetic mood
└── examples/
    └── sample-grid-output.md         # End-to-end sample run (Artisanal Coffee Roastery)
```

---

## Installation

### Option 1: Global Installation (Available across all chats and workspaces)
Clone or copy this folder into your global Gemini/Antigravity configuration:
```bash
# Windows
git clone https://github.com/<your-username>/ig-grid-brainstorm.git "$HOME\.gemini\config\skills\ig-grid-brainstorm"

# macOS / Linux
git clone https://github.com/<your-username>/ig-grid-brainstorm.git ~/.gemini/config/skills/ig-grid-brainstorm
```

### Option 2: Project / Workspace Installation
Place the folder inside your project's `.agents/skills/` directory:
```bash
mkdir -p .agents/skills
git clone https://github.com/<your-username>/ig-grid-brainstorm.git .agents/skills/ig-grid-brainstorm
```

---

## How to Use

Once installed, simply provide an image in your Antigravity conversation and prompt:

> *"Here is an image: `[image path or upload]`. Brainstorm an Instagram grid for it."*

---

## License

[MIT License](LICENSE)
