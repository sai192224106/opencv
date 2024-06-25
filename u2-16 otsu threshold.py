import cv2

# Read the input image in grayscale
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg', cv2.IMREAD_GRAYSCALE)

# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Apply Otsu's thresholding
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Display the original and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Image (Otsu)', binary_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
