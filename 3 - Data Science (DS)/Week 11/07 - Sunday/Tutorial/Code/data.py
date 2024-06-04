import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# def data():
#     # Create a small dataset
#     data = {
#         'feature1': [1, 2, 3, 4, 5],
#         'feature2': [2, 3, 4, 5, 6],
#         'target': [1, 0, 1, 0, 1]
#     }

#     df = pd.DataFrame(data)
#     X = df[['feature1', 'feature2']].values
#     y = df['target'].values
#     return X, y 

iris_data_source = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
def data():
    col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
    iris =  pd.read_csv(iris_data_source, names = col_names)
    # Case-like structure
    X = iris[['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']].values
    y = iris['Species'].values
    # Declare dictionary to map each number to its corresponding text
    dictionary = {'Iris-setosa':0 ,'Iris-versicolor':1 ,'Iris-virginica': 2}
    # Translate each number to text using the dictionary
    y = np.array([dictionary[i] for i in y]).reshape(-1, 1)
    # One-hot encode the target variable
    encoder = OneHotEncoder(sparse=False)
    y = encoder.fit_transform(y)
    return X, y 