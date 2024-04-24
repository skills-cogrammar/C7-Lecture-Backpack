# Importing the numpy library and aliasing it as np for ease of use.
import numpy as np  

# Defining a function called r2_score_custom that calculates the R-squared score.
def r2_score_custom(y_true, y_pred):
    # Calculate the mean of the true y values.
    y_mean = np.mean(y_true)
    
    # Calculate the total sum of squares (TSS).
    tss = np.sum((y_true - y_mean) ** 2)
    
    # Calculate the residual sum of squares (RSS).
    rss = np.sum((y_true - y_pred) ** 2)
    
    # Calculate R-squared score.
    r2 = 1 - (rss / tss)
    
    # Return the calculated R-squared score.
    return r2  

