import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt

from mean_square_error import mean_squared_error_custom
import r_squared
from joblib import dump

# Load the dataset from CSV file
data = pd.read_csv('salary_dataset_large.csv')

# # Assuming the first column is the independent variable (X) and the second column is the dependent variable (y)
# X = data.iloc[:, 1].values.reshape(-1, 1)
# y = data.iloc[:, 2].values

X = data['Years of Experience'].values.reshape(-1, 1)
y = data['Salary'].values

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Define the hyperparameter grid for tuning (grid search)
param_grid = {
    'fit_intercept': [True, False],
    'positive': [True, False],
}

# Perform grid search for hyperparameter tuning
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best model after hyperparameter tuning
best_model = grid_search.best_estimator_

# Train the model on the training data
best_model.fit(X_train, y_train)

dump(best_model, 'salary_model.joblib')

# Make predictions on the testing data
y_pred = best_model.predict(X_test)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
mse_custom = mean_squared_error_custom(y_test, y_pred)
print("Mean Squared Error library:", mse)
print("Mean Squared Error custom:", mse_custom)

# Calculate R-squared score
r2 = r2_score(y_test, y_pred)
r2_custom = r_squared.r2_score_custom(y_test, y_pred)
print("R-squared Score library:", r2)
print("R-squared Score custom:", r2_custom)

# y = intercept + coefficient * X
print("Best Model Intercept: ", best_model.intercept_)
print("Best Model Coefficient: ", best_model.coef_)
print("Best Model Score: ", best_model.score(X, y))

# Plot the training data, testing data, and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Testing Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression')
plt.legend()
plt.show()
plt.close()