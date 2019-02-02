#load the modules
import cv2
import matplotlib.pyplot as plt
import numpy as np


#load the image as usual, here we're using colored sample
img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

#draw a white line
#first param - image object
#second & third - starting and ending of the line
#fourth - color of the line: in B G R! eg: white is all in 255
#fifth is thickness in pixel
cv2.line(img, (100,100), (300,100), (0,0,255), 4)


#draw a rectangle: using rectangle module
#specific param list:
#2nd and 3rd - top left and bottom right point value as tuples
#same for color in B G R
#end with rectangle pixel width
#if the thickness is negative then its going to fill in the area
cv2.rectangle(img, (154, 216), (606,631), (100,0,0), 2)


#draw a circle: follow the shitty pattern
#2nd and 3rd param being centre of the circle and the radius
cv2.circle(img, (850,200), 100, (0,250,0), 1)


#draw a polygon!
#we need points here, throw them as a numpy array
#also pts is expected as a list, further discussion: https://stackoverflow.com/questions/17241830/opencv-polylines-function-in-python-throws-exception
#isClosed = True for first and last point to be Connected or not
pts = np.array([[910, 641], [206, 632], [696, 488], [458, 485]], np.int32)
# pts = pts.reshape(-1,1,2)
cv2.polylines(img, [pts] , True, (0,255,255),1)



#writing in an image
#define a font first, well you can directly pass it as always
#5th param is font scaling, which lets you scale the font, not really set the size instead
font = cv2.FONT_ITALIC
cv2.putText(img, 'HELLO WORLD MOTHERFUHERS', (238,178), font, 1, (0,0,0), 2)


#show the image, use the basic routine
cv2.imshow('rifat', img)
cv2.waitKey(0)	#param, is delay in ms
cv2.destroyWindow('rifat')

#again we can use plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()