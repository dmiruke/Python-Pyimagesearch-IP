# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:29:01 2017

@author: Jose Odell Dixon
"""

import numpy as np 
import cv2
cap = cv2.VideoCapture()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #Our operations on the frane cone here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & O&FF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()