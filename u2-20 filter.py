import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Convert BGR to HSV (Hue, Saturation, Value)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([90, 50, 50])   # Lower bound for blue color
    upper_blue = np.array([130, 255, 255])  # Upper bound for blue color

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
