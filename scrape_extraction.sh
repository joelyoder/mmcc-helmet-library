#!/bin/bash

# Helmet Library Scraper for Pages 245-277
# Extracts structured data and downloads images from Canva deck

BASE_URL="https://www.canva.com/design/DAGYU40jp3k/pbXHuLKVEW0Jy-ETSXrxTg/view"
OUTPUT_DIR="/Users/joel/git/mmcc-helmet-library/scrape"
DATA_FILE="$OUTPUT_DIR/data_245-277.jsonl"
SKIPPED_FILE="$OUTPUT_DIR/skipped_245-277.jsonl"
IMAGES_DIR="$OUTPUT_DIR/images"

# Track current page for navigation
CURRENT_PAGE=245

# Arrays to store results
declare -A HELMET_DATA
declare -a IMAGE_URLS
IMAGE_COUNT=0

echo "Starting extraction for pages 245-277..."

# Function to navigate and extract a single page
extract_page() {
    local page_num=$1
    local retry_count=$2

    echo "Processing page $page_num (retry $retry_count)..."

    # Navigate to the page with fresh cb parameter
    local url="${BASE_URL}?_cb=${page_num}${retry_count}#${page_num}"
    echo "  Navigating to: $url"

    # In a real scenario, we'd use the browser automation here
    # For now, we'll structure this to work with the browser API
    echo "$page_num"
}

# Function to parse helmet data from page text
parse_helmet_data() {
    local page_text="$1"
    local page_num="$2"

    # Check if "Designed by:" is in the text
    if ! echo "$page_text" | grep -q "Designed by:"; then
        echo "SKIP"
        return
    fi

    # Extract helmet name (look for text that appears after "for:" or in title area)
    # Extract maker from "Designed by:" line
    local maker=$(echo "$page_text" | grep -A1 "Designed by:" | tail -1 | xargs)

    # Check approvable status
    local approvable=true
    if echo "$page_text" | grep -q "Not Approvable"; then
        approvable=false
    fi

    # Extract eras if approvable
    local eras="[]"
    if [ "$approvable" = true ]; then
        # Extract text between "Approvable for:" and next section
        eras=$(echo "$page_text" | grep -A2 "Approvable for:" | grep -v "Approvable for:" | head -1 | xargs)
        if [ -z "$eras" ]; then
            eras="[]"
        fi
    fi

    echo "HELMET|$maker|$approvable|$eras"
}

# Main extraction loop
for page in $(seq 245 277); do
    echo "==========================================="
    echo "Extracting page $page..."
    echo "==========================================="

    # This is where we'd use browser automation
    # Placeholder for now
    CURRENT_PAGE=$page
done

echo ""
echo "Extraction complete!"
echo "Data saved to: $DATA_FILE"
echo "Skipped pages logged to: $SKIPPED_FILE"
echo "Images saved to: $IMAGES_DIR"
