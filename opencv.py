# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:49:08 2024

@author: gaosh
"""

import cv2

im=cv2.imread("flowers_s.png")
gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
enhanced=cv2.equalizeHist(gray)

# cv2.imshow("Original",im[:,:,0])
cv2.imshow("Enhanced",enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()