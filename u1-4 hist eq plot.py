

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\nature1.jpeg'  # replace with your image path
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(original_image)

# Plot the original and equalized images for comparison
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap="gray")
plt.title('Original Image')
plt.axis('off')

# Equalized Image
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()

# Plot the histograms of the original and equalized images
plt.figure(figsize=(10, 5))

# Histogram of Original Image
plt.subplot(1, 2, 1)
plt.hist(original_image.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')

# Histogram of Equalized Image
plt.subplot(1, 2, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')

plt.show()
