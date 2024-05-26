import numpy as np
import matplotlib.pyplot as plt

# Define the loss function
# (y - y_hat)^2

def f(x):
    return x**2

# Define the gradient of the loss function
def loss_derivative_function(x):
    return 2*x

# Gradient descent function
def gradient_descent(initial_point, alpha, num_iters):
    x = initial_point
    x_history = [x]
    
    for i in range(num_iters):
        # Calculate the gradient
        grad = loss_derivative_function(x)
        
        # Update the parameters
        x = x - alpha * grad
        
        # Store the updated parameters
        x_history.append(x)
    
    return x_history

# Initial point
random_initial_point = 2

# Learning rate and number of iterations
# Please change this and run the code
learning_rate = 0.1
num_iters = 100

# Run gradient descent
x_history = gradient_descent(random_initial_point, learning_rate, num_iters)

# Plot the loss function
x = np.linspace(-5, 5, 100)
plt.figure(figsize=(8, 6))
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Loss Function: f(x) = x^2')

# Plot the tangent lines
for i in range(len(x_history)):
    x_point = x_history[i]
    y_point = f(x_point)
    grad = loss_derivative_function(x_point)
    
    # Equation of the tangent line: y = mx + b
    m = grad
    b = y_point - m*x_point
    
    x_tangent = np.linspace(x_point-1, x_point+1, 100)
    y_tangent = m*x_tangent + b
    
    plt.plot(x_tangent, y_tangent, '--', label=f'Iteration {i}')
    plt.scatter(x_point, y_point, color='red')

    plt.legend()
    plt.show()