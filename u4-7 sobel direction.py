import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image from file
img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\face.jpeg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the gradients along the x and y axis using the Sobel operator
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradient along the x-axis
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradient along the y-axis

# Compute the gradient magnitude and direction
magnitude = cv2.magnitude(grad_x, grad_y)
direction = cv2.phase(grad_x, grad_y, angleInDegrees=True)

# Normalize the magnitude to the range [0, 255] for display purposes
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Display the original image
cv2.imshow('Original Image', img)

# Display the gradient magnitude image
cv2.imshow('Gradient Magnitude', np.uint8(magnitude))

# Display the gradient direction image
# Normalize the direction to the range [0, 255] for display purposes
direction_normalized = cv2.normalize(direction, None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('Gradient Direction', np.uint8(direction_normalized))

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally, use matplotlib to plot the results for better visualization
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Gradient Magnitude')
plt.imshow(magnitude, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Gradient Direction')
plt.imshow(direction_normalized, cmap='gray')

plt.show()
