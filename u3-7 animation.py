import cv2
import numpy as np

# Load image sequence (for simplicity, load from individual files)
frame1 = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg')
frame2 = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg')

# Convert frames to grayscale
prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
curr_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# Verify image dimensions
if prev_gray.shape != curr_gray.shape:
    print("Error: Image dimensions do not match.")
    exit()

# Lucas-Kanade parameters
lk_params = dict(winSize=(15, 15),
                maxLevel=2,
                criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Define initial points to track (for simplicity, use Shi-Tomasi corner detection)
prev_pts = cv2.goodFeaturesToTrack(prev_gray, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Calculate optical flow (Lucas-Kanade method)
if prev_pts is not None:
    prev_pts = np.float32(prev_pts.reshape(-1, 1, 2))
    next_pts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, curr_gray, prev_pts, None, **lk_params)

    # Create an animation by warping pixels based on the optical flow
    flow_map = np.zeros_like(frame1)
    for i, (new, old) in enumerate(zip(next_pts, prev_pts)):
        a, b = new.ravel()
        c, d = old.ravel()
        cv2.line(flow_map, (a, b), (c, d), (0, 255, 0), 2)
        cv2.circle(frame2, (a, b), 5, (0, 255, 0), -1)

    # Display animation
    cv2.imshow('Optical Flow Animation', frame2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: No points to track.")

