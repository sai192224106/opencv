import cv2

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the input image
image_path = r"C:\Users\Harsha\OneDrive\Documents\opencv_img\smilegroup.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces and count them
    number_of_faces = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        number_of_faces += 1

    # Display the count of faces
    print(f"Number of faces detected: {number_of_faces}")

    # Display the output image with rectangles around faces
    cv2.imshow('Image with Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
