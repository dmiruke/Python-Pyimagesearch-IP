# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:15:42 2017

@author: Rukayat Ariori
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()