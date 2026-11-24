#!/usr/bin/env python3
"""
Sequential Image Generator for 6-Tile Instagram Grids
Handles strict 1-image-per-tile generation, 10s cooldowns, and 35s retry logic for 503 / capacity limits.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path

def generate_tile(client, model_name, prompt, output_path, tile_num, max_retries=3, retry_delay=35):
    """Generates a single image with built-in retry logic."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[*] Generating Tile {tile_num} (Attempt {attempt}/{max_retries})...")
            # Using google-genai or google.generativeai if available
            response = client.models.generate_images(
                model=model_name,
                prompt=prompt,
                config=dict(
                    number_of_images=1,
                    aspect_ratio="4:5",
                    output_mime_type="image/png"
                )
            )
            if response and response.generated_images:
                image_bytes = response.generated_images[0].image.image_bytes
                with open(output_path, "wb") as f:
                    f.write(image_bytes)
                print(f"[+] Saved Tile {tile_num} to {output_path}")
                return True
        except Exception as e:
            err_msg = str(e)
            print(f"[!] Warning on Tile {tile_num} attempt {attempt}: {err_msg}")
            if "503" in err_msg or "CAPACITY" in err_msg.upper() or "RESOURCE_EXHAUSTED" in err_msg.upper():
                if attempt < max_retries:
                    print(f"[*] Capacity limit reached. Pausing {retry_delay}s before retry...")
                    time.sleep(retry_delay)
                    continue
            if attempt == max_retries:
                print(f"[-] Tile {tile_num} failed after {max_retries} attempts.")
                return False
    return False

def main():
    parser = argparse.ArgumentParser(description="Generate 6 Instagram Grid Tiles Sequentially")
    parser.add_argument("--config", required=True, help="Path to JSON file with prompts and output dir")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir = Path(data.get("output_dir", "./generated_grid"))
    output_dir.mkdir(parents=True, exist_ok=True)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[-] GEMINI_API_KEY not found in environment. Please use native image-generator or provide key.")
        sys.exit(2)

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
    except ImportError:
        try:
            from google import generativeai as client
            client.configure(api_key=api_key)
        except ImportError:
            print("[-] google-genai library not installed.")
            sys.exit(3)

    model_name = data.get("model", "imagen-3.0-generate-002")
    tiles = data.get("tiles", [])

    if len(tiles) != 6:
        print(f"[!] Warning: Expected 6 tiles, received {len(tiles)}")

    successful = 0
    for idx, tile in enumerate(tiles, start=1):
        tile_name = f"tile_{idx:02d}.png"
        tile_path = output_dir / tile_name
        prompt = tile.get("prompt", "")

        success = generate_tile(client, model_name, prompt, tile_path, idx)
        if not success:
            print(f"[-] Aborting generation loop at Tile {idx}.")
            sys.exit(1)

        successful += 1
        if idx < len(tiles):
            print("[*] Pausing 10s before next tile to maintain quota stability...")
            time.sleep(10)

    print(f"[+] Successfully generated all {successful} tiles in {output_dir}")
    sys.exit(0)

if __name__ == "__main__":
    main()
