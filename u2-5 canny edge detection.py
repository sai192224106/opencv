import cv2

img=cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\bird.jpeg',cv2.IMREAD_GRAYSCALE)

blur_img=cv2.GaussianBlur(img,(5,5),1.4)
t_lower = 50  # Lower Threshold 
t_upper = 150  # Upper threshold 
edge=cv2.Canny(blur_img,t_lower,t_upper)

cv2.imshow("original ",img)
cv2.imshow("canny edge ",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()