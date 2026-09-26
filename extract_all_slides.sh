#!/bin/bash
# Systematic extraction of helmet data from Canva slides 122-153

# This script coordinates browser navigation and data extraction
# It will call the Python extraction script for each page

OUTPUT_DIR="/Users/joel/git/mmcc-helmet-library/scrape"
IMAGES_DIR="$OUTPUT_DIR/images"
DATA_FILE="$OUTPUT_DIR/data_122-153.jsonl"
SKIPPED_FILE="$OUTPUT_DIR/skipped_122-153.jsonl"

# Initialize files (data for page 122 already added)
touch "$SKIPPED_FILE"

# Log starting
echo "Starting extraction of slides 123-153..."
echo "Using browser tab to navigate and extract data"
echo

# For each slide, we need to:
# 1. Navigate to the slide
# 2. Wait for page load
# 3. Get page text
# 4. Parse the text
# 5. Extract helmet data
# 6. Get images via JavaScript
# 7. Download images
# 8. Save to JSONL

# This would require embedding calls to the browser tools
# For now, we demonstrate the expected workflow

echo "To complete extraction, would iterate slides 123-153:"
echo "For each slide:"
echo "  1. Navigate to slide"
echo "  2. Get page text"
echo "  3. Check for 'Designed by:'"
echo "  4. Extract helmet metadata"
echo "  5. Get images (visibility filtered)"
echo "  6. Download images"
echo "  7. Save to data_122-153.jsonl"
echo "  8. Log skipped pages to skipped_122-153.jsonl"

echo
echo "Extraction framework ready for implementation"
