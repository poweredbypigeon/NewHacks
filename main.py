'''
Monitor the user and return a square of their face
-> Feed the face into the neural net prediction to get a result
-> Store the result as a function of time
-> Set parameters for fatigue and focusness.
-> At the end of the session, provide a full report of the users activity
'''

import cv2, imutils
import numpy as np
import pandas as pd
import os
from cnn_running import fatigue_pred

user_data = []
frame_number = 1
cur_state = ""
text_font = cv2.FONT_HERSHEY_SIMPLEX

cascade_classifier = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
vid = cv2.VideoCapture(0)
# Read the first frame of the video file use "_," to ignore variable type, ignores the tuple

while True:
    ret, frame = vid.read()
    frame = imutils.resize(frame,width = 1080) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cascade_classifier.detectMultiScale(gray, 1.3, 5)

    if len(res) > 0:
        (x,y,w,h) = res[0]
        w,h = max(w,h),max(w,h)
        print(frame)
        if fatigue_pred(frame[x,y,w,h]) == True:
            cur_state = "Fatigue"
        else: 
            cur_state = "Active"
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0 ,255), 3)

    cv2.putText(frame, "Frame Count: " + str(frame_number), (50, 50), text_font, 0.8, (0, 255, 255), 1, cv2.LINE_4)
    cv2.putText(frame, "Current State: " + cur_state, (500, 50), text_font, 0.8, (0, 255, 255), 1, cv2.LINE_4)
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

def check_tireness():
    pass

def check_focusness():
	pass

def final_report():
	pass


