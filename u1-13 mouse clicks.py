import cv2

# Function to display coordinates on click
def click_event(event, x, y, flags, param):
    # Check for left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked coordinates: ({x}, {y})")
        # Display the coordinates on the image
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"({x}, {y})", (x, y), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

# Read an image from file
img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

# Create a window and set the mouse callback function
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

# Wait until a key is pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
