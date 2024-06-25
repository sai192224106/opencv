import cv2

# Read the input image in grayscale
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg', cv2.IMREAD_GRAYSCALE)

# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Set a threshold value manually (you can experiment with different values)
    threshold_value = 100

    # Apply simple binary thresholding
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Thresholded Image', binary_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
