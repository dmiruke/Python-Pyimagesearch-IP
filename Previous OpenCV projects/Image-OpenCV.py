# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:09:41 2017
# Successful
@author: Rukayat Ariori
"""

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1 

cv2.imshow('TheTreeImage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
