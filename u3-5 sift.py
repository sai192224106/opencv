import cv2

# Load the main image and template image
image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg')
template = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird1.jpeg')

# Convert images to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Initialize the SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints_image, descriptors_image = sift.detectAndCompute(gray_image, None)
keypoints_template, descriptors_template = sift.detectAndCompute(gray_template, None)

# Use the BFMatcher to match descriptors
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors_template, descriptors_image)

# Sort matches by distance (best matches first)
matches = sorted(matches, key=lambda x: x.distance)

# Draw the first 10 matches
result_image = cv2.drawMatches(template, keypoints_template, image, keypoints_image, matches[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the result
cv2.imshow('Feature-Based Matching', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
