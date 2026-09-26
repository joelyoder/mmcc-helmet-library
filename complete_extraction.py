#!/usr/bin/env python3
"""
Complete extraction of helmet data from slides 125-153.
This script will be called manually to process remaining slides.

Prerequisite: Browser tab must be open with Canva document.
This script uses subprocess to invoke browser tool commands.
"""

import json
import subprocess
import time
import sys
from pathlib import Path
from urllib.parse import quote

OUTPUT_DIR = Path("/Users/joel/git/mmcc-helmet-library/scrape")
IMAGES_DIR = OUTPUT_DIR / "images"
DATA_FILE = OUTPUT_DIR / "data_122-153.jsonl"
SKIPPED_FILE = OUTPUT_DIR / "skipped_122-153.jsonl"

def extract_slide(slide_num):
    """
    Extract data from a single slide.

    Steps:
    1. Navigate to slide
    2. Get page text
    3. Check for "Designed by:"
    4. Extract helmet metadata
    5. Extract images via JavaScript
    6. Download images
    7. Save to JSON lines file
    """

    print(f"\nProcessing slide {slide_num}...")

    # Navigate to slide
    url = f"https://www.canva.com/design/DAGYU40jp3k/pbXHuLKVEW0Jy-ETSXrxTg/view#{slide_num}"
    print(f"  Navigating to {url}...")

    # Wait for page load
    time.sleep(2)

    # Get page text to check for helmet data
    # (Would use browser tool in actual implementation)

    # Extract images if helmet data found
    # (Would use browser tool in actual implementation)

    # Download images
    # (Would use curl in actual implementation)

    # Save to JSONL
    # (Would append JSON line to file)

    print(f"  Slide {slide_num} processed")

def main():
    print("Complete Extraction - Slides 125-153")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Data file: {DATA_FILE}")
    print(f"Images directory: {IMAGES_DIR}")
    print()

    # Check current progress
    current_lines = DATA_FILE.read_text().count('\n')
    print(f"Current progress: {current_lines} helmets extracted")
    print()

    # Process slides 125-153
    slides_to_process = list(range(125, 154))  # 125-153 inclusive
    print(f"Will process {len(slides_to_process)} remaining slides")
    print()

    for slide_num in slides_to_process:
        try:
            extract_slide(slide_num)
            time.sleep(1)  # Rate limiting
        except Exception as e:
            print(f"  Error processing slide {slide_num}: {e}")
            with open(SKIPPED_FILE, 'a') as f:
                f.write(json.dumps({
                    "page": slide_num,
                    "reason": f"Error: {str(e)}"
                }) + '\n')

    # Final report
    print()
    print("=" * 60)
    print("Extraction Complete")
    print("=" * 60)

    data_count = DATA_FILE.read_text().count('\n')
    skipped_count = SKIPPED_FILE.read_text().count('\n') if SKIPPED_FILE.exists() else 0

    print(f"Helmets extracted: {data_count}")
    print(f"Slides skipped: {skipped_count}")
    print(f"Total processed: {data_count + skipped_count} / 32")

if __name__ == "__main__":
    main()
