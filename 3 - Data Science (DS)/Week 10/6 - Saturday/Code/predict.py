import pickle
import numpy as np
from PIL import Image
from preprocess import preprocess_images

def predict_digit(image_path, model):
    # Load the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    
    # Resize the image to match the MNIST dataset dimensions (28x28)
    image = image.resize((28, 28))
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Reshape and preprocess the input image
    image_preprocessed = preprocess_images(image_array.reshape(1, 28, 28))
    
    # Make prediction using the trained model
    predicted_label = model.predict(image_preprocessed)
    
    # Get the probabilities for each class
    probabilities = model.predict_proba(image_preprocessed)
    
    # The confidence is the highest probability
    confidence = np.max(probabilities)
    
    return predicted_label[0], confidence

# Load the trained model from the file
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Get the image file path from the user
image_path = input("Enter the path to the image file: ")

# Make prediction on the user input image
predicted_digit, confidence = predict_digit(image_path, model)
print("Predicted Digit:", predicted_digit, "with confidence:", confidence)