import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\nature1.jpeg')
# Loading the image



# Resize to smaller dimensions (half the size)
smaller_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

# Resize to larger dimensions (double the size)
larger_img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))

# Display the original, smaller, and larger images
cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image", smaller_img)
cv2.imshow("Larger Image", larger_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()








#bigger=cv2.resize(img,(1050,1610))
#bigger=cv2.cvtColor(bigger,cv2.COLOR_BGR2RGB)

#smaller=cv2.resize(img,(900,350))
#smaller=cv2.cvtColor(smaller,cv2.COLOR_BGR2RGB)


#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Titles =["Original", "Bigger", "smaller"]
#images =[img, bigger, smaller]
#count = 3

#for i in range(count):
#	plt.subplot(1, 3, i + 1)
#	plt.title(Titles[i])
#	plt.imshow(images[i])
	
#plt.tight_layout()
#plt.show()
