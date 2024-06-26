import cv2
import numpy as np

# Function to calculate optical flow
def calculate_optical_flow(prev_frame, curr_frame):
    # Convert frames to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow using Lucas-Kanade method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    return flow

# Open video file
cap = cv2.VideoCapture(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\vid.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")

# Read the first frame
ret, prev_frame = cap.read()

# Loop through the frames
while ret:
    # Read the next frame
    ret, curr_frame = cap.read()
    if not ret:
        break

    # Calculate optical flow
    flow = calculate_optical_flow(prev_frame, curr_frame)

    # Display motion vectors as lines on the current frame
    for y in range(0, curr_frame.shape[0], 10):
        for x in range(0, curr_frame.shape[1], 10):
            # Get the flow vector at this point
            dx, dy = flow[y, x]

            # Draw line to show the motion vector
            cv2.line(curr_frame, (x, y), (int(x + dx), int(y + dy)), (0, 255, 0), 1)
            cv2.circle(curr_frame, (x, y), 1, (0, 255, 0), -1)

    # Show the frame with motion vectors
    cv2.imshow('Motion Vectors', curr_frame)

    # Update the previous frame
    prev_frame = curr_frame.copy()

    # Exit if ESC key is pressed
    if cv2.waitKey(30) == 27:
        break

# Release video capture object and close windows
cap.release()
cv2.destroyAllWindows()
