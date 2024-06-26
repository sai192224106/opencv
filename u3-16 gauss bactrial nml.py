import cv2 as cv
import numpy as np

# Load the noisy image
noisy_image = cv.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\bird2.jpeg")

# Check if image is loaded
if noisy_image is None:
    print("Could not open or find the image!")
    exit(0)

# Convert the image to grayscale for denoising
gray_image = cv.cvtColor(noisy_image, cv.COLOR_BGR2GRAY)

# Apply Gaussian filtering
gaussian_denoised = cv.GaussianBlur(gray_image, (5, 5), 0)
#d: Diameter of each pixel neighborhood used during filtering. If it is non-positive, it is computed from sigmaSpace. In this example, it is 9.
#sigmaColor: Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together, resulting in larger areas of semi-equal color. In this example, it is 75.
#sigmaSpace: Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor). 

# Apply Bilateral filtering
bilateral_denoised = cv.bilateralFilter(gray_image, 9, 75, 75)
#dst: Destination image. In the function call, it can be None because the function returns the result directly.
#h: Parameter regulating filter strength. A larger h value removes noise effectively but also removes image details. In this example, it is 30.
#templateWindowSize: Size (in pixels) of the window used to compute weighted average for the given pixel. It should be odd. A typical value is 7.
#searchWindowSize: Size (in pixels) of the window used to search for pixels with similar colors. It should be odd. A typical value is 21.
# Apply Non-local Means denoising
nlm_denoised = cv.fastNlMeansDenoising(gray_image, None, 30, 7, 21)

# Display the original and denoised images
cv.imshow('Original Noisy Image', gray_image)
cv.imshow('Gaussian Denoised', gaussian_denoised)
cv.imshow('Bilateral Denoised', bilateral_denoised)
cv.imshow('Non-local Means Denoised', nlm_denoised)

cv.waitKey(0)
cv.destroyAllWindows()
