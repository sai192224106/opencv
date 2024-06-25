import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply the opening operation
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
