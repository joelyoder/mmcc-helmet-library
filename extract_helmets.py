#!/usr/bin/env python3
"""
Helmet Library Scraper - Extracts data from Canva deck pages 245-277
"""

import json
import sys
import re

def parse_page_text(page_text, page_num):
    """Parse page text to extract helmet data"""
    
    # Check if "Designed by:" is present
    if "Designed by:" not in page_text:
        return None  # Skip non-helmet pages
    
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
    match = re.search(r'Designed by:\s*(.+?)(?:\n|$)', page_text)
    if match:
        result["maker"] = match.group(1).strip()
    
    # Check if "Not Approvable" is present
    if "Not Approvable" in page_text:
        result["approvable"] = False
    
    # Extract eras if approvable
    if result["approvable"]:
        # Look for era tags after "Approvable for:"
        match = re.search(r'Approvable for:\s*(.+?)(?:\n|$)', page_text)
        if match:
            eras_text = match.group(1).strip()
            if eras_text and eras_text != "NONE":
                # Split by bullet points or commas
                eras = [e.strip() for e in re.split(r'[•,]|\n', eras_text) if e.strip()]
                result["eras"] = eras
    
    return result

def process_pages(start=245, end=277):
    """Process pages and yield data for each"""
    for page_num in range(start, end + 1):
        yield page_num

if __name__ == "__main__":
    # Generate page numbers to process
    for page in process_pages():
        print(f"{page}")
