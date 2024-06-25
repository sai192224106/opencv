import cv2
import numpy as np

def add_text_watermark(image_path, text, position=(30, 30), font=cv2.FONT_HERSHEY_SIMPLEX, 
                       font_scale=1, color=(255, 255, 255), thickness=2, alpha=0.5):
    # Load the image
    image = cv2.imread(image_path)
    
    # Create a copy of the image to overlay the text on
    overlay = image.copy()
    
    # Add the text to the overlay image
    cv2.putText(overlay, text, position, font, font_scale, color, thickness)
    
    # Blend the overlay image with the original image
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
    
    # Save the output image
    cv2.imshow("watermarked image ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
add_text_watermark(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg', 'Watermark 1234')
