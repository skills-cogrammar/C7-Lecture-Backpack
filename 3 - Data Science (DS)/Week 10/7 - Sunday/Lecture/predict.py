import numpy as np
import joblib

# Load the trained model
kmeans = joblib.load('iris_kmeans_model.pkl')

# Get user input
print("Enter the features of the Iris flower (in cm):")
sepal_length = float(input("Sepal Length (4.3 - 7.9): "))
sepal_width = float(input("Sepal Width (2.0 - 4.4): "))
petal_length = float(input("Petal Length (1.0 - 6.9): "))
petal_width = float(input("Petal Width (0.1 - 2.5): "))

# Create a new sample
new_sample = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict the cluster for the new sample
cluster_label = kmeans.predict(new_sample)

# Map cluster labels to species names
species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
predicted_species = species_mapping[cluster_label[0]]

print(f"The predicted species for the given Iris flower is: {predicted_species}")