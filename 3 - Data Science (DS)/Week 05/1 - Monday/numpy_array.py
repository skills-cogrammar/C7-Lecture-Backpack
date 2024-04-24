import numpy as np

#Define a list
distances = [1, 13.1, 26.2, 100]
print(type(distances))
print(distances)
#Output: <class 'list'>
#Output: [1, 13.1, 26.2, 100]

#Convert to numpy array
numpy_dist = np.array(distances)
print(type(numpy_dist))
print(numpy_dist)
#Output: <class 'numpy.ndarray'>
#Output: [1.   13.1  26.2 100.]

#Convert distances in miles to km
#Using numpy scalar mutliplication
conversion = numpy_dist * 1.60934
print(conversion)
#Output: [1.60934, 21.082354, 42.164708, 160.934]

#Using core Python 
#Define an empty array to store km distances
conversion = []

#Using a for loop for conversion
for x in distances:
    conversion.append(x*1.60934)
    
print(conversion)
#Output: [1.60934, 21.082354, 42.164708, 160.934]