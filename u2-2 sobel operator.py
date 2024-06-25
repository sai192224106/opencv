import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\nature1.jpeg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply the Sobel operator
# Calculate the x and y gradients using the Sobel operator
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel operator on the x axis
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel operator on the y axis

# Step 4: Combine the Sobel gradients
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Normalize the result to the range [0, 255]
sobel_combined = np.uint8(255 * sobel_combined / np.max(sobel_combined))

# Display the result (optional)
cv2.imshow('Sobel Edge Detected Image', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
