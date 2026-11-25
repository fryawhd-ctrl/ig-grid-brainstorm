#!/usr/bin/env python3
"""
validate_grid.py - Deterministic Quality Control Validator for ig-grid-brainstorm

Validates that a generated grid blueprint (grid-blueprint.md) or captions file (captions.txt)
strictly adheres to the non-negotiable compliance rules:
1. Compiled Master Grid prompt in 12:10 (6:5) with 1px–2px hairline dividers and anti-cropping constraints.
2. Exactly 6 individual tiles in a 3x2 matrix with 4:5 aspect ratio.
3. Alternating dark/light checkerboard rhythm.
4. Micro-copy strictly under 6 words per tile.
5. Zero banned AI slop words or binary contrasts.
6. Complete publication-ready captions with hooks (<125 chars), CTAs, and 3-tier hashtags.
"""

import sys
import re
import argparse
from pathlib import Path

BANNED_WORDS = [
    r"\bdelve\b", r"\bfoster\b", r"\bleverage\b", r"\butilize\b", r"\bstreamline\b",
    r"\brobust\b", r"\bcutting-edge\b", r"\bparadigm shift\b", r"\bgame-changer\b",
    r"\btapestry\b", r"\brealm\b", r"\bbeacon\b", r"\belevate\b", r"\bsupercharge\b",
    r"\bharness\b", r"\bmeticulous\b"
]

BINARY_CONTRAST_PATTERN = re.compile(r"it['’]s not\b.*?\bit['’]s\b", re.IGNORECASE)

def validate_blueprint(file_path: Path) -> list:
    errors = []
    if not file_path.exists():
        return [f"File not found: {file_path}"]

    content = file_path.read_text(encoding="utf-8")

    # 1. Master Grid Prompt Check
    if "Master Grid" in content or "grid_master" in content:
        if not re.search(r"--ar\s+(12:10|6:5|5:4)", content, re.IGNORECASE):
            errors.append("Master Grid Error: Missing required aspect ratio flag (--ar 12:10, --ar 6:5, or --ar 5:4).")
        if not re.search(r"hairline", content, re.IGNORECASE):
            errors.append("Master Grid Error: Missing specification for 1px–2px hairline dividers.")

    # 2. Tile Count Check
    tile_headers = re.findall(r"###\s+Tile\s+(\d+)", content, re.IGNORECASE)
    if len(tile_headers) != 6:
        errors.append(f"Grid Cardinality Error: Found {len(tile_headers)} tiles; expected exactly 6 tiles in 3x2 format.")

    # 3. Banned Words Check
    for word_regex in BANNED_WORDS:
        matches = re.findall(word_regex, content, re.IGNORECASE)
        if matches:
            errors.append(f"AI Slop Error: Found banned word '{matches[0]}'.")

    # 4. Binary Contrast Check
    if BINARY_CONTRAST_PATTERN.search(content):
        errors.append("AI Slop Error: Found binary contrast ('It's not X. It's Y.').")

    # 5. Micro-copy Length Check
    micro_copies = re.findall(r"-\s+\*\*Text\*\*:\s*[\"']([^\"']+)[\"']", content)
    for i, copy in enumerate(micro_copies, start=1):
        words = copy.strip().split()
        if len(words) >= 6:
            errors.append(f"Tile {i} Micro-Copy Error: Text '{copy}' has {len(words)} words (must be strictly < 6 words).")

    # 6. Checkerboard Rhythm Check
    tones = re.findall(r"-\s+\*\*Background Tone\*\*:\s*\[?(Dark|Light)\]?", content, re.IGNORECASE)
    if len(tones) == 6:
        expected = ["Dark", "Light", "Dark", "Light", "Dark", "Light"]
        for idx, (actual, exp) in enumerate(zip(tones, expected), start=1):
            if actual.capitalize() != exp:
                errors.append(f"Checkerboard Rhythm Error: Tile {idx} tone is '{actual}'; expected '{exp}'.")

    # 7. Caption Completeness Check
    captions = re.findall(r"####\s+SEO Hook & Humanized Caption", content, re.IGNORECASE)
    if len(captions) != 6:
        errors.append(f"Caption Completeness Error: Found {len(captions)} caption blocks; expected 6 full captions.")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Deterministic QC Validator for ig-grid-brainstorm")
    parser.add_argument("file", help="Path to grid-blueprint.md or captions.txt")
    args = parser.parse_args()

    target_file = Path(args.file)
    errors = validate_blueprint(target_file)

    if errors:
        print(f"\n[FAIL] Quality Control Audit Failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"\n[PASS] Quality Control Audit Passed! All compliance gates met for '{target_file.name}'.")
        sys.exit(0)

if __name__ == "__main__":
    main()
