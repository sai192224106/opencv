import cv2
import numpy as np

def apply_averaging_filter(image_path, kernel_size):

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image at path {image_path} could not be found.")

    # Create the averaging kernel
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    # Apply the filter using cv2.filter2D
    smoothed_image = cv2.filter2D(image, -1, kernel)

    return smoothed_image

# Example usage
smoothed_img = apply_averaging_filter(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg', 3)
cv2.imshow('smoothed img', smoothed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
