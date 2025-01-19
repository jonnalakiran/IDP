# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:02:26 2025

@author: HP
"""

import pytest
from field_extraction import extract_fields

def test_extract_fields():
    """
    Test that fields are correctly extracted from sample text.
    """
    sample_text = """
    Invoice Number: INV12345
    Invoice Date: 01/12/2023
    Vendor Name: ABC Corp
    Total Amount: 1000.50
    Tax Amount: 50.25
    """
    fields = extract_fields(sample_text)
    assert fields["Invoice Number"] == "INV12345"
    assert fields["Invoice Date"] == "01/12/2023"
    assert fields["Vendor Name"] == "ABC Corp"
    assert fields["Total Amount"] == "1000.50"
    assert fields["Tax Amount"] == "50.25"
