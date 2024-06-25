# import OpenCV 
import cv2 
  
# import Numpy 
import numpy as np 
  
# read an image using imread 
img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\nature1.jpeg') 
  
# convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# creating a Histograms Equalization 
# of the grayscale image using cv2.equalizeHist() 
equ = cv2.equalizeHist(gray_img)

# convert the equalized image back to BGR
equ_color = cv2.cvtColor(equ, cv2.COLOR_GRAY2BGR)

# stacking images side-by-side 
res = np.hstack((img, equ_color)) 
  
# show image input vs output 
cv2.imshow('image', res) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows()
