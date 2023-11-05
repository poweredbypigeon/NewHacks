from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import platform
# Load the trained model
model = load_model('my_model.h5')


def load_single_image(image, img_size=(48, 48)):
    #images = []
    #unix_path = path.replace('\\', '/')
    #path = path if platform.system() == 'Windows' else unix_path
    # Open image, resize it and convert to grayscale 
    img = Image.open(image).resize(img_size).convert('L') 
    # Convert image to numpy array and normalize (rescale) it
    img = np.array(img) / 255.0
    
    return img
# Path to the new image
def fatigue_pred(image):
    # Preprocess the image
    preprocessed_image = load_single_image(image)

    # Predict the class with the model
    prediction = model.predict(preprocessed_image)
    print(prediction)
    predicted_class = int(prediction > 0.2)  # Using 0.5 as the threshold
    return True if not predicted_class else False
