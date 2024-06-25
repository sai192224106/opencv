import cv2
import numpy as np

def modify_roi(image_path, top_left, bottom_right, color):

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image at path {image_path} could not be found.")

    # Define the ROI
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Check for valid ROI coordinates
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]:
        raise ValueError("ROI coordinates are out of image bounds")

    # Modify the ROI
    image[y1:y2, x1:x2] = color

    return image

# Example usage
top_left_corner = (50, 50)
bottom_right_corner = (200, 150)
fill_color = (0, 255, 0)  # Green color

modified_img = modify_roi(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg', top_left_corner, bottom_right_corner, fill_color)
cv2.imshow('smoothed img', modified_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    Modify a specific region of interest (ROI) in an image.

    :param image_path: Path to the input image.
    :param top_left: Tuple of (x, y) coordinates for the top-left corner of the ROI.
    :param bottom_right: Tuple of (x, y) coordinates for the bottom-right corner of the ROI.
    :param color: Tuple of (B, G, R) values to fill the ROI with.
    :return: Modified image.
    """