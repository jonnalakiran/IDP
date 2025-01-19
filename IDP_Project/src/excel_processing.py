# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:56:40 2025

@author: HP
"""

import pandas as pd

def process_excel(file_path):
    """
    Process an Excel file to extract specific fields:
    - Invoice Number
    - Invoice Date
    - Vendor Name
    - Total Amount
    - Tax Amount

    :param file_path: Path to the Excel file.
    :return: Dictionary with extracted fields.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Normalize column names to lowercase for easier matching
        df.columns = [col.lower() for col in df.columns]

        # Define required fields and their possible variations in column names
        field_mapping = {
            "Invoice Number": ["invoice number","Invoice Number",  "inv number", "invoice id"],
            "Invoice Date": ["invoice date", "date","Invoice Date"],
            "Vendor Name": ["vendor name", "supplier name", "company name","Vendor Name"],
            "Total Amount": ["total amount", "amount", "invoice total", "Total Amount"],
            "Tax Amount": ["tax amount", "tax", "vat", "Tax Amount"],
        }

        # Extract fields from the DataFrame
        extracted_fields = {}
        for field, variations in field_mapping.items():
            for variation in variations:
                if variation in df.columns:
                    extracted_fields[field] = df[variation].tolist()  # Assuming first row contains relevant data
                    break
            else:
                extracted_fields[field] = None  # Default to None if not found

        return extracted_fields

    except Exception as e:
        print(f"Error processing Excel file: {e}")
        return None
