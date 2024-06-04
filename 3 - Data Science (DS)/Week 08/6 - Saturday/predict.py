import numpy as np
import pandas as pd
import joblib

# Load the trained models
multi_reg_model = joblib.load('multiple_linear_regression_model.pkl')
simple_reg_model = joblib.load('simple_linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# User input for multiple linear regression
print("Enter the following details for multiple linear regression prediction:")
avg_area_income = float(input("Average Area Income: "))
avg_area_house_age = float(input("Average Area House Age: "))
avg_area_number_of_rooms = float(input("Average Area Number of Rooms: "))
avg_area_population = float(input("Average Area Population: "))

# Create a DataFrame with the user input and appropriate feature names
user_input_df = pd.DataFrame({
    'Avg. Area Income': [avg_area_income],
    'Avg. Area House Age': [avg_area_house_age],
    'Avg. Area Number of Rooms': [avg_area_number_of_rooms],
    'Area Population': [avg_area_population]
})

# Scale the user input using the loaded scaler
user_input_scaled = scaler.transform(user_input_df)

# Predict using multiple linear regression model
price_prediction = multi_reg_model.predict(user_input_scaled)
print(f"\nPredicted Price (Multiple Linear Regression): ${price_prediction[0]:.2f}")

# User input for simple linear regression
print("\nEnter the following details for simple linear regression prediction:")
avg_area_income_simple = float(input("Average Area Income: "))

# Create a DataFrame with the user input and appropriate feature name
user_input_simple_df = pd.DataFrame({
    'Avg. Area Income': [avg_area_income_simple]
})

# Predict using simple linear regression model
price_prediction_simple = simple_reg_model.predict(user_input_simple_df)
print(f"\nPredicted Price (Simple Linear Regression): ${price_prediction_simple[0]:.2f}")