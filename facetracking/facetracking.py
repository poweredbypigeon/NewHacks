import cv2, imutils
import numpy as np
import pandas as pd
import os

class FaceTracking:
	frame_number = 1
	fps = 30
	text_font = cv2.FONT_HERSHEY_SIMPLEX

	cascade_classifier = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
	vid = cv2.VideoCapture(0)
	# Read the first frame of the video file use "_," to ignore variable type, ignores the tuple

	while True:
		ret, frame = vid.read()
		frame = imutils.resize(frame,width = 1080) 
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		res = cascade_classifier.detectMultiScale(gray, 1.3, 5)

		if(len(res) > 0):
			(x,y,w,h) = res[0]
			adj = max(w,h)
			if w < h:
				w = h
			else:
				h = w
			frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0 ,255), 3)

		# Display frame count
		time = round(frame_number/30, 2)
		cv2.putText(frame, "Time Elapsed: " + str(time), (50, 50), text_font, 0.8, (0, 255, 255), 1, cv2.LINE_4)
		print(frame_number)

		cv2.imshow('Output', frame)

		# Always checking for 'q' key every frame in the while loop to exit whenever

		key  =  cv2.waitKey(1) & 0xff  

		if key == ord('q'):
			frame_number = 1
			break
		frame_number += 1
	# vid.release()
	# cv2.destroyAllWindows()
