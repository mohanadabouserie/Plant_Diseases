import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "img2.jpg"  # Replace with your image file
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Define the brownish color range in HSV
lower_brown = np.array([10, 50, 50])  # Lower bound of brown
upper_brown = np.array([30, 255, 200])  # Upper bound of brown

# Create a mask for brownish areas
brown_mask = cv2.inRange(hsv_image, lower_brown, upper_brown)

# Perform morphological operations to clean up the mask
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_CLOSE, kernel)

# Highlight the brown areas in the original image
brown_highlighted = cv2.bitwise_and(image, image, mask=brown_mask)

# Detect edges in the original image using the Canny Edge Detector
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray_image, 254, 255)

# Overlay edges on the brown-highlighted image
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)  # Convert edges to RGB
combined_result = cv2.addWeighted(brown_highlighted, 0.7, edges_colored, 0.3, 0)

# Display the results
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(brown_highlighted)
plt.title("Brownish Areas Highlighted")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap="gray")
plt.title("Detected Edges")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(combined_result)
plt.title("Brown Areas with Edges Overlay")
plt.axis("off")

plt.show()
