import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define Gabor filter parameters
ksize = 21  # Size of the filter
sigma = 5.0  # Standard deviation of the Gaussian envelope
lambd = 10.0  # Wavelength of the sinusoidal factor
gamma = 0.5  # Spatial aspect ratio
psi = 0  # Phase offset
theta_values = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Orientations

# Apply Gabor filters
filtered_images = []
for theta in theta_values:
    gabor_kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)
    filtered_image = cv2.filter2D(gray_image, cv2.CV_8UC3, gabor_kernel)
    filtered_images.append(filtered_image)

# Stack the filtered images to create a feature map
feature_map = np.stack(filtered_images, axis=-1)

# Reshape feature map for clustering
h, w = gray_image.shape
feature_map_reshaped = feature_map.reshape((-1, len(theta_values)))

# Perform k-means clustering
K = 4  # Number of clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, _ = cv2.kmeans(feature_map_reshaped.astype(np.float32), K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Reshape the labels to the original image shape
segmented_image = labels.reshape((h, w))

# Map the labels to colors for visualization
segmented_image_color = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(K):
    segmented_image_color[segmented_image == i] = np.random.randint(0, 255, 3)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
