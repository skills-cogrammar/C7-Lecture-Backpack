import numpy as np
import matplotlib.pyplot as plt

def linear_regression_gradient_descent(data, iterations, theta, learning_rate):
    """
    Performs linear regression using gradient descent algorithm.

    Args:
        data (pandas.DataFrame): The input data containing features and target variable.
        iterations (int): The number of iterations for gradient descent.
        theta (numpy.ndarray): The initial parameters (intercept and coefficient).
        learning_rate (float): The learning rate for gradient descent.

    Returns:
        numpy.ndarray: The learned parameters after performing gradient descent.
    """
    X = data.iloc[:, 1].values  # Extract the feature column (index 1)
    y = data.iloc[:, 2].values  # Extract the target variable column (index 2)

    for _ in range(iterations):
        predictions = theta[0] + theta[1] * X  # Calculate predictions using current parameters

        # Plot the training data and the regression line
        plt.scatter(X, y, color='blue', label='Training Data')
        plt.plot(X, predictions, color='red', label='Regression Line')
        plt.xlabel('Independent Variable')
        plt.ylabel('Dependent Variable')
        plt.title('Linear Regression')
        plt.legend()
        plt.show()

        error = predictions - y  # Calculate error (difference between predictions and actual values)
        gradient_0 = np.mean(error)  # Gradient for intercept term
        gradient_1 = np.mean(error * X)  # Gradient for coefficient of independent variable

        # Update parameters using gradient descent algorithm
        theta[0] -= learning_rate * gradient_0  # Update intercept term
        theta[1] -= learning_rate * gradient_1  # Update coefficient of independent variable

    return theta