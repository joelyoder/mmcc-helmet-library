#!/usr/bin/env python3
"""
Parse Canva page text and extract helmet data
"""

import json
import sys
import re

def extract_helmet_data(page_text, page_num):
    """
    Extract helmet data from page text.
    Returns dict or None if not a helmet slide.
    """

    # Check if "Designed by:" is present
    if "Designed by:" not in page_text:
        return None

    result = {
        "page": page_num,
        "name": "",
        "maker": "",
        "approvable": True,
        "eras": [],
        "images": [],
        "links": []
    }

    # Extract maker from "Designed by:" line
    # The text often has "Designed by: <maker>" appearing multiple times
    lines = page_text.split('\n')
    for i, line in enumerate(lines):
        if "Designed by:" in line:
            parts = line.split("Designed by:")
            if len(parts) > 1:
                maker = parts[1].strip()
                if maker and maker != "Designed by:":
                    result["maker"] = maker
                    break

    # Extract helmet name - look for lines that appear before "Designed by:"
    # Usually there's a name line that appears before the "Designed by:" line
    # It might appear multiple times in the text
    designed_idx = -1
    for i, line in enumerate(lines):
        if "Designed by:" in line:
            designed_idx = i
            break

    if designed_idx > 0:
        # Look backwards from the "Designed by:" line for the helmet name
        for i in range(designed_idx - 1, -1, -1):
            line = lines[i].strip()
            if line and line != "Approvable" and line != "for:" and not line.startswith("Approvable"):
                if not "Designed by:" in line and line != "Not Approvable" and line != "NONE":
                    result["name"] = line
                    break

    # If still no name, find the most repeated non-special line
    if not result["name"]:
        line_counts = {}
        era_keywords = {"Modern", "Legacy", "Pilot w/ Acc.", "Covert", "Mercenary", "Survivor", "Master"}
        for line in lines:
            line_stripped = line.strip()
            if (line_stripped and len(line_stripped) < 50 and
                "Designed by:" not in line_stripped and
                "Approvable" not in line_stripped and
                "for:" != line_stripped and
                "NONE" != line_stripped and
                line_stripped not in era_keywords and
                "Not Approvable" != line_stripped):
                line_counts[line_stripped] = line_counts.get(line_stripped, 0) + 1

        # Find the most repeated line (likely the helmet name)
        if line_counts:
            result["name"] = max(line_counts, key=line_counts.get)

    # Check if "Not Approvable" is present
    if "Not Approvable" in page_text:
        result["approvable"] = False

    # Extract eras if approvable
    if result["approvable"]:
        # Look for era tags in lines after "Approvable for:"
        for i, line in enumerate(lines):
            if "Approvable for:" in line:
                # Get the next non-empty line
                for j in range(i + 1, len(lines)):
                    era_line = lines[j].strip()
                    if era_line and era_line != "Approvable" and era_line != "for:":
                        if era_line != "NONE" and not "Designed by:" in era_line:
                            # Parse era line - might have bullets or be comma-separated
                            eras = [e.strip() for e in era_line.split('\n')]
                            eras = [e.strip() for e in re.split(r'[•,]', '\n'.join(eras)) if e.strip()]
                            result["eras"] = eras
                        break

    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_helmet_data.py <page_num>", file=sys.stderr)
        sys.exit(1)

    page_num = int(sys.argv[1])
    page_text = sys.stdin.read()

    result = extract_helmet_data(page_text, page_num)
    if result:
        print(json.dumps(result))
    else:
        print(json.dumps({"page": page_num, "skipped": True}))
