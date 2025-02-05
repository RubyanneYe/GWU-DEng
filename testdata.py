# -*- coding: utf-8 -*-
"""testData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iynese_UvF1KeGNxQ8Br04f7fArQHrMB
"""

import joblib
import pandas as pd

# Read dataset
new_data = pd.read_csv('data_imputed.csv')
new_data = new_data.drop(['attack type', 'bandwidth_utilization'], axis=1)
# Load model
model_path = 'model/C_Stacking_Model.joblib'
model = joblib.load(model_path)

# Start prediction
new_data['attack type'] = model.predict(new_data)
print(new_data['attack type'])
# Define category mapping
class_mapping = {
    0: 'Benign',
    1: 'Brute Force',
    2: 'DDoS',
    3: 'MITM',
    4:'SQL Injection',
}

# Mapping of projected results
new_data['attack type'] = new_data['attack type'].map(class_mapping)
print(new_data['attack type'])
# Generate accept/reject columns based on predictions
new_data['result'] = new_data['attack type'].apply(lambda x: 'accept' if x == 'Benign' else 'reject')

# Save the output to a CSV file
new_data.to_csv('prediction_Finally1.csv', index=False)

print("Prediction and result columns have been added and saved to 'prediction_Finally.csv'.")

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import load_model

# # Read dataset
# data = pd.read_csv('data_imputed.csv')
# data = data.iloc[::100, :]
data = new_data
# Load model
model = load_model('model/R_BiGRU_Model.h5')

# Pre-processing data
# Ensure that data is preprocessed in a manner consistent with training
# label_encoders = {}
# for column in data.select_dtypes(include=['object']).columns:
#     le = LabelEncoder()
#     data[column] = le.fit_transform(data[column])
#     label_encoders[column] = le

# 假设class_mapping等映射已经存在，并正确应用到数据中
class_mapping = {
    'Benign': 0,
    'Brute Force': 1,
    'DDoS': 2,
    'MITM': 3,
    'SQL Injection': 4
}
print(data.head())
# Add new integer category column
data['attack type'] = data['attack type'].map(class_mapping)
print(data.head())
# Only data with a result of ‘accept’ is detected
data = data[data['result'] == 'accept']

# Selecting features and labelling
X = data.drop('result', axis=1).values

# Data standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Predicting data
X_scaled_reshaped = X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1))
predictions = model.predict(X_scaled_reshaped)

# Create a new column to output ‘reject’ or ‘accept’ based on the predicted value.
data['prediction'] = predictions
threshold = 5 * 10**-5
data['result'] = np.where(data['prediction'] > threshold, 'reject', 'accept')

# Save data with predictions to a new CSV file
output_path = 'prediction_Finally2.csv'
data.to_csv(output_path, index=False)
print(f"Data with predictions saved to {output_path}")

# Display the first few rows of results
print(data.head())

