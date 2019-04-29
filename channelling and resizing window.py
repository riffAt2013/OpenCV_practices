import cv2 as cv


def singleChanneling(imgMatrix,channelName):
	# "blue" = 0
	# "green" = 1
	# "red" = 2
	if channelName.lower() == "blue":
		imgMatrix = imgMatrix[:,:,0]
		return imgMatrix
	elif channelName.lower() == "green":
		imgMatrix = imgMatrix[:,:,1]
		return imgMatrix
	elif channelName.lower() == "red":
		imgMatrix = imgMatrix[:,:,2]
		return imgMatrix
	else:
		print("Wrong Channel input")

def windowResizedOutput(winname,h,w, waitKey, imageMatrix):
	cv.namedWindow(winname, cv.WINDOW_NORMAL)
	cv.resizeWindow(winname, h,w)
	cv.imshow(winname, imageMatrix)
	cv.waitKey(waitKey)	
		

image = cv.imread('pic/DSC_0103.jpg')

image = singleChanneling(image, "red")

windowResizedOutput('sexy', 1200, 800, 0, image)


