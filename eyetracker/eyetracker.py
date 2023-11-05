# import cv2
# import dlib
# from scipy.spatial import distance as dist
# import numpy as np

# # Function to convert the facial landmarks to a NumPy array
# def shape_to_np(shape, dtype="int"):
#     coords = np.zeros((shape.num_parts, 2), dtype=dtype)
#     for i in range(0, shape.num_parts):
#         coords[i] = (shape.part(i).x, shape.part(i).y)
#     return coords

# # Load the pre-trained facial landmark predictor
# predictor_path = "shape_predictor_68_face_landmarks.dat"  # Download from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# predictor = dlib.shape_predictor(predictor_path)

# # Load the face detector
# detector = dlib.get_frontal_face_detector()

# def get_eye_aspect_ratio(eye):
#     # Calculate the Euclidean distances between the two sets of vertical eye landmarks
#     A = dist.euclidean(eye[1], eye[5])
#     B = dist.euclidean(eye[2], eye[4])

#     # Calculate the Euclidean distance between the horizontal eye landmarks
#     C = dist.euclidean(eye[0], eye[3])

#     # Calculate the eye aspect ratio
#     ear = (A + B) / (2.0 * C)
#     return ear

# # Set the threshold for the eye aspect ratio to determine focus
# EAR_THRESHOLD = 0.2

# # Open the webcam
# cap = cv2.VideoCapture(0)
# focus_status_array = []

# while True:
#     ret, frame = cap.read()

#     # Convert the frame to grayscale for better face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the grayscale frame
#     faces = detector(gray)

#     for face in faces:
#         shape = predictor(gray, face)
#         shape = shape_to_np(shape)

#         # Extract eye coordinates
#         left_eye = shape[42:48]
#         right_eye = shape[36:42]

#         # Calculate eye aspect ratio for both eyes
#         left_ear = get_eye_aspect_ratio(left_eye)
#         right_ear = get_eye_aspect_ratio(right_eye)

#         # Average eye aspect ratio for both eyes
#         avg_ear = (left_ear + right_ear) / 2.0

#         # Check if the average eye aspect ratio is below the threshold
#         if avg_ear < EAR_THRESHOLD:
#             cv2.putText(frame, "Not Focused", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             focus_status = "Not Focused"
#         else:
#             cv2.putText(frame, "Focused", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             focus_status = "Focused"
#         focus_status_array.append(focus_status)
#         print(focus_status_array)


#     # Display the frame
#     cv2.imshow("Focus Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import dlib
from scipy.spatial import distance as dist
import numpy as np

# Function to determine focus status for a single frame
def determine_focus_status(frame):
    # Convert the frame to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape = shape_to_np(shape)

        # Extract eye coordinates
        left_eye = shape[42:48]
        right_eye = shape[36:42]

        # Calculate eye aspect ratio for both eyes
        left_ear = get_eye_aspect_ratio(left_eye)
        right_ear = get_eye_aspect_ratio(right_eye)

        # Average eye aspect ratio for both eyes
        avg_ear = (left_ear + right_ear) / 2.0

        # Output whether the person is focused or not for the single frame
        if avg_ear < EAR_THRESHOLD:
            return "Not Focused"
        else:
            return "Focused"

# Function to convert the facial landmarks to a NumPy array
def shape_to_np(shape, dtype="int"):
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

# Load the pre-trained facial landmark predictor
predictor_path = "shape_predictor_68_face_landmarks.dat"  # Download from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor = dlib.shape_predictor(predictor_path)

# Load the face detector
detector = dlib.get_frontal_face_detector()

def get_eye_aspect_ratio(eye):
    # Calculate the Euclidean distances between the two sets of vertical eye landmarks
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # Calculate the Euclidean distance between the horizontal eye landmarks
    C = dist.euclidean(eye[0], eye[3])

    # Calculate the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

# Set the threshold for the eye aspect ratio to determine focus
EAR_THRESHOLD = 0.2

# Open the webcam
cap = cv2.VideoCapture(0)

# Initialize flag for the first frame
first_frame_processed = False

# for i in range(1):
#     ret, frame = cap.read()


#     # Output focus status for the current frame
#     focus_status = determine_focus_status(frame)
#     print(f"Focus Status: {focus_status}")

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

def get_focus_status_for_frame(frame_number):
    # Set the frame number
    current_frame = 0

    while True:
        ret, frame = cap.read()

        # Check if it's the target frame
        if current_frame == frame_number:
            # Output focus status for the target frame
            return determine_focus_status(frame)

        current_frame += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
frame_number_to_check = 200 # Replace with the desired frame number
focus_status_result = get_focus_status_for_frame(frame_number_to_check)
print(f"Focus Status for Frame {frame_number_to_check}: {focus_status_result}")