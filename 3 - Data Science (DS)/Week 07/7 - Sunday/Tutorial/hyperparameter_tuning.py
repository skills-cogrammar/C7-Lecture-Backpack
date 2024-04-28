import pandas as pd
import numpy as np
from learning import learning_1
import matplotlib.pyplot as plt

# Load the dataset from CSV file
data = pd.read_csv("data/salary_dataset.csv")

# Define different learning rates and iterations to try
learning_rates = [0.01, 0.05, 0.1]
iterations_list = [100, 500, 1000]

# Iterate over different learning rates and iterations
for learning_rate in learning_rates:
    for iterations in iterations_list:
        # Initialize theta randomly for each combination
        theta = np.random.randn(2)
        
        # Perform linear regression with the current hyperparameters
        theta = learning_1(data, iterations, theta, learning_rate)

        # Extract feature (X) and target variable (y) from the data
        X = data.iloc[:, 1].values
        y = data.iloc[:, 2].values
        
        # Calculate predictions using the learned theta values
        predictions = theta[0] + theta[1] * X

        # Plot the training data and regression line for each combination
        plt.scatter(X, y, color='blue', label='Training Data')
        plt.plot(X, predictions, color='red', label=f'LR={learning_rate}, Iter={iterations}')
        plt.xlabel('Independent Variable')
        plt.ylabel('Dependent Variable')
        plt.title('Linear Regression with Different Hyperparameters')
        plt.legend()
        plt.show()
        plt.close()