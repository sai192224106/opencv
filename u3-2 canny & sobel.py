import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, 100, 200)

cv2.imshow("canny edge",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

grad_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

grad_magnitude = cv2.magnitude(grad_x, grad_y)
grad_magnitude = cv2.normalize(grad_magnitude, None, 0, 255, cv2.NORM_MINMAX)
grad_magnitude = grad_magnitude.astype(np.uint8)

cv2.imshow("sobel operator",grad_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()