import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image in grayscale
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg', cv2.IMREAD_GRAYSCALE)


# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Reshape the image into a 1D array of pixels
    pixels = image.flatten().astype(np.float32)

    # Perform PCA
    mean, eigenvectors = cv2.PCACompute(pixels, mean=None)

    # Choose the number of principal components to analyze
    num_components = 5  # For example, analyze the top 3 principal components

    # Project original data onto principal components
    projected = cv2.PCAProject(pixels, mean, eigenvectors[:, :num_components])

    # Reconstruct the image from projected data
    reconstructed_pixels = cv2.PCABackProject(projected, mean, eigenvectors[:, :num_components])
    reconstructed_image = np.reshape(reconstructed_pixels, image.shape)

    # Display the original image and reconstructed image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title('Reconstructed Image using PCA')

    # Show plot
    plt.tight_layout()
    plt.show()
