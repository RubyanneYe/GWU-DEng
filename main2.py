# -*- coding: utf-8 -*-
"""main2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HB-ev61pPTByxd5AtDC6pdVelnas_BcS
"""

import pandas as pd

data = pd.read_csv('data_imputed.csv')

data

"""## LSTM"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Bidirectional, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping

# Read dataset
data = pd.read_csv('data_imputed.csv')
# Select the first of every 100 samples
data = data.iloc[::100, :]

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
# Define category mapping
# class_mapping = {
#     'BENIGN': 0,
#     'Brute Force': 1,
#     'DDoS': 2,
#     'SQL Injection': 3,
#     'XSS': 4
# }
# # Assuming that the top 20% of important features have been selected and stored in the selected_features list
# # selected_features = ['Fwd Packet Length Mean', 'Avg Fwd Segment Size', 'Init_Win_bytes_backward', 'Fwd Packet Length Max', 'Average Packet Size', 'Fwd IAT Std', 'Total Length of Fwd Packets', 'Subflow Fwd Bytes', 'Destination Port', 'Fwd IAT Min']
# # Add new integer category column
# data['attack type'] = data['attack type'].map(class_mapping)
# Feature selection and labeling
X = data.drop('bandwidth_utilization', axis=1).values
y = data['bandwidth_utilization'].values

# Data standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split train set and train set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Defining model parameters
input_shape = X_train.shape[1]
output_units = 1  # The regression task output unit is 1
dropout_rate = 0.2

# Define LSTM Model
LSTM = Sequential([
    LSTM(128, return_sequences=True, input_shape=(input_shape, 1)),
    Dropout(dropout_rate),
    BatchNormalization(),
    LSTM(64, return_sequences=True),
    Dropout(dropout_rate),
    BatchNormalization(),
    LSTM(32),
    Dropout(dropout_rate),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dropout(dropout_rate),
    Dense(output_units)
])

# Compilation model
LSTM.compile(optimizer='adam', loss='mean_squared_error')

# Define Early Stopping callback function
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train model and record loss
history = LSTM.fit(X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train,
                        epochs=150, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)

# Save model to the model folder
model_save_path = 'model/R_LSTM_Model.h5'
LSTM.save(model_save_path)
print(f"Model saved to {model_save_path}")

# Plotting the loss curve
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('LSTM Training and Validation Loss')
plt.legend()
plt.show()

# Predictions on the test set
y_pred = LSTM.predict(X_test.reshape((X_test.shape[0], X_test.shape[1], 1)))

# Calculate and output R^2 score
r2 = r2_score(y_test, y_pred)
print(f'R^2 Score: {r2:.4f}')

# Plotting real and predicted values
plt.figure(figsize=(30, 6))
plt.plot(y_test, label='True Values')
plt.plot(y_pred, label='Predictions')
plt.xlabel('Samples')
plt.ylabel('bandwidth_utilization')
plt.title('True Values vs Predictions')
plt.legend()
plt.show()

"""## GRU"""

from tensorflow.keras.layers import Dense, GRU, Bidirectional, Dropout, BatchNormalization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Bidirectional, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping

# Read dataset
data = pd.read_csv('data_imputed.csv')
# Select the first of every 100 samples
data = data.iloc[::100, :]

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
# Define category mapping
# class_mapping = {
#     'BENIGN': 0,
#     'Brute Force': 1,
#     'DDoS': 2,
#     'SQL Injection': 3,
#     'XSS': 4
# }
# # Assuming that the top 20% of important features have been selected and stored in the selected_features list
# # selected_features = ['Fwd Packet Length Mean', 'Avg Fwd Segment Size', 'Init_Win_bytes_backward', 'Fwd Packet Length Max', 'Average Packet Size', 'Fwd IAT Std', 'Total Length of Fwd Packets', 'Subflow Fwd Bytes', 'Destination Port', 'Fwd IAT Min']
# # Add new integer category column
# data['attack type'] = data['attack type'].map(class_mapping)
# Feature selection and labeling
X = data.drop('bandwidth_utilization', axis=1).values
y = data['bandwidth_utilization'].values

# Data standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split train set and test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Defining model parameters
input_shape = X_train.shape[1]
output_units = 1  # The regression task output unit is 1
dropout_rate = 0.2

# Define GRU model
GRU_model = Sequential([
    GRU(128, return_sequences=True, input_shape=(input_shape, 1)),
    Dropout(dropout_rate),
    BatchNormalization(),
    GRU(64, return_sequences=True),
    Dropout(dropout_rate),
    BatchNormalization(),
    GRU(32),
    Dropout(dropout_rate),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dropout(dropout_rate),
    Dense(output_units)
])

# Compilation model
GRU_model.compile(optimizer='adam', loss='mean_squared_error')

# Define Early Stopping callback function
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train model and record loss
history = GRU_model.fit(X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train,
                        epochs=150, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)

# Save model to the model folder
model_save_path = 'model/R_GRU_Model.h5'
GRU_model.save(model_save_path)
print(f"Model saved to {model_save_path}")

# Plotting the loss curve
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('GRU Training and Validation Loss')
plt.legend()
plt.savefig('pic/GRU Training and Validation Loss.jpg')
plt.show()

# Predictions on the test set
y_pred = GRU_model.predict(X_test.reshape((X_test.shape[0], X_test.shape[1], 1)))

# Calculate and output R^2 score
r2 = r2_score(y_test, y_pred)
print(f'R^2 Score: {r2:.4f}')

# Plotting real and predicted values
plt.figure(figsize=(30, 6))
plt.plot(y_test, label='True Values')
plt.plot(y_pred, label='Predictions')
plt.xlabel('Samples')
plt.ylabel('Flow Duration')
plt.title('GRU True Values vs Predictions')
plt.legend()
plt.savefig('pic/GRU True Values vs Predictions.jpg')
plt.show()

"""## BIGRU"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Bidirectional, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tqdm import tqdm

# Read dataset
data = pd.read_csv('data_imputed.csv')
# Select the first of every 100 samples
data = data.iloc[::100, :]

label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
# Define category mapping
# class_mapping = {
#     'BENIGN': 0,
#     'Brute Force': 1,
#     'DDoS': 2,
#     'SQL Injection': 3,
#     'XSS': 4
# }
# # Assuming that the top 20% of important features have been selected and stored in the selected_features list
# # selected_features = ['Fwd Packet Length Mean', 'Avg Fwd Segment Size', 'Init_Win_bytes_backward', 'Fwd Packet Length Max', 'Average Packet Size', 'Fwd IAT Std', 'Total Length of Fwd Packets', 'Subflow Fwd Bytes', 'Destination Port', 'Fwd IAT Min']
# # Add new integer category column
# data['attack type'] = data['attack type'].map(class_mapping)
# Select features and labelling
X = data.drop('bandwidth_utilization', axis=1).values
y = data['bandwidth_utilization'].values

# Data standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split train set and test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Defining model parameters
input_shape = X_train.shape[1]
output_units = 1  # The regression task output unit is 1
dropout_rate = 0.2

# Define BiGRU model
BiGRU = Sequential([
    Bidirectional(GRU(128, return_sequences=True, input_shape=(input_shape, 1))),
    Dropout(dropout_rate),
    BatchNormalization(),
    Bidirectional(GRU(64, return_sequences=True)),
    Dropout(dropout_rate),
    BatchNormalization(),
    Bidirectional(GRU(32)),
    Dropout(dropout_rate),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dropout(dropout_rate),
    Dense(output_units)
])

# Compilation model
BiGRU.compile(optimizer='adam', loss='mean_squared_error')

# Define Early Stopping callback functions
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train model and record loss
history = BiGRU.fit(X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train,
                        epochs=150, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)

# Save model to the model folder
model_save_path = 'model/R_BiGRU_Model.h5'
BiGRU.save(model_save_path)
print(f"Model saved to {model_save_path}")

# Plotting the loss curve
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('BiGRU Training and Validation Loss')
plt.legend()
plt.savefig('pic/BiGRU Training and Validation Loss.jpg')
plt.show()

# Predictions on the test set
y_pred = BiGRU.predict(X_test.reshape((X_test.shape[0], X_test.shape[1], 1)))

# Calculate and output R^2 score
r2 = r2_score(y_test, y_pred)
print(f'R^2 Score: {r2:.4f}')

# Plotting real and predicted values
plt.figure(figsize=(30, 6))
plt.plot(y_test, label='True Values')
plt.plot(y_pred, label='Predictions')
plt.xlabel('Samples')
plt.ylabel('Flow Duration')
plt.title('True Values vs Predictions')
plt.legend()
plt.savefig('pic/BiGRU True Values vs Predictions.jpg')
plt.show()
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Calculate and output MSE
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.4f}')

# Calculate and output MAE
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae:.4f}')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Bidirectional, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder

# Read dataset
data = pd.read_csv('data_imputed.csv')

# Select the first of every 100 samples
data = data.iloc[::100, :]

# Encoded Category Variables
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
# Remove bandwidth_utilization max 10% of data
quantile_90 = data['bandwidth_utilization'].quantile(0.90)
data = data[data['bandwidth_utilization'] <= quantile_90]
# Visualise the range of values and interval density of label
plt.figure(figsize=(12, 6))
sns.histplot(data['bandwidth_utilization'], bins=50, kde=True)
plt.xlabel('Bandwidth Utilization')
plt.ylabel('Density')
plt.title('Distribution of Bandwidth Utilization')
plt.savefig('pic/Bandwidth_Utilization_Distribution.jpg')
plt.show()

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

# Read dataset
data = pd.read_csv('data_imputed.csv')
data = data.iloc[::100, :]

# Loading the previously saved model
model = load_model('model/R_BiGRU_Model.h5')

# Pre-processing data
# Ensure that data is preprocessed in a manner consistent with training
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Assuming that mappings such as class_mapping already exist and are correctly applied to the data

# Select features and labelling
X = data.drop('bandwidth_utilization', axis=1).values
y = data['bandwidth_utilization'].values

# Data standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Predicting data
X_scaled_reshaped = X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1))
predictions = model.predict(X_scaled_reshaped)

# Create a new column to output ‘reject’ or ‘accept’ based on the predicted value
data['prediction'] = predictions
threshold = 5 * 10**-5
data['result'] = np.where(data['prediction'] > threshold, 'reject', 'accept')

# Save data with predictions to a new CSV file
output_path = 'data_with_predictions2.csv'
data.to_csv(output_path, index=False)
print(f"Data with predictions saved to {output_path}")

# Display the first few rows of results
print(data.head())
