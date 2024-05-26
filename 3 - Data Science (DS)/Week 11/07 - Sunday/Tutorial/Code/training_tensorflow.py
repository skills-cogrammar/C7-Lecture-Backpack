# First please install the following
# pip install tensorflow 

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

random_state = 42
learning_rate = 0.01
reg_lambda =0.01
epochs = 1000
verbose = 2
validation_split = 0.2

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define a function to create a neural network model
def create_model(regularization=None):
    model = keras.Sequential([
        keras.layers.Dense(5, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        keras.layers.Dense(3, activation='softmax', kernel_regularizer=regularization)
    ])
    model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Create and train the model without regularization
model_no_reg = create_model()
history_no_reg = model_no_reg.fit(X_train_scaled, y_train, epochs = epochs, validation_split = validation_split, verbose=verbose)

# Create and train the model with L1 regularization
model_l1 = create_model(regularization=keras.regularizers.l1(reg_lambda))
history_l1 = model_l1.fit(X_train_scaled, y_train, epochs = epochs, validation_split = validation_split, verbose=verbose)

# Create and train the model with L2 regularization
model_l2 = create_model(regularization=keras.regularizers.l2(reg_lambda))
history_l2 = model_l2.fit(X_train_scaled, y_train, epochs = epochs, validation_split = validation_split, verbose=verbose)

# Evaluate the models on the test set
loss_no_reg, accuracy_no_reg = model_no_reg.evaluate(X_test_scaled, y_test)
loss_l1, accuracy_l1 = model_l1.evaluate(X_test_scaled, y_test)
loss_l2, accuracy_l2 = model_l2.evaluate(X_test_scaled, y_test)

# Print the test loss
print("Test Loss without regularization:", loss_no_reg)
print("Test Loss with L1 regularization:", loss_l1)
print("Test Loss with L2 regularization:", loss_l2)
