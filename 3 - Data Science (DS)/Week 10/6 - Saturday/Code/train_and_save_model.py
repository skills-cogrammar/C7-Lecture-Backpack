import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from preprocess import preprocess_images
from train import train_model

# Load the MNIST dataset from CSV
data = pd.read_csv('mnist_train.csv')
X = data.iloc[:, 1:].values
y = data.iloc[:, 0].values

# Reshape the images to 2D arrays
X = X.reshape(-1, 28, 28)

# Preprocess the images
X_preprocessed = preprocess_images(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

# Train the model and save it
model = train_model(X_train, y_train)
print("Model trained and saved successfully.")