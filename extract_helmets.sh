#!/bin/bash
# Extract helmet data from Canva pages 122-153

OUTPUT_DIR="/Users/joel/git/mmcc-helmet-library/scrape"
IMAGES_DIR="$OUTPUT_DIR/images"
DATA_FILE="$OUTPUT_DIR/data_122-153.jsonl"
SKIPPED_FILE="$OUTPUT_DIR/skipped_122-153.jsonl"

mkdir -p "$IMAGES_DIR"
touch "$DATA_FILE" "$SKIPPED_FILE"

# Function to extract data from a page using JavaScript
extract_from_page() {
    local page_num=$1
    local url="https://www.canva.com/design/DAGYU40jp3k/pbXHuLKVEW0Jy-ETSXrxTg/view?_cb=${page_num}#N"

    echo "Processing page $page_num..."

    # Use curl to fetch the Canva page HTML (might not work due to JS rendering)
    # Better approach: use open command or AppleScript to control browser

    # For now, we'll create a helper that interacts with the already-open browser tab
    # This would require specific browser API integration

    return 0
}

# Main loop
for page in {122..153}; do
    extract_from_page "$page"
    sleep 1
done

echo "Extraction complete!"
echo "Data file: $DATA_FILE"
echo "Skipped file: $SKIPPED_FILE"
