import cv2
import numpy as np

# Load stereo image pair
img_left = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg', 0)
img_right = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st3.jpeg', 0)

# Check if images are loaded correctly
if img_left is None or img_right is None:
    print("Error: Could not read the images.")
    exit()

# StereoSGBM parameters
min_disparity = 0
num_disparities = 128
block_size = 5
uniqueness_ratio = 10
speckle_window_size = 100
speckle_range = 32
disp12_max_diff = 1
pre_filter_cap = 63
P1 = 8 * 3 * block_size ** 2
P2 = 32 * 3 * block_size ** 2

# Compute disparity map
stereo = cv2.StereoSGBM_create(minDisparity=min_disparity,
                               numDisparities=num_disparities,
                               blockSize=block_size,
                               uniquenessRatio=uniqueness_ratio,
                               speckleWindowSize=speckle_window_size,
                               speckleRange=speckle_range,
                               disp12MaxDiff=disp12_max_diff,
                               preFilterCap=pre_filter_cap,
                               P1=P1,
                               P2=P2)
disparity_map = stereo.compute(img_left, img_right)

# Normalize the disparity map for visualization
disparity_map = cv2.normalize(disparity_map, disparity_map, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_map = np.uint8(disparity_map)

# Display the disparity map
cv2.imshow('Disparity Map', disparity_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the disparity map
cv2.imwrite('disparity_map.jpg', disparity_map)


#import cv2 as cv
#import numpy as np
#import time

# Load the left and right images
#img_left = cv.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg', cv.IMREAD_GRAYSCALE)
#img_right = cv.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st3.jpeg', cv.IMREAD_GRAYSCALE)

# Check if images are loaded
#if img_left is None or img_right is None:
#    print("Could not open or find the images!")
#    exit(0)

# Initialize the stereo block matcher
#stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)

# Compute the disparity map
#start_time = time.time()
#disparity = stereo.compute(img_left, img_right)
#end_time = time.time()

# Normalize the disparity map for visualization
#disparity = cv.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
#disparity = np.uint8(disparity)

# Display the disparity map
#cv.imshow('Disparity Map', disparity)
#cv.waitKey(0)
#cv.destroyAllWindows()

# Print the computation time
#print(f"Computation Time: {end_time - start_time} seconds")
