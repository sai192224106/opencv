import cv2

# Read the input image in grayscale
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg', cv2.IMREAD_GRAYSCALE)

# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Apply Adaptive Thresholding
    binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Display the original and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Adaptive Thresholding', binary_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
