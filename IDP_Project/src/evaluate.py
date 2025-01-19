# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 07:57:29 2025

@author: HP
"""

import os
from metrics import evaluate_metrics, measure_performance
from main import process_image, process_pdf, process_excel_or_csv

# Define base directories for different file types
base_paths = {
    "image": "G:/IDP_Project/data/images/",
    "pdf": "G:/IDP_Project/data/pdfs/",
    "excel": "G:/IDP_Project/data/excel/",
}

def list_files(base_path):
    """
    List all files in the given directory.
    """
    try:
        files = os.listdir(base_path)
        if not files:
            print(f"No files found in {base_path}.")
            return []
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

def select_file():
    """
    Ask the user to select a file type and a file to evaluate.
    """
    print("Select the file type:")
    print("1. Image (JPG/PNG)")
    print("2. PDF")
    print("3. Excel/CSV")
    choice = input("Enter your choice (1/2/3): ")

    # Map choice to file type
    file_types = {"1": "image", "2": "pdf", "3": "excel"}
    if choice not in file_types:
        print("Invalid choice. Exiting.")
        return None, None

    file_type = file_types[choice]
    base_path = base_paths[file_type]

    # List available files
    files = list_files(base_path)
    if not files:
        return None, None

    print(f"Available files in {base_path}:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

    file_choice = input(f"Enter the number of the file to process (1-{len(files)}): ")
    if not file_choice.isdigit() or not (1 <= int(file_choice) <= len(files)):
        print("Invalid file choice. Exiting.")
        return None, None

    selected_file = files[int(file_choice) - 1]
    file_path = os.path.join(base_path, selected_file)
    return file_type, file_path

def get_ground_truth():
    """
    Ask the user to enter ground truth values for evaluation.
    """
    print("\nEnter the ground truth values for the following fields:")
    ground_truth = {
        "Invoice Number": input("Invoice Number: "),
        "Invoice Date": input("Invoice Date (YYYY-MM-DD or MM/DD/YYYY): "),
        "Vendor Name": input("Vendor Name: "),
        "Total Amount": input("Total Amount (e.g., $1234.56): "),
        "Tax Amount": input("Tax Amount (e.g., $234.56): "),
    }
    return ground_truth

def run_evaluation():
    """
    Run the evaluation for the selected file.
    """
    print("\nStarting Evaluation...\n")

    file_type, file_path = select_file()
    if not file_type or not file_path:
        print("No valid file selected. Exiting.")
        return

    # Map file type to processing function
    process_functions = {
        "image": process_image,
        "pdf": process_pdf,
        "excel": process_excel_or_csv,
    }
    process_function = process_functions[file_type]

    # Get ground truth values from the user
    true_fields = get_ground_truth()

    print(f"\nProcessing {file_path}...")

    # Measure performance and process the document
    processing_time, predicted_fields = measure_performance(process_function, file_path)

    if predicted_fields:
        print("\nExtracted Fields:")
        for key, value in predicted_fields.items():
            print(f"{key}: {value}")

        # Evaluate metrics
        print("\nEvaluating Metrics...")
        evaluate_metrics(true_fields, predicted_fields)
    else:
        print("No fields extracted.")

    print(f"Processing Time: {processing_time:.2f} seconds\n")
    print("Evaluation Completed.")

if __name__ == "__main__":
    run_evaluation()
