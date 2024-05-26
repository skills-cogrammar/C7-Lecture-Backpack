import matplotlib.pyplot as plt
import numpy as np
from data import data

# retrieve the data
X, y = data()

# parameters
epochs = 1000
# random_state = np.random.randint(0,10000)
random_state = 42
learning_rate = 0.01
reg_lambda =0.01

# Initialize parameters
input_size = X.shape[1]  # Number of input features (4 for Iris)
hidden_size = 5          # Number of hidden units (arbitrary choice)
output_size = 3          # Number of output units (3 classes for Iris)

# Weights initialization
np.random.seed(random_state)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# Activation function: Sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Derivative of sigmoid
def sigmoid_derivative(z):
    return z * (1 - z)

# Activation function: Softmax
def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# Loss function: Categorical Cross-Entropy
def categorical_crossentropy(y_true, y_pred):
    return -np.sum(y_true * np.log(y_pred + 1e-9)) / y_true.shape[0]

# Forward pass
def forward_pass(X):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = softmax(z2)
    return z1, a1, z2, a2

# Backward pass with regularization
def backward_pass(X, y, z1, a1, z2, a2, alpha, reg_type, lambda_):
    global W1, b1, W2, b2
    
    # Compute the error
    error = a2 - y
    
    # Output layer gradients
    dW2 = np.dot(a1.T, error)
    db2 = np.sum(error, axis=0, keepdims=True)
    
    # Hidden layer gradients
    dA1 = np.dot(error, W2.T)
    dW1 = np.dot(X.T, dA1 * sigmoid_derivative(a1))
    db1 = np.sum(dA1 * sigmoid_derivative(a1), axis=0, keepdims=True)
    
    # Apply regularization
    if reg_type == 'L1':
        dW2 += lambda_ * np.sign(W2)
        dW1 += lambda_ * np.sign(W1)
    elif reg_type == 'L2':
        dW2 += lambda_ * W2
        dW1 += lambda_ * W1
    
    # Update weights and biases
    W1 -= alpha * dW1
    b1 -= alpha * db1
    W2 -= alpha * dW2
    b2 -= alpha * db2

# Training function
def train(X, y, epochs, alpha, reg_type=None, lambda_=0):
    losses = []
    for epoch in range(epochs):
        z1, a1, z2, a2 = forward_pass(X)
        backward_pass(X, y, z1, a1, z2, a2, alpha, reg_type, lambda_)
        loss = categorical_crossentropy(y, a2)
        losses.append(loss)
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss}')
    return losses

# Train without regularization
print("Training without regularization")
np.random.seed(random_state)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))
losses_no_reg = train(X, y, epochs=epochs, alpha=learning_rate)

# Train with L1 regularization
print("\nTraining with L1 regularization")
np.random.seed(random_state)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))
losses_l1_reg = train(X, y, epochs=epochs, alpha=learning_rate, reg_type='L1', lambda_=reg_lambda)

# Train with L2 regularization
print("\nTraining with L2 regularization")
np.random.seed(random_state)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))
losses_l2_reg = train(X, y, epochs=epochs, alpha=learning_rate, reg_type='L2', lambda_=reg_lambda)

# Plot the results
plt.plot(losses_no_reg, label='No Regularization')
plt.plot(losses_l1_reg, label='L1 Regularization')
plt.plot(losses_l2_reg, label='L2 Regularization')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss with Different Regularization Techniques')
plt.legend()
plt.show()
