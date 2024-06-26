import cv2
import numpy as np

# Load stereo images
left_img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg', 0)
right_img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st3.jpeg', 0)

# Check if images are loaded successfully
if left_img is None or right_img is None:
    print("Error: Could not load stereo images.")
    exit()

# Stereo block matching
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(left_img, right_img)

# Normalize the disparity map for display
min_disp = disparity.min()
max_disp = disparity.max()
disparity = np.uint8(255 * (disparity - min_disp) / (max_disp - min_disp))

# Display the disparity map
cv2.imshow('Disparity Map', disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()
