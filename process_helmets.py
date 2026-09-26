#!/usr/bin/env python3
"""
Extract and process helmet data from Canva slides 122-153.
"""

import json
import subprocess
import time
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import hashlib

OUTPUT_DIR = Path("/Users/joel/git/mmcc-helmet-library/scrape")
IMAGES_DIR = OUTPUT_DIR / "images"
DATA_FILE = OUTPUT_DIR / "data_122-153.jsonl"
SKIPPED_FILE = OUTPUT_DIR / "skipped_122-153.jsonl"

# Ensure directories exist
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

# Initialize files
DATA_FILE.write_text("")
SKIPPED_FILE.write_text("")

def run_bash(cmd):
    """Run a bash command and return output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def extract_page_data(page_num):
    """
    Extract helmet data from a single page.
    Uses the browser to navigate and extract.
    """
    print(f"\n{'='*60}")
    print(f"Processing slide {page_num}")
    print('='*60)

    # Navigate to slide
    url = f"https://www.canva.com/design/DAGYU40jp3k/pbXHuLKVEW0Jy-ETSXrxTg/view#{page_num}"
    print(f"Navigating to slide {page_num}...")

    # We'll use AppleScript or curl to do the navigation
    # For now, we'll assume the browser is open and we control it via CLI

    return None

def download_images(urls, page_num):
    """Download images from URLs."""
    downloaded = []

    for idx, url in enumerate(urls, 1):
        filename = f"p{page_num}-{idx}.png"
        filepath = IMAGES_DIR / filename

        print(f"Downloading image {idx}/{len(urls)} to {filepath}...")

        # Use curl with referer to download from Canva
        cmd = f'curl -sS -H "Referer: https://www.canva.com/" -o "{filepath}" "{url}"'
        result = run_bash(cmd)

        if filepath.exists():
            print(f"  Downloaded: {filepath}")
            downloaded.append(filename)
        else:
            print(f"  Failed to download")

    return downloaded

def save_helmet_data(page_num, name, maker, approvable, eras, images):
    """Save helmet data to JSONL file."""
    data = {
        "page": page_num,
        "name": name,
        "maker": maker,
        "approvable": approvable,
        "eras": eras,
        "images": images,
        "links": []
    }

    with open(DATA_FILE, 'a') as f:
        f.write(json.dumps(data) + '\n')

    print(f"Saved data for {name}")

def save_skipped(page_num, reason="No 'Designed by:' found"):
    """Log skipped pages."""
    data = {"page": page_num, "reason": reason}

    with open(SKIPPED_FILE, 'a') as f:
        f.write(json.dumps(data) + '\n')

    print(f"Skipped page {page_num}: {reason}")

def extract_text_from_page(page_num):
    """Get text content from a slide using browser."""
    # This would need to be called via the browser's CLI interface
    # For now, this is a placeholder
    pass

def main():
    """Main processing loop."""
    print("Helmet Library Extractor - Pages 122-153")
    print("="*60)

    # Define slides to process
    slides = list(range(122, 154))  # 122-153 inclusive

    print(f"Will process {len(slides)} slides")
    print()

    # Note: Since we can't directly embed browser calls in Python here,
    # we would need to:
    # 1. Navigate to each slide via the browser CLI
    # 2. Extract text via get_page_text
    # 3. Parse the text
    # 4. Extract images via JavaScript
    # 5. Download images
    # 6. Save to JSONL

    # For now, we'll demonstrate the data structure with the slide 122 example

    # Example data for slide 122 (extracted manually above)
    page_122_data = {
        "page": 122,
        "name": "Techno Mando",
        "maker": "Galactic Armory",
        "approvable": False,
        "eras": [],
        "images": ["p122-1.png", "p122-2.png", "p122-3.png"],
        "links": []
    }

    print("Example structure for slide 122:")
    print(json.dumps(page_122_data, indent=2))
    print()
    print("To complete extraction, would need to:")
    print("1. Navigate to each slide")
    print("2. Extract text content")
    print("3. Parse helmet metadata")
    print("4. Download images")
    print("5. Save to JSONL files")

if __name__ == "__main__":
    main()
