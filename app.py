# import cv2
# import dlib

# # Load pre-trained facial landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

# # Open the webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the image
#     faces = detector(gray)

#     for face in faces:
#         # Get facial landmarks
#         landmarks = predictor(gray, face)
        
#         # Extract eye coordinates
#         left_eye = (landmarks.part(36).x, landmarks.part(36).y, landmarks.part(39).x, landmarks.part(39).y)
#         right_eye = (landmarks.part(42).x, landmarks.part(42).y, landmarks.part(45).x, landmarks.part(45).y)

#         # Draw rectangles around the eyes
#         cv2.rectangle(frame, (left_eye[0], left_eye[1]), (left_eye[2], left_eye[3]), (0, 255, 0), 2)
#         cv2.rectangle(frame, (right_eye[0], right_eye[1]), (right_eye[2], right_eye[3]), (0, 255, 0), 2)

#         # Calculate the ratio of the width of the eye to the face
#         eye_width_ratio = (left_eye[2] - left_eye[0]) / (face.right() - face.left())
#         print(f"Eye Width Ratio: {eye_width_ratio}")

#         # Threshold for considering someone is looking at the screen
#         threshold = 0.2

#         # Check if the person is looking at the screen
#         if eye_width_ratio > threshold:
#             cv2.putText(frame, "Looking at the Screen", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # Display the frame
#     cv2.imshow("Screen Look Detection", frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     img = cv2.Canny(frame, 100, 200) # Some image processing

#     cv2.imshow('frame', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import av
# import cv2

# st.title("My first Streamlit app")
# st.write("Hello, world")

# threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
# threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)


# def callback(frame):
#     img = frame.to_ndarray(format="bgr24")

#     img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2))

#     return av.VideoFrame.from_ndarray(img, format="bgr24")


# webrtc_streamer(
#     key="example",
#     video_frame_callback=callback,
#     rtc_configuration={  # Add this line
#         "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
#     }
# )




from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

send_data = True

def continuous_data_sender():
    global send_data
    counter = 0
    while True:
        if send_data:
            counter += 1
            socketio.emit('data_update', {'counter': counter})
            time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle_data_sending')
def toggle_data_sending():
    global send_data
    send_data = not send_data
    emit('status_update', {'status': 'Data sending ' + ('enabled' if send_data else 'disabled')})

if __name__ == '__main__':
    socketio.start_background_task(target=continuous_data_sender)
    socketio.run(app, host='0.0.0.0', port=5000, debug = True)




