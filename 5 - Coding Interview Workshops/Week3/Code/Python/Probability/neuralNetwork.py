import numpy as np

# Define the sigmoid activation function for neural networks
def sigmoid(x):
    # This function maps any value to a value between 0 and 1, which can be interpreted as a probability.
    return 1 / (1 + np.exp(-x))

# Define a single layer of a neural network
def neural_network_layer(inputs, weights, biases):
    # Perform matrix multiplication between inputs and weights and add biases.
    # This linear algebra operation is the basis of data transformation in neural networks.
    layer_input = np.dot(inputs, weights) + biases
    
    # Apply the sigmoid activation function to introduce non-linearity.
    # Non-linearity allows the network to learn more complex patterns.
    layer_output = sigmoid(layer_input)
    return layer_output

# Initialize weights (for 2 inputs to 1 output) and biases for the layer
weights = np.array([[0.7], [-0.3]])
biases = np.array([0.1])

# Example input vector (2 inputs)
inputs = np.array([0.5, 0.25])

# Perform a forward pass through the network layer
output = neural_network_layer(inputs, weights, biases)
print("Neural Network Output:", output)
