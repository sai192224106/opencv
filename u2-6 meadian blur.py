import cv2
import numpy as np

# Define the dataset
data = np.array([3, 5, 8, 12, 7, 10, 15, 20, 18, 22, 25, 28, 30], dtype=np.float32)

# Apply Median Filtering
# OpenCV expects a 2D array for filtering, so we reshape the data to a 2D array
data_reshaped = data.reshape(1, -1)
median_filtered = cv2.medianBlur(data_reshaped, ksize=3)
print(median_filtered)
median_filtered = median_filtered.reshape(-1)

# Apply Box Filtering (Moving Average Filter)
# Using a 3-element kernel for a simple moving average
box_filtered = cv2.blur(data_reshaped, ksize=(1, 3))
box_filtered = box_filtered.reshape(-1)

# Print the results
print("Original data:         ", data)
print("Median filtered data:  ", median_filtered)
print("Box filtered data:     ", box_filtered)
