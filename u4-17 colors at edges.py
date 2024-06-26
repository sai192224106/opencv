import cv2
import numpy as np

def create_image_with_colored_boxes(width, height, box_size):
    # Create a white image
    image = np.ones((height, width, 3), np.uint8) * 255

    # Define colors in BGR format
    black = (0, 0, 0)
    blue = (255, 0, 0)
    green = (0, 255, 0)
    red = (0, 0, 255)

    # Top-left corner (black)
    cv2.rectangle(image, (0, 0), (box_size, box_size), black, -1)
    
    # Top-right corner (blue)
    cv2.rectangle(image, (width - box_size, 0), (width, box_size), blue, -1)
    
    # Bottom-left corner (green)
    cv2.rectangle(image, (0, height - box_size), (box_size, height), green, -1)
    
    # Bottom-right corner (red)
    cv2.rectangle(image, (width - box_size, height - box_size), (width, height), red, -1)

    return image

# Get user input for image size and box size
width = int(input("Enter the width of the image: "))
height = int(input("Enter the height of the image: "))
box_size = int(input("Enter the size of the boxes: "))

# Create the image and add colored boxes
image = create_image_with_colored_boxes(width, height, box_size)

# Display the output image
cv2.imshow('Image with Colored Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
