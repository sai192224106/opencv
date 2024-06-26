import cv2 as cv
import numpy as np

# Load two consecutive frames
frame1 = cv.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg", cv.IMREAD_GRAYSCALE)
frame2 = cv.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\bird2.jpeg", cv.IMREAD_GRAYSCALE)

# Check if images are loaded
if frame1 is None or frame2 is None:
    print("Could not open or find the images!")
    exit(0)

# Calculate optical flow using Farneback method
flow = cv.calcOpticalFlowFarneback(frame1, frame2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

# Compute the magnitude and angle of the flow
magnitude, angle = cv.cartToPolar(flow[..., 0], flow[..., 1])

# Create an HSV image to visualize the optical flow
hsv = np.zeros_like(cv.cvtColor(frame1, cv.COLOR_GRAY2BGR))
hsv[..., 1] = 255  # Set saturation to maximum

# Set hue according to the flow direction
hsv[..., 0] = angle * 180 / np.pi / 2

# Set value according to the flow magnitude (normalized)
hsv[..., 2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)

# Convert HSV image to BGR for visualization
flow_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# Display the optical flow
cv.imshow('Optical Flow', flow_bgr)
cv.waitKey(0)
cv.destroyAllWindows()
