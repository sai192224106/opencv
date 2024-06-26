import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels
pixel_values = image.reshape((-1, 3))
# Convert the pixel values to float32 as 
# required by the K-means algorithm in OpenCV.
pixel_values = np.float32(pixel_values)

# Define the criteria for the K-means algorithm
#cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER:
#  The algorithm stops either when the specified accuracy (EPS) is reached 
# or when the maximum number of iterations (MAX_ITER) is reached.
#100: The maximum number of iterations.
#0.2: The desired accuracy (epsilon).
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Define the number of clusters (K)
k = 4  # You can change the number of clusters as needed

# Apply K-means clustering
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert the centers to uint8 (since they are float32)
centers = np.uint8(centers)

# Map the labels to the center values
segmented_image = centers[labels.flatten()]

# Reshape the segmented image to the original image dimensions
segmented_image = segmented_image.reshape(image.shape)

# Display the original and segmented images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.title('Segmented Image')
plt.imshow(segmented_image)
plt.show()
