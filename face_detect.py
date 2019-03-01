#loading modules as usual -_-
import cv2

#to detect face, first load a classifier 
cascade = cv2.CascadeClassifier('classifiers\\haarcascade_frontalface_default.xml')

#then load an image, of which faces exist
image = cv2.imread('src\\IMG_20190222_170132.jpg')

#grayscale it. detection works better when its g-scale, since the image is sharp
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detectMultiscale returns rectangle vectors for matched objects
faces = cascade.detectMultiScale(gray, 1.3, 5)


#using the retval from faces, draw a rectangle, refer image_draw.py for understanding that
for (x,y,w,h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)


#since my image res is huge, I needed to change the window by modifying WINDOW_NORMAL flag
#and then resizing the window, this just scales the size
cv2.namedWindow('winname', cv2.WINDOW_NORMAL)
cv2.resizeWindow('winname', 1136,640)

#basic imshow :P and further workings
cv2.imshow('winname', image)

cv2.waitKey(0)
cv2.destroyAllWindows()