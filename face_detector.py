# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:16:46 2017

@author: Rukayat Ariori I
"""

# import the necessary packages
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-fc", "--fcascade",
	default="haarcascade_frontalface_default.xml",
	help="path to face detector haar cascade")
ap.add_argument("-ec", "--ecascade", 
   default="haarcascade_eye.xml")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the cat detector Haar cascade, then detect cat faces
# in the input image
face_cascade = cv2.CascadeClassifier(args["fcascade"])
eye_cascade = cv2.CascadeClassifier(args["ecascade"])



# loop over the cat faces and draw a rectangle surrounding each
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('Faces',image)
cv2.waitKey(0)

# show the detected cat faces