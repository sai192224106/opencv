import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Read and convert the image to grayscale
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg', cv2.IMREAD_GRAYSCALE)

# Step 3: Define Robert's Cross Operator
roberts_cross_v = np.array([[1, 0], [0, -1]], dtype=int)
roberts_cross_h = np.array([[0, 1], [-1, 0]], dtype=int)

# Step 4: Apply the convolution
# Vertical Gradient
vertical = cv2.filter2D(image, -1, roberts_cross_v)
# Horizontal Gradient
horizontal = cv2.filter2D(image, -1, roberts_cross_h)

# Step 5: Compute the gradient magnitude
edges = np.sqrt(np.square(horizontal) + np.square(vertical))
edges = np.clip(edges, 0, 255).astype(np.uint8)

# Step 6: Display the original and edge-detected images
plt.figure(figsize=(10, 7))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Robert Edge Detection')
plt.imshow(edges, cmap='gray')

plt.show()
