# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:01:43 2025

@author: HP
"""

import pytest
from ocr import extract_text


def test_extract_text():
    """
    Test that OCR correctly extracts text from a sample image.
    """
    test_image_path = r"G:\IDP_Project\data\images\invoice1.jpg"
    text = extract_text(test_image_path)
    assert isinstance(text, str), "OCR did not return a string"
    assert len(text) > 0, "OCR output is empty"
