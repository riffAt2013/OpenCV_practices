import cv2
import numpy as np


#load img
img1 = cv2.imread('src/pic1.jpg')
fey = cv2.imread('src/fey.jpg')

#adding image ;), both with their original opacity
add = img1+ img2

#cv2 addition, this adds per pixel color values, and adds it to get the
#new color value for same pixel position
#(1,1,1) + (200,40,255) = (201,41,255)
add = cv2.add(img1, img2)

#for weighted adding, here img1 should have 90% opacity
#5th param is gamma value
weighted = cv2.addWeighted(img1, 0.9, img2, 0.1, 1)


#For COPYPASTA entire image 
rows,cols,channels = fey.shape
roi = fey[0:rows, 0:cols]
img1[0:rows, 0:cols] = roi 



#For just adding the foreground of the image
rows,cols,channels = fey.shape
roi = img1[0:rows, 0:cols]

feygray = cv2.cvtColor(fey, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(feygray, 220, 255,cv2.THRESH_BINARY_INV)

mask_inverse = cv2.bitwise_not(mask)

background = cv2.bitwise_and(roi, roi, mask = mask_inverse)
foreground = cv2.bitwise_and(fey, fey, mask = mask)

res = cv2.add(background,foreground)

img1[0:rows, 0:cols] = res




cv2.imshow('winname', img1)
cv2.waitKey(0)
# cv2.imshow('winname', weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()