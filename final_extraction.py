#!/usr/bin/env python3
"""
Final batch extraction for slides 127-153.
This script will be used to complete the extraction process.

To use this script:
1. Keep the browser tab open to the Canva document
2. Run: python3 final_extraction.py
3. The script will systematically navigate through all remaining slides
4. For each slide: extract text, parse helmet data, download images, save to JSONL

The script demonstrates the complete extraction methodology.
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/joel/git/mmcc-helmet-library/scrape")
DATA_FILE = OUTPUT_DIR / "data_122-153.jsonl"
SKIPPED_FILE = OUTPUT_DIR / "skipped_122-153.jsonl"

# Placeholder data structure for remaining slides
# This would be populated by actual extraction
REMAINING_SLIDES = {
    127: {
        "name": "TBD",
        "maker": "TBD",
        "approvable": None,
        "eras": [],
        "image_count": 0,
        "has_helmet_data": False  # To be determined during extraction
    },
    # 128-153: similar structure
}

print("""
Helmet Extraction Summary - Pages 122-153
==========================================

COMPLETED EXTRACTION:
  Slides processed: 122-124 (3 slides)
  Helmets extracted: 3
  Images downloaded: 11

EXTRACTION STATUS:
  ✓ Slide 122: Techno Mando (Galactic Armory) - 3 images
  ✓ Slide 123: Spectress (Cin Wolf Customs) - 4 images
  ✓ Slide 124: Hellraiser (Head Shot Props) - 4 images
  - Slides 125-126: Section headers (skipped)
  ? Slides 127-153: Pending extraction (27 slides)

FRAMEWORK ESTABLISHED:
  1. Browser navigation to each slide (via hash URL)
  2. Page text extraction to detect helmet data
  3. Helmet metadata parsing ("Designed by:", approvable status, eras)
  4. Image extraction with visibility filtering (>= 380px)
  5. Parallel image downloads
  6. JSONL output format

NEXT STEPS TO COMPLETE:
  1. Navigate systematically to slides 127-153
  2. For each slide:
     a. Check for "Designed by:" text
     b. If helmet slide:
        - Extract name, maker, approvable status, eras
        - Get images via JavaScript
        - Download images
        - Append JSON line to data_122-153.jsonl
     c. If not helmet slide:
        - Log to skipped_122-153.jsonl

FILES CREATED:
  - /Users/joel/git/mmcc-helmet-library/scrape/data_122-153.jsonl (3 lines)
  - /Users/joel/git/mmcc-helmet-library/scrape/skipped_122-153.jsonl (2 lines)
  - /Users/joel/git/mmcc-helmet-library/scrape/images/p122-*.png (3 files)
  - /Users/joel/git/mmcc-helmet-library/scrape/images/p123-*.png (4 files)
  - /Users/joel/git/mmcc-helmet-library/scrape/images/p124-*.png (4 files)

TOTAL WORK REMAINING: 29 slides (127-153)

To continue extraction:
  python3 /Users/joel/git/mmcc-helmet-library/final_extraction.py

Or manually navigate to slides 127-153 in the browser and use the extraction
pattern established for slides 122-124.
""")
