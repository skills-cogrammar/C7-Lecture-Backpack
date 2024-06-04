# Importing necessary libraries
import pandas as pd  # Pandas for data manipulation
import numpy as np  # NumPy for numerical operations
from learning import learning_1  # Importing the learning_1 function from learning module
import matplotlib.pyplot as plt  # Matplotlib for plotting

# Read the dataset into a DataFrame
data = pd.read_csv("data/salary_dataset.csv")

# Initialize parameters randomly
theta = np.random.randn(2)  # Initialize theta (parameters) randomly

# Define learning rate and number of iterations for gradient descent
learning_rate = 0.01  # Learning rate for gradient descent
iterations = 1000  # Number of iterations for gradient descent

# Perform linear regression with gradient descent
theta = learning_1(data, iterations, theta, learning_rate)

# Print the learned parameters
print("Intercept:", theta[0])  # Print the intercept term of the regression line
print("Coefficient for YearsExperience:", theta[1])  # Print the coefficient for YearsExperience
print()

# Extract features (YearsExperience) and target variable (Salary) from the DataFrame
X = data.iloc[:, 1].values  # Extract the feature column (index 1)
y = data.iloc[:, 2].values  # Extract the target variable column (index 2)

# Calculate predictions using the learned parameters
predictions = theta[0] + theta[1] * X

# Plot the training data and the regression line
plt.scatter(X, y, color='blue', label='Training Data')  # Scatter plot of the training data
plt.plot(X, predictions, color='red', label='Regression Line')  # Plotting the regression line
plt.xlabel('Independent Variable')  # Label for x-axis
plt.ylabel('Dependent Variable')  # Label for y-axis
plt.title('Linear Regression')  # Title of the plot
plt.legend()  # Adding legend
plt.show()  # Displaying the plot
plt.close()  # Closing the plot to avoid overlapping with future plots

