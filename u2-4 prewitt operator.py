import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the image path
image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg'

# Read the image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print(f"Error: Could not open or find the image at {image_path}")
    exit()

# Define the Prewitt kernels
prewitt_kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitt_kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

# Apply the Prewitt operator
prewitt_x = cv2.filter2D(image, -1, prewitt_kernel_x)
prewitt_y = cv2.filter2D(image, -1, prewitt_kernel_y)

# Convert to float32
prewitt_x = prewitt_x.astype(np.float32)
prewitt_y = prewitt_y.astype(np.float32)

# Combine the two gradients
prewitt_combined = cv2.magnitude(prewitt_x, prewitt_y)

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1), plt.imshow(prewitt_x, cmap='gray'), plt.title('Prewitt X')
plt.subplot(1, 3, 2), plt.imshow(prewitt_y, cmap='gray'), plt.title('Prewitt Y')
plt.subplot(1, 3, 3), plt.imshow(prewitt_combined, cmap='gray'), plt.title('Prewitt Combined')
plt.show()
