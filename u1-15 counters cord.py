import cv2

def find_contours_coordinates(image_path):
    # Read the image from the file
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to get a binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for i, contour in enumerate(contours):
        print(f"Contour {i} has {len(contour)} points")

        # Draw the contour and its coordinates on the image
        for point in contour:
            x, y = point[0]
            print(f"Contour {i} point: ({x}, {y})")
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
    
    # Display the image with contours
    cv2.imshow('Contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg'
find_contours_coordinates(image_path)
