import pandas as pd
import numpy as np
from learning import linear_regression_gradient_descent
import matplotlib.pyplot as plt

data = pd.read_csv("data/salary_dataset.csv")  # Read the dataset into a DataFrame
theta = np.random.randn(2)  # Initialize theta (parameters) randomly
learning_rate = 0.01  # Learning rate for gradient descent
iterations = 1000  # Number of iterations for gradient descent

# Perform linear regression with gradient descent
theta = linear_regression_gradient_descent(data, iterations, theta, learning_rate)

print("Intercept:", theta[0])  # Print the intercept term of the regression line
print("Coefficient for YearsExperience:", theta[1])  # Print the coefficient for YearsExperience
print()

X = data.iloc[:, 1].values  # Extract the feature column (index 1)
y = data.iloc[:, 2].values  # Extract the target variable column (index 2)
predictions = theta[0] + theta[1] * X  # Calculate predictions using the learned parameters

# Plot the training data and the regression line
plt.scatter(X, y, color='blue', label='Training Data')
plt.plot(X, predictions, color='red', label='Regression Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression')
plt.legend()
plt.show()
plt.close()