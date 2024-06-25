import cv2
import matplotlib.pyplot as plt

image_path = r'C:\Users\Harsha\OneDrive\Documents\opencv_img\nature1.jpeg'
img=cv2.imread(image_path)

if img is None:
    print("unable to load image")
else:
    grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imshow("original",img)
    cv2.imshow("grey image",grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
