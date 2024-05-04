import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import joblib

# Load the trained models
multi_reg_model = joblib.load('multiple_linear_regression_model.pkl')
simple_reg_model = joblib.load('simple_linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# Import the dataset
df = pd.read_csv("housing.csv")

# Prepare the data for multiple linear regression
X_feature = df.drop(['Price', 'Address', 'Avg. Area Number of Bedrooms'], axis=1)
y_target = df['Price']
X_feature_normalized = scaler.transform(X_feature)
_, X_test, _, y_test = train_test_split(X_feature_normalized, y_target, test_size=0.3, random_state=42)

# Prepare the data for simple linear regression
X_feature_simple = df[['Avg. Area Income']]
y_target_simple = df['Price']
_, X_test_simple, _, y_test_simple = train_test_split(X_feature_simple, y_target_simple, test_size=0.3, random_state=42)

# Predict using multiple linear regression model
y_pred = multi_reg_model.predict(X_test)

# Predict using simple linear regression model
y_pred_simple = simple_reg_model.predict(X_test_simple)

# Performance metrics for multiple linear regression
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print("Multiple Linear Regression:")
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
print(f'Mean Absolute Error: {mae}')

# Performance metrics for simple linear regression
mse_simple = mean_squared_error(y_test_simple, y_pred_simple)
r2_simple = r2_score(y_test_simple, y_pred_simple)
mae_simple = mean_absolute_error(y_test_simple, y_pred_simple)
print("\nSimple Linear Regression:")
print(f'Mean Squared Error: {mse_simple}')
print(f'R-squared: {r2_simple}')
print(f'Mean Absolute Error: {mae_simple}')

# Plot the predicted vs actual for multiple linear regression
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Predicted vs Actual Price - Multiple Linear Regression')
plt.tight_layout()
plt.show()

# Plot the residuals for multiple linear regression
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Price')
plt.ylabel('Residuals')
plt.title('Residuals - Multiple Linear Regression')
plt.tight_layout()
plt.show()

# Plot the predicted vs actual for simple linear regression
plt.figure(figsize=(8, 6))
plt.scatter(y_test_simple, y_pred_simple, color='blue')
plt.plot([y_test_simple.min(), y_test_simple.max()], [y_test_simple.min(), y_test_simple.max()], color='red', linestyle='--')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Predicted vs Actual Price - Simple Linear Regression')
plt.tight_layout()
plt.show()

# Plot the residuals for simple linear regression
residuals_simple = y_test_simple - y_pred_simple
plt.figure(figsize=(8, 6))
plt.scatter(y_pred_simple, residuals_simple, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Price')
plt.ylabel('Residuals')
plt.title('Residuals - Simple Linear Regression')
plt.tight_layout()
plt.show()