import cv2

def crop_copy_paste_roi(image_path, roi_coords, paste_coords, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f'Error: Unable to load image at {image_path}')
        return
    
    # Get the dimensions of the image
    img_height, img_width, _ = image.shape
    
    # Define the coordinates of the ROI (x, y, width, height)
    x, y, w, h = roi_coords
    
    # Ensure the ROI coordinates are within the image bounds
    if x < 0 or y < 0 or x+w > img_width or y+h > img_height:
        print('Error: ROI coordinates are out of image bounds')
        return
    
    # Crop the ROI from the image
    roi = image[y:y+h, x:x+w]
    
    # Define the top-left corner where the ROI will be pasted
    paste_x, paste_y = paste_coords
    
    # Ensure the paste coordinates are within the image bounds
    if paste_x < 0 or paste_y < 0 or paste_x+w > img_width or paste_y+h > img_height:
        print('Error: Paste coordinates are out of image bounds')
        return
    
    # Paste the ROI onto the image at the specified location
    image[paste_y:paste_y+h, paste_x:paste_x+w] = roi
    
    cv2.imshow("watermarked image ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
crop_copy_paste_roi(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg', (50, 50, 100, 100), (50, 50), 'output.jpg')
