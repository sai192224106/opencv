import cv2

def detect_faces_and_eyes(image_path):
    # Load the pre-trained Haar cascades for face and eye detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Extract the region of interest (ROI) for the detected face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Draw rectangles around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    # Display the output image
    cv2.imshow('Image with Face and Eye Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the path to the image
image_path =r"C:\Users\Harsha\OneDrive\Documents\opencv_img\face.jpeg"
detect_faces_and_eyes(image_path)
