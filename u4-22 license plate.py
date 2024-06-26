import cv2

# Load the pre-trained Haar cascade classifier for license plates
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

img = cv2.imread(r"C:\Users\Harsha\OneDrive\Documents\opencv_img\pedestrian1.jpeg")

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to open image file {r'C:\Users\Harsha\OneDrive\Documents\opencv_img\pedestrian1.jpeg'}")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect license plates in the image
plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around detected license plates
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

# Display the image with rectangles around license plates
cv2.imshow('License Plate Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
