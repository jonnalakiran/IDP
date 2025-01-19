# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:03:10 2025

@author: HP
"""

import pytest
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),r'G:\IDP_Project\src')))

# Import the module
from excel_processing import process_excel

def test_process_excel():
    """
    Test that Excel files are correctly processed into structured data.
    """
    test_excel_path = os.path.abspath(r"G:\IDP_Project\data\excel\invoice_data_1.xlsx")  # Ensure absolute path
    data = process_excel(test_excel_path)
    assert isinstance(data, list), "Excel data was not processed into a list"
    assert len(data) > 0, "Excel file is empty or not processed"
