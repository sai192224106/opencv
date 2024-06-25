import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply the closing operation
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Compute the black hat transformation
black_hat_image = cv2.subtract(closed_image, image)

# Display the original and black hat images
cv2.imshow('Original Image', image)
cv2.imshow('Black Hat Image', black_hat_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
