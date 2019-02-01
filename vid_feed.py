#load modules as usual
import cv2

#load the video feed. arg takes 'n'
#for n'th webcam
#also pre-made video can be included thru path/to/vid

cap = cv2.VideoCapture('C:/Users/Rifat/Desktop/OpenCV tests/aab.mp4')

#to show the output create a codec file first
#use the codec to create a outfile object to be captured
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outfile = cv2.VideoWriter('C:/Users/Rifat/Desktop/OpenCV tests/malc.avi', fourcc, 30.0, (640,312))

#infinite loop to capture all the frame
while True:
	ret, frame = cap.read()

	if ret == True:
		# gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)	#I MAAAADE ITTTTT!!! The frame has to be BGR, regular shizz are RGB
		outfile.write(frame)
		# cv2.imshow('gray', gray)
		if cv2.waitKey(30) & 0xFF == ord('q'):	#'q' pressed, done!, interesting, waitKey seems to change fps while loading pre-made videos
			break
	else:
		break

cap.release()
outfile.release()
cv2.destroyAllWindows()

