# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:55:01 2024

@author: gaosh
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift,ifft2,ifftshift

im_GS_amplitude=plt.imread("C:/Users/gaosh/Image_augment/flowers_s.png")
im_GS=plt.imread("C:/Users/gaosh/Image_augment/flowers_s_10_wh_p(1, 'nL')_p2_4_check_I3.png")
im_MP=plt.imread("C:/Users/gaosh/Image_augment/flower_Scurve_10_wh_p(1, 'nL')_p2_4_check_I3.png")
im_WH_amplitude=plt.imread("C:/Users/gaosh/Image_augment/flower_Scurve.png")
im_GS_R=im_GS[:,:,0]*255
im_MP_R=im_MP[:,:,0]*255

im_GS_R_angle=(im_GS_R/255)*1.8*np.pi
im_MP_R_angle=(im_MP_R/255)*1.8*np.pi

center_h=1920//2
y_offset=center_h-1080//2
current_field_GS = ifft2(ifftshift(im_GS_amplitude[:,:,0][y_offset:y_offset+1080,:]*np.exp(1j * im_GS_R_angle)))
current_field_MP = ifft2(ifftshift(im_WH_amplitude[:,:,0][y_offset:y_offset+1080,:]*np.exp(1j * im_MP_R_angle)))

plt.figure()
# Reconstructed amplitude
plt.title("Original")
plt.imshow(np.abs(ifftshift(current_field_GS))*255, cmap="Reds")
plt.colorbar()
plt.show()

plt.figure()
# Reconstruction error
# error = np.abs(np.abs(im_shift) - final_field)
plt.title("WH_augment")
plt.imshow(np.abs(ifftshift(current_field_MP))*255, cmap="Reds")
plt.colorbar()
plt.show()