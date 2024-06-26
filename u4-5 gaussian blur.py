import cv2
import numpy as np

# Read the image from file
img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\face.jpeg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

# Apply Gaussian blur to the image
# (15, 15) is the kernel size, and 0 specifies that the standard deviation in both x and y directions is calculated based on the kernel size
blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

# Display the original image
cv2.imshow('Original Image', img)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_img)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
