import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

#To see color value in a Pixel, in B G R
pixel = img[99,66]

#Assigning color values to a pixel
img[99, 66] = [255,255,255]
print(pixel)

#Selecting Region of an Image and showing color values of it
roi = img[55:99, 55:99]
print(roi)

#Assigning Specific color all accross a region of an image
img[55:99, 55:99] = [255,255,255]


#COPYPASTA of color values of an ROI to another ROI, pixel H and W has to be the same
roi2 = img[231:260, 209:244]
img[0:29, 0:35] = roi2

cv2.imshow('output',img)
cv2.waitKey(0)

