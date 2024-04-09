import numpy as np
import matplotlib.pyplot as plt

# 3
# Sample grayscale images (all of the same size)
image1 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0]])


image2 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],])

image3 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0],])

image4 = np.array([[0, 255, 0, 0, 0, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 255],
                   [0, 0, 0, 0, 255, 0],
                   [0, 0, 0, 0, 255, 0]])

image5 = np.array([[0, 255, 255, 255, 255, 0],
                   [0, 255, 0, 0, 0, 0],
                   [0, 255, 255, 255, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 0, 0, 0, 255, 0],
                   [0, 255, 255, 255, 255, 0]])

# Stack images into a 3D tensor
stacked_tensor = stack_images([image1, image2, image3, image4, image5])

# Display two images from the stacked tensor
display_image(stacked_tensor[0])
display_image(stacked_tensor[1])