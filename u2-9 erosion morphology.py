import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply the erosion operation
eroded_image = cv2.erode(image, kernel, iterations=2)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
