import numpy as np
import matplotlib.pyplot as plt

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

class ImageStacker():
    def __init__(self, img_stack):
        self.imgs = img_stack
        pass

    def stack_images(self):
        stacked = np.stack(self.imgs)
        return stacked

    def display_image(self, img):
        plt.imshow(img, cmap="gray")
        plt.show()


img_stack = ImageStacker([image1, image2, image3, image4, image5])

# Stack images into a 3D tensor
stacked_tensor = img_stack.stack_images()

# Display two images from the stacked tensor
img_stack.display_image(stacked_tensor[0])
img_stack.display_image(stacked_tensor[1])
img_stack.display_image(stacked_tensor[2])
img_stack.display_image(stacked_tensor[3])
img_stack.display_image(stacked_tensor[4])
