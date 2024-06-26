import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Reshape the image to a 2D array of pixels (height*width, 3)
pixels = image.reshape((-1, 3))
pixels = np.float32(pixels)

# Define criteria for K-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Perform K-means clustering
k = 5  # Number of clusters
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers from float32 back to uint8
centers = np.uint8(centers)

# Map each pixel to its corresponding centroid color
segmented_image = centers[labels.flatten()]

# Reshape back the image to its original dimensions
segmented_image = segmented_image.reshape(image.shape)

# Display original image and segmented image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image (K=5)')
plt.axis('off')

plt.tight_layout()
plt.show()
