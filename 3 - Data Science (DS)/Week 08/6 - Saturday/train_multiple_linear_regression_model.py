import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Import the dataset
df = pd.read_csv("housing.csv")

# Drop the Address field
df = df.drop('Address', axis=1)

# Feature matrix and target vector
X_feature = df.drop('Price', axis=1)
y_target = df['Price']

# Updating Feature matrix by dropping Avg. Area Number of Bedrooms
X_feature = X_feature.drop('Avg. Area Number of Bedrooms', axis=1)

# Normalize the feature matrix
scaler = StandardScaler()
X_feature_normalized = scaler.fit_transform(X_feature)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_feature_normalized, y_target, test_size=0.3, random_state=42)

# Initialize and train the multiple regression model
multi_reg_model = LinearRegression()
multi_reg_model.fit(X_train, y_train)

# Save the trained model
joblib.dump(multi_reg_model, 'multiple_linear_regression_model.pkl')
joblib.dump(scaler, 'scaler.pkl')