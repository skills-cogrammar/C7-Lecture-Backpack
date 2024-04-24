# Importing the load function from the joblib library.
from joblib import load  

# Loading the trained machine learning model stored in the file 'salary_model.joblib' and assigning it to the variable clf.
clf = load('salary_model.joblib')  

# Prompting the user to input the years of experience of the employee and converting it to a floating-point number.
years_of_experience = float(input("Input the years of experience of the employee: "))  

# Using the loaded model to predict the salary based on the input years of experience and printing the result.
print(clf.predict([[years_of_experience]]))  


