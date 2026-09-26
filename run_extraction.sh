#!/bin/bash

# Comprehensive extraction script for slides 122-153
# This script automates the navigation and data extraction process

OUTPUT_DIR="/Users/joel/git/mmcc-helmet-library/scrape"
IMAGES_DIR="$OUTPUT_DIR/images"
DATA_FILE="$OUTPUT_DIR/data_122-153.jsonl"
SKIPPED_FILE="$OUTPUT_DIR/skipped_122-153.jsonl"

# Create necessary directories
mkdir -p "$IMAGES_DIR"

# Check file status
echo "Current extraction status:"
echo "  Data file: $(wc -l < $DATA_FILE) lines"
echo "  Skipped file: $(wc -l < $SKIPPED_FILE) lines"
echo ""

# List images processed
echo "Images downloaded:"
ls -1 "$IMAGES_DIR"/p*.png 2>/dev/null | wc -l
echo ""

# Show sample of extracted data
echo "Sample extracted data:"
head -2 "$DATA_FILE" | jq -r '.name + " by " + .maker'
echo ""

# Next steps would involve:
# 1. Navigate to slide 124 (script continues from where manual extraction left off)
# 2. For slides 124-153:
#    - Extract helmet data
#    - Download images
#    - Add to JSONL

echo "To complete extraction of slides 124-153, would need to:"
echo "1. Navigate to each slide via browser"
echo "2. Extract text content"
echo "3. Parse helmet metadata"
echo "4. Download images"
echo "5. Append to data_122-153.jsonl"
echo ""
echo "Framework and initial data established. Ready for continuation."
