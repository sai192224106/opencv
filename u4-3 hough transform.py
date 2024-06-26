import cv2
import numpy as np

# Reading the required image in which operations are to be done.
# Make sure that the image is in the same directory in which this python program is
img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\face.jpeg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load image")
    exit()

# Convert the img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection method on the image
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Show the edges image for debugging
cv2.imshow('Edges', edges)
cv2.waitKey(0)

# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)  # Lowered the threshold from 200 to 100

# Check if lines were detected
if lines is None:
    print("No lines were detected")
    exit()

# The below for loop runs till r and theta values are in the range of the 2d array
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    # Stores the value of cos(theta) in a
    a = np.cos(theta)

    # Stores the value of sin(theta) in b
    b = np.sin(theta)

    # x0 stores the value rcos(theta)
    x0 = a * r

    # y0 stores the value rsin(theta)
    y0 = b * r

    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000 * (-b))

    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000 * (a))

    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000 * (-b))

    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000 * (a))

    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0, 0, 255) denotes the colour of the line to be drawn. In this case, it is red.
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Show the result image with detected lines
cv2.imshow('Lines Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
