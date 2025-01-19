# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:56:02 2025

@author: HP
"""

import re

def extract_fields(text):
    """
    Extract required fields from OCR text using regex.
    """
    fields = {
        "Invoice Number": None,
        "Invoice Date": None,
        "Vendor Name": None,
        "Total Amount": None,
        "Tax Amount": None,
    }

    # Extract Invoice Number (e.g., INV-12345)
    match = re.search(r"INV[-\s]?\d+", text, re.IGNORECASE)
    if match:
        fields["Invoice Number"] = match.group(0)

    # Extract Invoice Date (e.g., 2024-01-23 or 01/23/2024)
    match = re.search(r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b", text)
    if match:
        fields["Invoice Date"] = match.group(0)

    # Extract Vendor Name (assume it's near "Vendor")
    match = re.search(r"Vendor[:\s]+([A-Za-z\s&]+)", text, re.IGNORECASE)
    if match:
        fields["Vendor Name"] = match.group(1).strip()

    # Extract Total Amount (e.g., $1234.56 or 1234.56)
    match = re.search(r"Total[:\s]*\$?(\d+[.,]?\d*)", text, re.IGNORECASE)
    if match:
        fields["Total Amount"] = match.group(1)

    # Extract Tax Amount (e.g., $234.56 or 234.56)
    match = re.search(r"Tax[:\s]*\$?(\d+[.,]?\d*)", text, re.IGNORECASE)
    if match:
        fields["Tax Amount"] = match.group(1)

    return fields
