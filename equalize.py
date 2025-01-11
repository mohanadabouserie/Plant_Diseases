import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "image.png"  # Replace with your image file
image = cv2.imread(image_path)

# Convert the image to RGB (from BGR as OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into individual channels (R, G, B)
r, g, b = cv2.split(image)

# Apply histogram equalization to each channel
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)

# Merge the equalized channels back into a single image
equalized_image = cv2.merge((r_eq, g_eq, b_eq))

# Convert the equalized image back to RGB for display
equalized_image_rgb = cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB)

# Display the original and equalized images side by side for comparison
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

# Equalized Image
plt.subplot(1, 2, 2)
plt.imshow(equalized_image_rgb)
plt.title("Equalized Image")
plt.axis("off")

plt.show()
