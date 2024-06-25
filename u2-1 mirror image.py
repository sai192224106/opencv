import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the dimensions of the image
height, width = gray_image.shape

# Calculate the midpoint
mid = height // 2

# Step 3: Mirror the lower half to the upper half
# Copy the lower half of the image
if height % 2 == 0:
    lower_half = gray_image[mid:height, :]
else:
    lower_half = gray_image[mid + 1:height, :]

# Mirror the lower half to the upper half
gray_image[0:mid, :] = lower_half[::-1, :]

# Step 4: Save the resulting image
cv2.imwrite('mirrored_image.jpg', gray_image)

# Display the result (optional)
cv2.imshow('Mirrored Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
