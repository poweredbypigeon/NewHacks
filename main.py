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

tired_threshold = 0.25
focus_threshold = 0.25

user_data = []
frame_number = 1
cur_tired, cur_focus = "", ""
text_font = cv2.FONT_HERSHEY_SIMPLEX
time_data, tired_data, unfocus_data = [], [], []
globtired_data, globunfocus_data = [], []
popup_tired = False
popup_unfocus = False

def check_tiredness(tired_data):
    if len(tired_data) > 70:
        if tired_data[-51:-1].count(True)/50 >= tired_threshold:
            globtired_data.append(True)
            return True
    globtired_data.append(False)
    return False

def check_unfocusness(unfocus_data):
    if len(unfocus_data) > 70:
        if unfocus_data[-51:-1].count(True)/50 >= tired_threshold:
            globunfocus_data.append(True)
            return True
    globunfocus_data.append(False)
    return False

def plot_report(user_data):
    plt.rcParams["figure.figsize"] = [5, 7]
    plt.rcParams["figure.autolayout"] = True

    data = user_data
    user_data.append(globtired_data)
    user_data.append(globunfocus_data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(data, aspect='auto', cmap="Blues_r", interpolation='nearest')
    section_labels = ['Time (s)', 'Instant Tired', 'Instant Unfocused', 'Actual Tired', 'Actual Unfocused'] 
    ax.set_title("Productivity Report of Session")
    ax.set_yticks(range(len(section_labels)))
    ax.set_yticklabels(section_labels)
    # x_val = np.linspace(0, user_data[0][-1], 5)
    # ax.set_xticklabels(x_val)
    ax.set_xlabel('Frames Elapsed (n)')
    fig.savefig('prodreport.png')
    plt.show()

cascade_classifier = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
vid = cv2.VideoCapture(0)
# Read the first frame of the video file use "_," to ignore variable type, ignores the tuple

while True:
    ret, frame = vid.read()
    frame = imutils.resize(frame,width = 1080) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cascade_classifier.detectMultiScale(gray, 1.3, 5)
    time = round((4*frame_number)/30, 2)
    time_data.append(time)

    if len(res) > 0:
        (x,y,w,h) = res[0]
        w,h = max(w,h),max(w,h)
        # frame[y:y+h, x:x+w]
        if fatigue_pred(gray[y:y+h, x:x+w]) == True:
            cur_tired = "Fatigue"
            tired_data.append(True)
        else: 
            cur_tired = "Active"
            tired_data.append(False)
        if determine_focus_status(frame) == True:
             cur_focus = "Focused"
             unfocus_data.append(False)
        else:
             cur_focus = "Not Focused"
             unfocus_data.append(True)
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0 ,255), 3)
    else:
         tired_data.append(True)
         unfocus_data.append(True)

    if(check_tiredness(tired_data) == True):
        print("YOU ARE TIRED")
        popup_tired = True
    else:
        popup_tired = False
    if(check_unfocusness(unfocus_data) == True):
        print("STAY ON TASK")
        popup_unfocus = True
    else:
        popup_unfocus = False
    cv2.putText(frame, "Time Elapsed: " + str(time), (50, 50), text_font, 0.8, (255, 0, 0), 1, cv2.LINE_4)
    cv2.putText(frame, "Current State: " + cur_tired + " and " + cur_focus, (500, 50), text_font, 0.8, (255, 0, 0), 1, cv2.LINE_4)

    cv2.imshow('Output', frame)

    # Always checking for 'q' key every frame in the while loop to exit whenever

    key  =  cv2.waitKey(1) & 0xff  

    if key == ord('q'):
        frame_number = 1
        break
    frame_number += 1
vid.release()
cv2.destroyAllWindows()

user_data = [time_data, tired_data, unfocus_data]
plot_report(user_data)


# push
