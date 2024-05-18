import numpy as np
from skimage import exposure

# Preprocessing function
def preprocess_images(X):
    X_preprocessed = []
    for image in X:
        # Apply contrast stretching
        p2, p98 = np.percentile(image, (2, 98))
        img_rescale = exposure.rescale_intensity(image, in_range=(p2, p98), out_range=(0, 1))
        
        # Clip the values to the valid range [0, 1]
        img_rescale = np.clip(img_rescale, 0, 1)
        
        # Flatten the preprocessed image
        img_flat = img_rescale.flatten()
        X_preprocessed.append(img_flat)
    return np.array(X_preprocessed)