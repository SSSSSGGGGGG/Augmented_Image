# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:23:01 2024

@author: gaosh
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Open the image and normalize to [0, 1]
im = Image.open("flowers_s_squared.png").convert("RGB")
im_np = np.array(im) / 255.0  # Normalize image to range [0, 1]

# Define custom curve control points
x = [0.0, 0.2,0.3,0.4,0.5, 0.6,0.7,0.8, 1.0]  # Input intensities (original image)
y = [0.2, 0.25,0.3,0.3,0.5,0.65, 0.8, 0.9,1.0]  # Output intensities (desired mapping)

# Create the interpolation function (cubic for smooth transitions)
curve = interp1d(x, y, kind="cubic", fill_value="extrapolate")

# Generate curve values for visualization
x_vals = np.linspace(0, 1, 256)  # Range of intensity values
y_vals = np.clip(curve(x_vals), 0, 1)  # Ensure the output stays in [0, 1]

# Apply the curve to each channel
adjusted_np = np.zeros_like(im_np)
for channel in range(3):  # RGB channels
    adjusted_np[..., channel] = np.clip(curve(im_np[..., channel]), 0, 1)

# Plot the curve
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(x_vals, y_vals, label="Intensity Mapping Curve", color="blue")
plt.scatter(x, y, color="red", label="Control Points")
plt.title("Custom Intensity Curve")
plt.xlabel("Input Intensity")
plt.ylabel("Output Intensity")
plt.legend()
plt.grid(True)

# Display the original image
plt.subplot(2, 2, 2)
plt.title("Original Image")
plt.imshow(im_np)
plt.axis("off")

# Display the adjusted image
plt.subplot(2, 2, 3)
plt.title("Adjusted Image")
plt.imshow(adjusted_np)
plt.axis("off")
filename="flower_Scurve"
plt.imsave(f"{filename}.png",adjusted_np)

plt.tight_layout()
plt.show()
