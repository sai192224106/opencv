import cv2
import numpy as np

# Read the image from file
img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\face.jpeg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a SIFT detector object
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw the keypoints on the image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the original image
cv2.imshow('Original Image', img)

# Display the image with keypoints
cv2.imshow('Image with SIFT Keypoints', img_with_keypoints)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
