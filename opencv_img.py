#importing modules -- this are all we need for most of the time
import matplotlib.pyplot as plt
import cv2


#LOAD IMAGE, first arg is path/to/image add grayscale filter = 0
#Various filters are there
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
img = cv2.imread('C:\\Users\\Rifat\\Desktop\\IMG_20170906_172014_2.jpg', cv2.IMREAD_GRAYSCALE)

#show the image, first arg = 'name_of_image', second 'imread' object
cv2.imshow('HELLO!', img)

#wait for any key to press to... for 0, it shows infinitely
cv2.waitKey(0)
#distroy the window
cv2.destroyAllWindows()
#to save the file - optional
# cv2.imwrite('kaggle_grayed.jpg', img)

#for showing through matplotlib
# plt.imshow(img, cmap = 'gray', interpolation='bicubic')
# plt.show()
