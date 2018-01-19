# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:09:05 2017

@author: Jose Odell Dixon
"""

import numpy as np
import cv2

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted