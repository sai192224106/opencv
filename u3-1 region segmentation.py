
import cv2
import numpy as np
import matplotlib.pyplot as plt

def region_growing(img, seed, thresh=5):
    # Get the height and width of the image
    h, w = img.shape

# Initialize the seed list with the initial seed point
    seed_list = [seed]

# Create an empty image (mask) with the same dimensions as the input image
# This mask will store the segmented region
    segmented = np.zeros_like(img)

# Set the pixel value of the seed point in the mask to 255 (white)
# This marks the seed point as part of the segmented region
    segmented[seed[1], seed[0]] = 255

# While there are still seed points in the list
    while seed_list:
    # Remove and return the first seed point from the list
        x, y = seed_list.pop(0)
    
    # Check the four connected neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # Calculate the coordinates of the neighbor
            nx, ny = x + dx, y + dy
        
        # Ensure the neighbor's coordinates are within the image bounds
            if 0 <= nx < w and 0 <= ny < h and segmented[ny, nx] == 0:
            # Check if the intensity difference between the neighbor and the current pixel
            # is less than the threshold
                if abs(int(img[ny, nx]) - int(img[y, x])) < thresh:
                # If the neighbor is within the threshold, mark it as part of the segmented region
                    segmented[ny, nx] = 255
                # Add the neighbor to the seed list to further explore its neighbors
                    seed_list.append((nx, ny))

# Return the segmented image (mask)
    return segmented


# Load the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg', cv2.IMREAD_GRAYSCALE)

# Seed point (x, y)
seed = (150, 150)

# Perform region growing
segmented_image = region_growing(image, seed, thresh=10)

# Display the result
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(segmented_image, cmap='gray'), plt.title('Segmented Image')
plt.show()
