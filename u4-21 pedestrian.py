import cv2
import numpy as np

# Load the pre-trained HOG descriptor and SVM detector for pedestrian detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load the input image
image_path = r"C:\Users\Harsha\OneDrive\Documents\opencv_img\pedestrian1.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Perform pedestrian detection
    (pedestrians, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw rectangles around detected pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output image with detected pedestrians
    cv2.imshow('Pedestrian Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
