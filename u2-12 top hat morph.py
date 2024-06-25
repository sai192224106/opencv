import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply the opening operation
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Compute the top hat transformation
top_hat_image = cv2.subtract(image, opened_image)

# Display the original and top hat images
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Image', top_hat_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
