import cv2 as cv
import numpy as np

# Load the images
img1 = cv.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st1.jpeg', cv.IMREAD_GRAYSCALE)  # Query image
img2 = cv.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\st3.jpeg', cv.IMREAD_GRAYSCALE)  # Train image

# Check if images are loaded
if img1 is None or img2 is None:
    print("Could not open or find the images!")
    exit(0)

# Initialize SIFT detector
sift = cv.SIFT_create()

# Find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Initialize the BFMatcher (Brute Force Matcher)
bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort them in the order of their distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw the first 10 matches
img_matches = cv.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the matches
cv.imshow('Feature Matches', img_matches)
cv.waitKey(0)
cv.destroyAllWindows()
