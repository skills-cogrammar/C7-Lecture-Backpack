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

        # # Plot the training data and the regression line
        # plt.scatter(X, y, color='blue')  # Scatter plot of the training data
        # plt.plot(X, predictions, color='red')  # Plotting the regression line
        # plt.xlabel('Independent Variable')  # Label for x-axis
        # plt.ylabel('Dependent Variable')  # Label for y-axis
        # plt.title(f'Linear Regression at step {i}')  # Title of the plot
        # plt.legend()  # Adding legend
        # plt.show()  # Displaying the plot

        # Calculate error (difference between predictions and actual values)
        error = predictions - y

        # Calculate gradients (partial derivatives of the cost function with respect to parameters)
        gradient_0 = np.mean(error)  # Gradient for intercept term
        gradient_1 = np.mean(error * X)  # Gradient for coefficient of independent variable

        # Update parameters using gradient descent algorithm
        theta[0] = theta[0] - learning_rate * gradient_0  # Update intercept term
        theta[1] = theta[1] - learning_rate * gradient_1  # Update coefficient of independent variable

    return theta  # Return the learned parameters

def gradient_descent_visualization(data, iterations, theta, learning_rate):
    # Extract feature (X) and target variable (y) from the data
    X = data.iloc[:, 1].values
    y = data.iloc[:, 2].values

    # Initialize lists to store cost and theta history
    cost_history = []
    theta_history = []

    # Perform gradient descent iterations
    for _ in range(iterations):
        # Calculate predictions using current theta values
        predictions = theta[0] + theta[1] * X
        
        # Calculate the error between predictions and actual values
        error = predictions - y
        
        # Calculate the mean squared error as the cost
        cost = np.mean(error ** 2)
        
        # Append the current cost and theta values to the history lists
        cost_history.append(cost)
        theta_history.append(theta.copy())

        # Calculate gradients for theta[0] and theta[1]
        gradient_0 = np.mean(error)
        gradient_1 = np.mean(error * X)

        # Update theta values using the gradients and learning rate
        theta[0] -= learning_rate * gradient_0
        theta[1] -= learning_rate * gradient_1

    # Return the final theta values and theta history
    return theta, theta_history

