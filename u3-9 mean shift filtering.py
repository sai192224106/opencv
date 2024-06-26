import cv2
import numpy as np

# Read the image
img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

# Convert image to Lab color space
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# Parameters for mean shift
# Try experimenting with these values
spatial_radius = 10
color_radius = 20
max_pyramid_level = 1

# Apply mean shift
shifted = cv2.pyrMeanShiftFiltering(lab_image, spatial_radius, color_radius, maxLevel=max_pyramid_level)

# Convert back to BGR color space
result = cv2.cvtColor(shifted, cv2.COLOR_Lab2BGR)

# Display input and result side by side
cv2.imshow('Mean Shift Segmentation', np.hstack([img, result]))
cv2.waitKey(0)
cv2.destroyAllWindows()
