# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:25:54 2017

@author: Rukayat Ariori
"""

from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
