import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
original_image = image_rgb.copy()

# Convert to grayscale
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Apply Gaussian blur to reduce noise
image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

# Compute gradient using Sobel operators
gradient_x = cv2.Sobel(image_blur, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image_blur, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Convert gradient magnitude to 8-bit for thresholding
gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

# Threshold gradient magnitude to obtain markers
_, markers = cv2.threshold(gradient_magnitude, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Perform morphological operations to clean up markers
kernel = np.ones((3, 3), np.uint8)
markers = cv2.morphologyEx(markers, cv2.MORPH_CLOSE, kernel)
markers = cv2.morphologyEx(markers, cv2.MORPH_OPEN, kernel)

# Convert markers to 32-bit integer
markers = np.int32(markers)

# Apply watershed algorithm
markers = cv2.watershed(image_rgb, markers)

# Create a mask to overlay watershed boundaries
overlay = image_rgb.copy()
overlay[markers == -1] = [255, 0, 0]  # Mark watershed boundaries in red

# Display the result
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(122)
plt.imshow(overlay)
plt.title('Watershed Segmentation')
plt.axis('off')
plt.show()
