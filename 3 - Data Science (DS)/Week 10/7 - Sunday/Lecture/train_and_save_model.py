import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import joblib

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert the data into a pandas DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

# Specify the number of clusters (k)
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# Save the trained model
joblib.dump(kmeans, 'iris_kmeans_model.pkl')

print("Model trained and saved successfully.")