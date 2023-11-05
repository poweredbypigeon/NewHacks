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
import matplotlib.pyplot as plt
from eyetracker.eyetracker import determine_focus_status
from cnn_running import fatigue_pred

tired_threshold = 0.05
focus_threshold = 0.05

user_data = []
frame_number = 1
cur_tired = ""
text_font = cv2.FONT_HERSHEY_SIMPLEX

def check_tiredness(user_data):
    if len(user_data) > 70:
        if [cur_state[1] for cur_state in user_data[-51:-1]].count(True)/50 >= tired_threshold:
            return True
    return False

def check_unfocusness(user_data):
    if len(user_data) > 70:
        if [cur_state[2] for cur_state in user_data[-51:-1]].count(True)/50 >= tired_threshold:
            return True
    return False

cascade_classifier = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
vid = cv2.VideoCapture(0)
# Read the first frame of the video file use "_," to ignore variable type, ignores the tuple

while True:
    ret, frame = vid.read()
    frame = imutils.resize(frame,width = 1080) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cascade_classifier.detectMultiScale(gray, 1.3, 5)
    cur_state = []
    time = round(frame_number/30, 2)
    cur_state.append(time)

    if len(res) > 0:
        (x,y,w,h) = res[0]
        w,h = max(w,h),max(w,h)
        # frame[y:y+h, x:x+w]
        if fatigue_pred(gray[y:y+h, x:x+w]) == True:
            cur_tired = "Fatigue"
            cur_state.append(True)
        else: 
            cur_tired = "Active"
            cur_state.append(False)
        if determine_focus_status(frame) == True:
             cur_focus = "Focused"
             cur_state.append(True)
        else:
             cur_focus = "Not Focused"
             cur_state.append(False)
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0 ,255), 3)
    else:
         cur_state.append(False)
         cur_state.append(False)

    user_data.append(cur_state)
    if(check_tiredness(user_data) == True):
        print("YOU ARE TIRED")
    if(check_unfocusness(user_data) == True):
        print("STAY ON TASK")
    
    cv2.putText(frame, "Time Elapsed: " + str(time), (50, 50), text_font, 0.8, (255, 0, 0), 1, cv2.LINE_4)
    cv2.putText(frame, "Current State: " + cur_tired + " and " + cur_focus, (500, 50), text_font, 0.8, (255, 0, 0), 1, cv2.LINE_4)

    cv2.imshow('Output', frame)

    # Always checking for 'q' key every frame in the while loop to exit whenever

    key  =  cv2.waitKey(1) & 0xff  

    if key == ord('q'):
        frame_number = 1
        break
    frame_number += 1
# vid.release()
# cv2.destroyAllWindows()


# def final_report():
#     plt.figure(figsize=(10, 5))

#     # Plot Focus
#     plt.subplot(1, 2, 1)
#     plt.plot(time_points, focus_data, marker='o', linestyle='-', color='b')
#     plt.title('Focus Over Time')
#     plt.xlabel('Time')
#     plt.ylabel('Focus Level')

#     # Plot Tiredness
#     plt.subplot(1, 2, 2)
#     plt.plot(time_points, tiredness_data, marker='o', linestyle='-', color='r')
#     plt.title('Tiredness Over Time')
#     plt.xlabel('Time')
#     plt.ylabel('Tiredness Level')
# 	pass


