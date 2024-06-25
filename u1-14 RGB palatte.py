import cv2
import numpy as np

# Function to update the image color based on trackbar position
def update_color(x):
    # Get the current positions of the trackbars
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')

    # Create a color image with the selected BGR color
    img[:] = [b, g, r]

    # Display the updated image
    cv2.imshow('image', img)

# Read the image from the file
img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
cv2.createTrackbar('B', 'image', 0, 255, update_color)
cv2.createTrackbar('G', 'image', 0, 255, update_color)
cv2.createTrackbar('R', 'image', 0, 255, update_color)

# Display the image with initial color set to black
update_color(0)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
