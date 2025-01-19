Invoice Data Processing (IDP) Solution


Project Overview

The Invoice Data Processing (IDP) project is designed to extract key information from various document formats, including images, PDFs, and Excel/CSV files. The solution identifies and extracts:

Invoice Number
Invoice Date
Vendor Name
Total Amount
Tax Amount

The solution supports OCR-based text extraction, field-specific data extraction, and performance metrics evaluation.

Setup Instructions

Prerequisites

Install Python (3.8+).

Install Tesseract OCR:

Download and install Tesseract from Tesseract OCR GitHub.
Note the installation path (e.g., C:\Program Files\Tesseract-OCR).
Install Poppler (for PDF to image conversion):

Download and install Poppler from Poppler.
Add the bin directory of Poppler to your system's PATH.


IDP_Project/
├── src/
│   ├── __init__.py                # Marks src as a package
│   ├── preprocess.py              # Image preprocessing logic
│   ├── ocr.py                     # OCR functionality for text extraction
│   ├── field_extraction.py        # Regex-based field extraction
│   ├── excel_processing.py        # Logic to process Excel/CSV files
│   ├── metrics.py                 # Performance and accuracy evaluation
│   ├── main.py                    # Main script for document processing
│   ├── evaluate.py                # Script for performance evaluation
├── tests/
│   ├── test_preprocess.py         # Unit tests for preprocess.py
│   ├── test_ocr.py                # Unit tests for ocr.py
│   ├── test_field_extraction.py   # Unit tests for field_extraction.py
│   ├── test_excel_processing.py   # Unit tests for excel_processing.py
├── data/
│   ├── images/                    # Sample image files
│   ├── pdfs/                      # Sample PDF files
│   ├── excel/                     # Sample Excel files
├── requirements.txt               # List of Python dependencies
├── README.md                      # Project documentation

Install Dependencies

Run the following command to install all required Python libraries:

pip install -r requirements.txt

Usage

1. Main Script (main.py)
The main.py script processes individual documents and extracts fields:

	> python src/main.py

Steps:

	a. Select the file type (image, PDF, or Excel/CSV).
	b. Enter the file name from the available list.
	c. View the extracted fields.

2. Evaluation Script (evaluate.py)
The evaluate.py script evaluates the solution’s accuracy and performance:

	>python src/evaluate.py

Steps:

	a. Select the file type.
	b. Choose a file from the list.
	c. Enter ground truth values for evaluation.
	d. View extracted fields, metrics, and processing time.

3. Excel Processing (excel_processing.py)
Use the process_excel function to extract fields from Excel/CSV files programmatically:

from excel_processing import process_excel

file_path = "data/excel/sample_invoice.xlsx"
fields = process_excel(file_path)
print(fields)

4. Unit Tests
Run unit tests to verify individual components:

	>pytest tests/

Modules

1. Preprocessing (preprocess.py)
Preprocesses images for OCR, including grayscaling, denoising, and binarization.

Functions:
preprocess_image(image_path): Returns a processed image.

2. OCR (ocr.py)
Performs OCR on preprocessed images or PDF pages.

Functions:
extract_text(image_path): Returns text extracted from the image.

3. Field Extraction (field_extraction.py)
Uses regex to extract specific fields from text.

Functions:
extract_fields(text): Returns a dictionary with extracted fields.

4. Excel Processing (excel_processing.py)
Reads Excel/CSV files and extracts the required fields.

Functions:
process_excel(file_path): Returns a dictionary with extracted fields.

5. Metrics (metrics.py)
Measures performance and evaluates accuracy.

Functions:
evaluate_metrics(true_fields, predicted_fields): Prints precision, recall, and F1-score.
measure_performance(process_function, file_path): Prints processing time.

Features

Multi-Format Support:
Processes images, PDFs, and Excel/CSV files.

Field Extraction:
Extracts invoice-specific fields using regex.

Performance Metrics:
Measures precision, recall, F1-score, and processing time.

Extensibility:
Easily customizable for additional fields or formats.

Sample Outputs

Processing a Document:

Processing G:/IDP_Project/data/images/invoice1.jpg...
Extracted Fields:
Invoice Number: INV-12345
Invoice Date: 2024-01-23
Vendor Name: ABC Supplies Inc.
Total Amount: $1234.56
Tax Amount: $234.56

Evaluation Metrics:

Evaluation Metrics:

               precision    recall  f1-score   support

Not Extracted       0.00      0.00      0.00       0
    Extracted     100.00    100.00    100.00       5

Future Enhancements

Enhance OCR Preprocessing:
Add deskewing and more advanced noise removal techniques.

Support for More Formats:
Extend support to Word documents or other structured data formats.

Automated Field Validation:
Automatically validate extracted fields against known rules.
 
Contributing
To contribute by opening issues or submitting pull requests. Ensure code adheres to PEP 8 standards and includes unit tests.











