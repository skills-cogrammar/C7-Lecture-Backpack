import numpy as np
import scipy as sp
import scipy.stats as stats

heights = [168, 170, 150, 160, 182, 140, 175, 191, 152, 150]

# Mean
mean = np.mean(heights)
print(mean)

# Median
median = np.median(heights)
print(median)

# Mode
mode = sp.stats.mode(heights)
print(mode)

# Variance
var = np.var(heights)
print(var)

# Standard Deviation
std = np.std(heights)


