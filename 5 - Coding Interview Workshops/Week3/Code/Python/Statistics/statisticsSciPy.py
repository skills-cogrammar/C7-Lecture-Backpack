from scipy import stats
import numpy as np

data = np.array([23, 78, 789, 12, 90, 384, 12, 3759, 109, 45, 67])

# This function returns descriptive statistics for this dataset
# Including mean, variance, min and max
print(stats.describe(data))



