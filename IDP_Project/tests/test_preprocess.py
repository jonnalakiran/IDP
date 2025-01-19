# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:00:34 2025

@author: HP
"""

import pytest
from preprocess import preprocess_image
import os
import sys

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'G:\IDP_Project\src')))
def test_preprocess_image():
    """
    Test that the preprocess_image function produces a binary image.
    """
    test_image_path = r"G:\IDP_Project\data\images\ledger_invoice_1.jpg"
    processed_image = preprocess_image(test_image_path)
    assert processed_image is not None, "Preprocessing failed"
    assert len(processed_image.shape) == 2, "Image is not grayscale"
