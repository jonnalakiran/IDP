# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:58:18 2025

@author: HP
"""

import os
import cv2
from pdf2image import convert_from_path
from preprocess import preprocess_image
from ocr import extract_text
from field_extraction import extract_fields
from excel_processing import process_excel


def process_image(file_path):
    """
    Process an image file and extract fields using OCR and preprocessing.
    """
    try:
        # Preprocess the image
        processed_image = preprocess_image(file_path)

        # Save the processed image temporarily
        temp_image_path = "temp_processed_image.png"
        cv2.imwrite(temp_image_path, processed_image)

        # Perform OCR
        text = extract_text(temp_image_path)
        os.remove(temp_image_path)  # Remove temporary image

        # Debugging: Print OCR output
        print(f"\nOCR Output:\n{text}")

        # Extract required fields
        fields = extract_fields(text)
        return fields
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


def process_pdf(file_path):
    """
    Process a PDF file by converting it to images and extracting fields using OCR.
    """
    try:
        images = convert_from_path(file_path, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        combined_text = ""

        for i, image in enumerate(images):
            temp_image_path = f"temp_pdf_page_{i + 1}.png"
            image.save(temp_image_path, "PNG")

            # Perform OCR with English language setting
            text = extract_text(temp_image_path)
            combined_text += text + "\n"
            os.remove(temp_image_path)  # Remove temporary file

        # Extract required fields
        fields = extract_fields(combined_text)
        return fields
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None


def process_excel_or_csv(file_path):
    """
    Process an Excel or CSV file and extract relevant fields.
    """
    try:
        fields_list = process_excel(file_path)
        if fields_list:
            return fields_list[0]  # Return the first record for simplicity
        return {}
    except Exception as e:
        print(f"Error processing Excel/CSV file: {e}")
        return None



if __name__ == "__main__":
    base_paths = {
        "image": "G:/IDP_Project/data/images/",
        "pdf": "G:/IDP_Project/data/pdfs/",
        "excel": "G:/IDP_Project/data/excel/",
    }

    print("Select the file type:")
    print("1. Image (JPG/PNG)")
    print("2. PDF")
    print("3. Excel/CSV")
    choice = input("Enter your choice (1/2/3): ")

    file_types = {"1": "image", "2": "pdf", "3": "excel"}
    if choice not in file_types:
        print("Invalid choice. Exiting.")
        exit()

    file_type = file_types[choice]
    base_path = base_paths[file_type]

    print(f"Available files in {base_path}:")
    print("\n".join(os.listdir(base_path)))

    file_name = input(f"Enter the file name (including extension) from {base_path}: ")
    file_path = os.path.join(base_path, file_name)

    if not os.path.exists(file_path):
        print(f"The file does not exist: {file_path}")
        exit()

    print("\nProcessing the document...")
    if file_type == "image":
        fields = process_image(file_path)
    elif file_type == "pdf":
        fields = process_pdf(file_path)
    elif file_type == "excel":
        fields = process_excel(file_path)

    if fields:
        print("\nExtracted Fields:")
        for key, value in fields.items():
            print(f"{key}: {value}")
    else:
        print("No fields extracted. Check the document and logic.")
