import cv2

# Path to the input video file
input_video_path = r"C:\Users\Harsha\OneDrive\Documents\opencv_img\car1.mp4"

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Start reading the video from the last frame to the first
frame_index = total_frames - 1

while cap.isOpened():
    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    # Read the next frame
    ret, frame = cap.read()

    if ret:
        # Display the frame
        cv2.imshow('Reversed Video', frame)

        # Decrease the frame index for the next frame
        frame_index -= 1

        # Check if we are at the beginning of the video
        if frame_index < 0:
            break

        # Wait for the specified amount of time between frames
        # Here, 30ms delay between each frame (i.e., 1000ms / 30fps)
        # Adjust this delay according to the actual video fps
        cv2.waitKey(int(1000 / fps))
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
