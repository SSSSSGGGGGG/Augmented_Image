# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 15:16:04 2024

@author: gaosh
"""

# import torch
# from torchvision import transforms
# from PIL import Image
# import matplotlib.pyplot as plt

# # # Load the image
# # image = Image.open('flowers_s.png')

# # # Define a transform pipeline
# # transform = transforms.Compose([
# #     transforms.RandomHorizontalFlip(),
# #     transforms.RandomRotation(30),
# #     transforms.ColorJitter(brightness=0.5, contrast=0.5),
# #     transforms.ToTensor()  # Convert to tensor for PyTorch
# # ])

# # # Apply the transformations
# # augmented_image = transform(image)

# # # Display the image
# # plt.imshow(augmented_image.permute(1, 2, 0))  # Convert from (C, H, W) to (H, W, C)
# # plt.show()

# import cv2
# import albumentations as A
# from matplotlib import pyplot as plt
# import numpy as np

# # Load an image using OpenCV
# im=np.mod(plt.imread('flowers_s.png'),255)
# im_S=np.mod(im**2,255)
# image = cv2.imread('flowers_s.png')
# plt.figure()
# plt.imshow(im)
# plt.show()
# plt.figure()
# plt.imshow(im_S)
# plt.show()
# # Define an augmentation pipeline
# transform = A.Compose([
#     # A.RandomCrop(width=300, height=300),
#     # A.HorizontalFlip(p=0.5),
#     # A.Rotate(limit=45, p=0.7),
#     A.RandomBrightnessContrast(p=0.2)
# ])

# # Apply the transformations
# augmented = transform(image=image)
# augmented_image = augmented['image']

# # Display the augmented image
# plt.figure()
# plt.imshow(cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read the image using OpenCV (default is BGR)
image = plt.imread('flowers_s.png')

im_S = image**2
im_S_max=np.max(im_S)
im_S_min=np.min(im_S)
output_filename = 'flowers_s_squared.png'
plt.imsave(output_filename, im_S)

im_S_bright=im_S+0.2
im_S2_max=np.max(im_S_bright)
im_S2_min=np.min(im_S_bright)

# Display the original image
plt.figure()
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Display the transformed image (mod 255 and squaring)
plt.figure()
plt.imshow(im_S)  # .astype(np.uint8)Convert to uint8 to display correctly
plt.title('Transformed Image')
plt.axis('off')
plt.show()

plt.figure()
plt.imshow(im_S_bright)  # .astype(np.uint8)Convert to uint8 to display correctly
plt.title('Brighten Image')
plt.axis('off')
plt.show()