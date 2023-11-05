from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import platform
# Load the trained model
model = load_model('my_model.h5')


def load_single_image(path, img_size=(48, 48)):
    images = []
    unix_path = path.replace('\\', '/')
    path = path if platform.system() == 'Windows' else unix_path
    # Open image, resize it and convert to grayscale 
    img = Image.open(path).resize(img_size).convert('L') 
    # Convert image to numpy array and normalize (rescale) it
    img = np.array(img) / 255.0
    images.append(img)
    
    return np.array(images)
# Path to the new image
def fatigue_pred(image_path):
    # Preprocess the image
    preprocessed_image = load_single_image(image_path)

    # Predict the class with the model
    prediction = model.predict(preprocessed_image)
    print(prediction)
    predicted_class = int(prediction > 0.2)  # Using 0.5 as the threshold
    return True if not predicted_class else False
