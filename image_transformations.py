import numpy as np
import cv2

image = cv2.imread(r'C:\Users\rifat\Desktop\OpenCV_practices\src\fey.jpg')

"""
translation mainly works via warpAffine method, it needs a translation matrix as an arg
that is of [1, 0, tx]* [0,,1, ty] format, where as tx and ty is the actual value in pixels
that we will move the image from the og position, e.g: tx=25, ty=25 means all the pixels are
shifted below 25 px and to the right 25px
"""
def translation (image, x, y):
	h,w = image.shape[:2]
	trans_matrix = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
	shifted = cv2.warpAffine(image, trans_matrix, (w,h))
	return shifted

"""
rotation also needs warpAffine method, it seems that it needs the modified matrix to work with the og
to create something. we give them rotation_matrix this time via getRotationMatrix2D which just takes an
amount of degree to be rotated(positive is counterclockwise) and a scale amount
"""
def rotation (image, degreeAmount):
	h,w = image.shape[:2]
	center = (w/2, h/2)
	rotation_matrix = cv2.getRotationMatrix2D(center, degreeAmount, scale=1.0)
	rotated_img = cv2.warpAffine(image, rotation_matrix, (w,h))
	return rotated_img

"""
resize works via resize method which needs src, the dimension of the new image and
and an interpolation method, this is just an algorithm of how the image is resized
under the hood. the imp part here is the dim kwarg which needs to be calculated.
for that we need the correct aspect ratio so that the image is perfectly scaled.
we do that via taking either one of the provided height or width
"""

def resize (image, width=None, height=None, inter=cv2.INTER_AREA):
	h,w = image.shape[:2]
	if width==None and height==None:
		return image

	if width == None:
		asp_r = height/float(h)
		dim = (int(w*asp_r), height)
	else:
		asp_r = width/float(w)
		dim = (width, int(h*asp_r))
	return cv2.resize(image, dim, interpolation = inter)


"""
Flipping is implemented via flip method, here
direction = 1 -> horizontal flip
direction = 0 -> vertical flip
direction = -1 -> vertical && horizontal flip || Default val is 1 
"""
def flip (image, direction = 1):
	return cv2.flip(image, direction)


def crop (image, startX, startY, endX, endY):
	cropped = image[int(startY):int(endY), int(startX):int(endX)]
	return cropped

cv2.imshow('translated', translation(image, 25, -25))
cv2.imshow('rotated_img', rotation(image, 310))
cv2.imshow('winname', resize(image, height = 200))
cv2.imshow('1', flip(image))
cv2.imshow("winname", crop(image, 0, 0, 340, 240))
cv2.waitKey(0)