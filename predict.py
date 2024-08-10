import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def load_trained_model(model_path='/Users/sujalpanchal/Desktop/hackathon/models/final_model.h5'):
    return load_model(model_path)

def predict(image_path, model, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    predictions = model.predict(img_array)
    return np.argmax(predictions, axis=1)
