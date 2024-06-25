import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'C:\Users\Harsha\OneDrive\Documents\opencv_img\beach.jpeg')

channels = cv2.split(image)
colors = ('b', 'g', 'r')
channel_names = ('Blue', 'Green', 'Red')


plt.figure(figsize=(10, 5))
plt.title('Color Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')

    
    # Plot the histogram for each color channel
for channel, color, channel_name in zip(channels, colors, channel_names):
    histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(histogram, color=color, label=f'{channel_name} channel')
    
plt.legend()
plt.xlim([0, 256])
plt.show()


