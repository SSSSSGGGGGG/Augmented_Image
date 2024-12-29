# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:24:55 2024

@author: gaosh
"""

from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt

# Open the image using PIL
im = Image.open('flowers_s.png')

# Convert the PIL image to a NumPy array (this automatically converts to uint8)
im_np = np.array(im)

# Perform the squaring operation
im_S = (im_np ** 2).astype("uint8")
output_filename = 'flowers_s_squared.png'
plt.imsave(output_filename, im_S)
# Display the transformed image using matplotlib
plt.figure()
plt.imshow(im_S)
plt.title('Squared and Modulated Image')
plt.axis('off')
plt.show()

# 3. Contrast Enhancement
contrast = ImageEnhance.Contrast(im)
enhanced = contrast.enhance(2.0)  # Increase contrast by 2.0
im.show()  # Show the original image
enhanced.show()  # Show the enhanced image

# 4. Brightness Enhancement
enhancer = ImageEnhance.Brightness(im)
brightened_image = enhancer.enhance(1.5)  # Increase brightness by 1.5x
brightened_image.show()  # Show the brightened image
