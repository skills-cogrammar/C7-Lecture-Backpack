from joblib import load

# Load the trained machine learning model
clf = load('salary_model.joblib')

# Prompt the user to input the years of experience
years_of_experience = float(input("Input the years of experience of the employee: "))

# Use the loaded model to predict the salary based on the input years of experience
predicted_salary = clf.predict([[years_of_experience]])

print("Predicted Salary:", predicted_salary[0])