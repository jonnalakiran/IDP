# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:56:40 2025

@author: HP
"""

import pandas as pd

def process_excel(file_path):
    """
    Read and process Excel files to extract structured data.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
