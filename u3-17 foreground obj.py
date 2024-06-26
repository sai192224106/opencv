import cv2 as cv

# Create a VideoCapture object and read the input video
cap = cv.VideoCapture(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\vid.mp4")

# Check if video is opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit(0)

# Create a background subtractor object
backSub = cv.createBackgroundSubtractorMOG2()

# Variables for tracking purposes
frame_count = 0

while True:
    # Read a new frame
    ret, frame = cap.read()

    if not ret:
        break

    # Update the background model
    fgMask = backSub.apply(frame)

    # Increment frame count
    frame_count += 1

    # Display the resulting frame
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    # Exit on ESC key press
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

# Release video capture and close all windows
cap.release()
cv.destroyAllWindows()
