import numpy as np

def r2_score_custom(y_true, y_pred):
    # Calculate the mean of the true y values
    y_mean = np.mean(y_true)
    
    # Calculate the total sum of squares (TSS)
    tss = np.sum((y_true - y_mean) ** 2)
    
    # Calculate the residual sum of squares (RSS)
    rss = np.sum((y_true - y_pred) ** 2)
    
    # Calculate R-squared score
    r2 = 1 - (rss / tss)
    
    return r2