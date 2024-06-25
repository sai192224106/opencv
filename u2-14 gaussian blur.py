import cv2

# Read the input image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\tree.jpeg')

# Check if image has been successfully read
if image is None:
    print("Error: Could not read the image.")
else:
    # Define the kernel size for Gaussian Blur (should be odd)
    kernel_size = (5, 5)  # Example kernel size (5x5)

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX=0)

    # Display the original and blurred images
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
