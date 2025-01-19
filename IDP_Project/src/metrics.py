# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:23:16 2025

@author: HP
"""
from sklearn.metrics import classification_report

import time

def measure_performance(process_function, file_path, *args, **kwargs):
    """
    Measure the time taken to process a document.
    :param process_function: The function used to process the document.
    :param file_path: Path to the document.
    :return: The processing time in seconds and the extracted fields.
    """
    start_time = time.time()
    try:
        fields = process_function(file_path, *args, **kwargs)
        end_time = time.time()
        processing_time = end_time - start_time

        print(f"Processing Time: {processing_time:.2f} seconds")
        if processing_time > 120:
            print("WARNING: Document processing exceeded the 2-minute limit.")
        return processing_time, fields
    except Exception as e:
        print(f"Error processing document: {e}")
        return None, None


def evaluate_metrics(true_fields, predicted_fields):
    """
    Evaluate the accuracy of the extracted fields using precision, recall, and F1-score.
    :param true_fields: Dictionary of ground truth values.
    :param predicted_fields: Dictionary of extracted values.
    """
    true_labels = [1 if val else 0 for val in true_fields.values()]
    predicted_labels = [1 if predicted_fields.get(k) else 0 for k in true_fields.keys()]

    # Ensure both classes (0 and 1) are represented in the report
    labels = [0, 1]  # 0: Not Extracted, 1: Extracted

    report = classification_report(
        true_labels,
        predicted_labels,
        target_names=["Not Extracted", "Extracted"],
        labels=labels,
        zero_division=0  # Avoid division by zero warnings
    )
    print("\nEvaluation Metrics:\n")
    print(report)
    return report
