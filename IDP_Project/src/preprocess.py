# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:53:01 2025

@author: HP
"""
#!pip install pdf2image

import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy:
    - Convert to grayscale.
    - Denoise using median blur.
    - Apply adaptive thresholding.
    - Deskew the image.
    """
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Denoise using median blur
    denoised_image = cv2.medianBlur(image, 5)

    # Apply adaptive thresholding
    binary_image = cv2.adaptiveThreshold(
        denoised_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Deskew the image
    coords = np.column_stack(np.where(binary_image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = binary_image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    deskewed_image = cv2.warpAffine(binary_image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC)

    return deskewed_image
