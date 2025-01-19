# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:54:59 2025

@author: HP
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """
    Perform OCR on the image at the given file path.
    """
    config = r'--oem 3 --psm 6'  # OCR engine for block text layout
    try:
        text = pytesseract.image_to_string(Image.open(image_path), config=config, lang='eng')
        return text
    except Exception as e:
        print(f"Error during OCR: {e}")
        return ""
