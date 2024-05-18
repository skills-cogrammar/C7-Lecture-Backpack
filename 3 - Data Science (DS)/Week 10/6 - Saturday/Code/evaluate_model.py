import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from preprocess import preprocess_images

# Load the trained model from the file
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the test dataset from CSV
test_data = pd.read_csv('mnist_test.csv')
X_test = test_data.iloc[:, 1:].values
y_test = test_data.iloc[:, 0].values

# Reshape the test images to 2D arrays
X_test = X_test.reshape(-1, 28, 28)

# Preprocess the test images
X_test_preprocessed = preprocess_images(X_test)

# Make predictions on the test set
y_pred = model.predict(X_test_preprocessed)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Print the evaluation metrics
print("Evaluation Metrics:")
print("Accuracy: {:.4f}".format(accuracy))
print("Precision: {:.4f}".format(precision))
print("Recall: {:.4f}".format(recall))
print("F1 Score: {:.4f}".format(f1))