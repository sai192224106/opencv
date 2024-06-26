import cv2

def add_text_to_image(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 0, 0), thickness=2):
    """
    Adds text to an image.

    :param image: The input image.
    :param text: The text string to add.
    :param position: A tuple (x, y) representing the bottom-left corner of the text.
    :param font: The font type.
    :param font_scale: The scale factor that is multiplied by the font-specific base size.
    :param color: The color of the text in BGR format.
    :param thickness: The thickness of the lines used to draw the text.
    :return: The image with the text added.
    """
    cv2.putText(image, text, position, font, font_scale, color, thickness)
    return image

# Load the input image
image_path = r"C:\Users\Harsha\OneDrive\Documents\opencv_img\smilegroup.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Get user input for the text string and position
    text = input("Enter the text to add to the image: ")
    x = int(input("Enter the x position for the text: "))
    y = int(input("Enter the y position for the text: "))

    # Add the text to the image
    image_with_text = add_text_to_image(image, text, (x, y))

    # Display the output image
    cv2.imshow('Image with Text', image_with_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
