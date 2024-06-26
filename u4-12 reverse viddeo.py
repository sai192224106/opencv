import cv2

# Path to the input video file
video_path =r"C:\Users\Harsha\OneDrive\Documents\opencv_img\video."

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# List to store all frames of the video
frames = []

# Read the video frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

# Release the video capture object
cap.release()

# Reverse the list of frames
frames.reverse()

# Create a named window for displaying the video
cv2.namedWindow('Reversed Video', cv2.WINDOW_NORMAL)

# Display the frames in reverse order
for frame in frames:
    cv2.imshow('Reversed Video', frame)
    
    # Wait for 25 milliseconds before moving to the next frame
    # Adjust the delay as needed to match the original frame rate
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Destroy all the windows
cv2.destroyAllWindows()
