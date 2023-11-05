from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import platform
# Load the trained model
model = load_model('my_model.h5')


def preprocess_image(image, img_size=(48, 48)):
    # Resize the image and convert to grayscale 
    img = image.resize(img_size).convert('L') 
    # Convert image to numpy array and normalize (rescale) it
    img = np.array(img) / 255.0
    return img

def fatigue_pred(image):
    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Predict the class with the model
    prediction = model.predict(np.array([preprocessed_image]))
    predicted_class = int(prediction > 0.2)  # Using 0.2 as the threshold
    return True if not predicted_class else False
