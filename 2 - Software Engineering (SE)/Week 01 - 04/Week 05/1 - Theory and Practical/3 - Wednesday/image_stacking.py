import numpy as np
import matplotlib.pyplot as plt

# Sample grayscale images (all of the same size)
image1 = np.array([[0, 10, 20],
                   [30, 40, 50],
                   [60, 70, 80]])

image2 = np.array([[5, 15, 25],
                   [35, 45, 55],
                   [65, 75, 85]])

image3 = np.array([[1, 11, 21],
                   [31, 41, 51],
                   [61, 71, 81]])

image4 = np.array([[2, 12, 22],
                   [32, 42, 52],
                   [62, 72, 82]])

image5 = np.array([[3, 13, 23],
                   [33, 43, 53],
                   [63, 73, 83]])

# Stack images into a 3D tensor
stacked_tensor = stack_images([image1, image2, image3, image4, image5])

# Display two images from the stacked tensor
display_image(stacked_tensor[0])
display_image(stacked_tensor[1])