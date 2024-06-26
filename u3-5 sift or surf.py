import cv2
import numpy as np

# Load the main image and template image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg')
template = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg', 0)

# Convert main image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply template matching
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Get the location of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the matched region
top_left = max_loc
h, w = template.shape
bottom_left = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_left, (0, 255, 0), 2)

# Display the result
cv2.imshow('Template Matching', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
