import cv2
import numpy as np

# Reading the required image in which operations are to be done.
# Make sure that the image is in the same directory in which this python program is
img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use the HoughCircles function to detect circles in the image
# Adjust the parameters of HoughCircles as needed
circles = cv2.HoughCircles(gray_blurred, 
                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=50, param2=30, minRadius=15, maxRadius=50)

# If some circles are detected, let's draw them
if circles is not None:
    # Convert the circle parameters a, b and r to integers
    circles = np.round(circles[0, :]).astype("int")
    
    for (x, y, r) in circles:
        # Draw the outer circle
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        # Draw the center of the circle
        cv2.circle(img, (x, y), 3, (0, 255, 255), 3)

# Show the output image with the detected circles
cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
