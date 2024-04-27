# Importing necessary libraries
import numpy as np  # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for plotting

# Define a function for linear regression with gradient descent
def learning_1(data, iterations, theta, learning_rate):
    # Extracting features (X) and target variable (y) from the DataFrame
    X = data.iloc[:, 1].values  # Extracting the feature column (index 1)
    y = data.iloc[:, 2].values  # Extracting the target variable column (index 2)

    # Perform gradient descent
    for i in range(iterations):
        # Calculate predictions using current parameters
        predictions = theta[0] + theta[1] * X

        # Plot the training data and the regression line
        plt.scatter(X, y, color='blue')  # Scatter plot of the training data
        plt.plot(X, predictions, color='red')  # Plotting the regression line
        plt.xlabel('Independent Variable')  # Label for x-axis
        plt.ylabel('Dependent Variable')  # Label for y-axis
        plt.title('Linear Regression')  # Title of the plot
        plt.legend()  # Adding legend
        plt.show()  # Displaying the plot

        # Calculate error (difference between predictions and actual values)
        error = predictions - y

        # Calculate gradients (partial derivatives of the cost function with respect to parameters)
        gradient_0 = np.mean(error)  # Gradient for intercept term
        gradient_1 = np.mean(error * X)  # Gradient for coefficient of independent variable

        # Update parameters using gradient descent algorithm
        theta[0] = theta[0] - learning_rate * gradient_0  # Update intercept term
        theta[1] = theta[1] - learning_rate * gradient_1  # Update coefficient of independent variable

    return theta  # Return the learned parameters

