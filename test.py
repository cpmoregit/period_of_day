#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 24 14:29:01 2025

@author: cpmore
"""

import pandas as pd
import numpy as np

# Feature names
feature_names = [
    "Age", "Height", "Weight", "Gender", "Income", "Education Level",
    "Number of Children", "Home Ownership", "Daily Exercise Time", "Sleep Duration"
]

# Generate dataset (100 samples, 10 features)
X = np.random.rand(100, 10) * 100  # Random values scaled for variability

# Convert to a DataFrame for better visualization
X_df = pd.DataFrame(X, columns=feature_names)

# Show the first few rows
print(X_df.head())
