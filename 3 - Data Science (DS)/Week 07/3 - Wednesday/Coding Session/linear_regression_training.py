""" 
Predict salary based on years of experience
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mean_square_error import mean_squared_error_custom
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import r_squared
import numpy as np
from joblib import dump

# Load the dataset from CSV file
data = pd.read_csv('salary_dataset.csv')

# Assuming the first column is the independent variable (X) and the second column is the dependent variable (y)
X = data.iloc[:, 1].values.reshape(-1, 1)
y = data.iloc[:, 2].values

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error
# The square in the formula put everything to exponent. 
# The RMSE is perfect for this. It is not 0 but is insignificant to 
# the current salaries
mse = mean_squared_error_custom(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", mse)


# Calculate R-squared score
r2 = r2_score(y_test, y_pred)
r2_custom = r_squared.r2_score_custom(y_test, y_pred)
print("R-squared Score library:", r2)
print("R-squared Score custom:", r2_custom)
print("Model Intercept: ", model.intercept_)
print("Model Coefficient: ", model.coef_)
print("Model Coefficient: ", model.score(X, y))

# Calculate the residuals
residuals = y_test - y_pred

dump(model, 'salary_model.joblib') 

# Plot the training data, testing data, and the regression line
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Testing Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression')
plt.legend()
plt.show()
plt.close()


