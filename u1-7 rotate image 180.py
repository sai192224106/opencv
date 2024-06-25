import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

if image is None:
    print("Failed to read the image.")
else:
    # Rotate the image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    # Display the original and rotated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated_image)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()