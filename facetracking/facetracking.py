import cv2, imutils
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Tracking:

	# Create an instance of the opencv TrackerCSRT Reference Class

	tracker = cv2.legacy.TrackerKCF_create()
	camera = True # False for vid, True for Webcam
	frame_number = 1
	text_font = cv2.FONT_HERSHEY_SIMPLEX

	# Initial Conditions + System Properties

	frame_per_second = 120
	frame_dt = 1 / frame_per_second

	if camera: 
		vid  = cv2.VideoCapture(0)

	# Read the first frame of the video file use "_," to ignore variable type, ignores the tuple

	_,frame = vid.read()
	frame = imutils.resize(frame,width = 1080)

	OBJ = cv2.selectROI(frame, False)
	tracker.init(frame, OBJ)

	while True:
		_,frame = vid.read()
		frame = imutils.resize(frame,width = 1080) 

		track_success, OBJ = tracker.update(frame)

		# Draw a rectangle for success

		if track_success:
			top_left = (int(OBJ[0]),int(OBJ[1]))
			bottom_right = (int(OBJ[0] + OBJ[2]), int(OBJ[1] + OBJ[3]))
			cv2.rectangle(frame,top_left,bottom_right,(0,0,255),5)

		# Display frame count

		cv2.putText(frame, "Frame Count: " + str(frame_number), (50, 50), text_font, 1, (0, 255, 255), 2, cv2.LINE_4)
		print(frame_number)

		cv2.imshow('Output', frame)

		# Always checking for 'q' key every frame in the while loop to exit whenever

		key  =  cv2.waitKey(1) & 0xff  

		if key == ord('q'):
			frame_number = 1
			break

	vid.release()
	cv2.destroyAllWindows()
