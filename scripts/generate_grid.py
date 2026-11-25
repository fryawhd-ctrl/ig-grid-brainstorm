#!/usr/bin/env python3
"""
generate_grid.py - Image Generator for ig-grid-brainstorm
Supports generating:
1. Compiled 3x2 Master Grid (grid_master.png) in 12:10 / 6:5 (or 5:4 preset) - DEFAULT.
2. Individual 4:5 vertical tiles (tile_01.png to tile_06.png) with 10s cooldown and 35s retries.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path

def generate_image(client, model_name, prompt, output_path, aspect_ratio="5:4", max_retries=3, retry_delay=35):
    """Generates an image with retry logic for 503 / capacity limits."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[*] Generating {output_path.name} (Attempt {attempt}/{max_retries}, AR {aspect_ratio})...")
            response = client.models.generate_images(
                model=model_name,
                prompt=prompt,
                config=dict(
                    number_of_images=1,
                    aspect_ratio=aspect_ratio,
                    output_mime_type="image/png"
                )
            )
            if response and response.generated_images:
                image_bytes = response.generated_images[0].image.image_bytes
                with open(output_path, "wb") as f:
                    f.write(image_bytes)
                print(f"[+] Saved image to {output_path}")
                return True
        except Exception as e:
            err_msg = str(e)
            print(f"[!] Warning on {output_path.name} attempt {attempt}: {err_msg}")
            if "503" in err_msg or "CAPACITY" in err_msg.upper() or "RESOURCE_EXHAUSTED" in err_msg.upper():
                if attempt < max_retries:
                    print(f"[*] Capacity limit reached. Pausing {retry_delay}s before retry...")
                    time.sleep(retry_delay)
                    continue
            if attempt == max_retries:
                print(f"[-] {output_path.name} failed after {max_retries} attempts.")
                return False
    return False

def main():
    parser = argparse.ArgumentParser(description="Generate Instagram Grid Assets")
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--mode", choices=["master", "individual", "all"], default="master",
                        help="Generation mode: 'master' (default: 3x2 grid_master.png), 'individual' (6 tiles), or 'all'")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir = Path(data.get("output_dir", "./generated_grid"))
    output_dir.mkdir(parents=True, exist_ok=True)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[-] GEMINI_API_KEY not found in environment.")
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

    # 1. Master Grid Generation (Default)
    if args.mode in ["master", "all"]:
        master_prompt = data.get("master_prompt")
        if master_prompt:
            master_path = output_dir / "grid_master.png"
            success = generate_image(client, model_name, master_prompt, master_path, aspect_ratio="5:4")
            if not success and args.mode == "master":
                sys.exit(1)
        else:
            print("[-] No 'master_prompt' found in config.")
            if args.mode == "master":
                sys.exit(1)

    # 2. Individual Tile Generation (Optional)
    if args.mode in ["individual", "all"]:
        tiles = data.get("tiles", [])
        if len(tiles) != 6:
            print(f"[!] Warning: Expected 6 tiles, received {len(tiles)}")

        for idx, tile in enumerate(tiles, start=1):
            tile_name = f"tile_{idx:02d}.png"
            tile_path = output_dir / tile_name
            prompt = tile.get("prompt", "")

            success = generate_image(client, model_name, prompt, tile_path, aspect_ratio="4:5")
            if not success:
                print(f"[-] Aborting individual generation at Tile {idx}.")
                sys.exit(1)

            if idx < len(tiles):
                print("[*] Pausing 10s before next tile to maintain quota stability...")
                time.sleep(10)

    print(f"[+] Generation complete in {output_dir}")
    sys.exit(0)

if __name__ == "__main__":
    main()
