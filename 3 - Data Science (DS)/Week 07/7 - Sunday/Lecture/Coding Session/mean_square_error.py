import numpy as np

def mean_squared_error_custom(y_true, y_pred):
    # Calculate the squared differences between true and predicted values
    squared_errors = (y_true - y_pred) ** 2
    
    # Calculate the mean of squared errors
    mse = np.mean(squared_errors)
    
    return mse