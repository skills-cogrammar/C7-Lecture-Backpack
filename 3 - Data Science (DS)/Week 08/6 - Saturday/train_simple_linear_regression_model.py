import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Import the dataset
df = pd.read_csv("housing.csv")

# Feature matrix and target vector
X_feature = df[['Avg. Area Income']]  # Using only 'Avg. Area Income' for simple linear regression
y_target = df['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_feature, y_target, test_size=0.3, random_state=42)

# Initialize and train the simple regression model
simple_reg_model = LinearRegression()
simple_reg_model.fit(X_train, y_train)

# Save the trained model
joblib.dump(simple_reg_model, 'simple_linear_regression_model.pkl')