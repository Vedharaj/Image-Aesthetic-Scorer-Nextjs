# backend/model.py

import os
import numpy as np
import requests
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image

# -----------------------------
# Config
# -----------------------------
MODEL_PATH = "./models/inception_resnet_weights.h5"
MODEL_URL = "https://github.com/titu1994/neural-image-assessment/releases/download/v0.5/inception_resnet_weights.h5"
IMG_SIZE = (299, 299)

# -----------------------------
# Download model from URL
# -----------------------------
def download_model(url, destination):
    """Download file from URL if it does not exist"""
    if os.path.exists(destination):
        print(f"Model already exists at {destination}")
        return

    os.makedirs(os.path.dirname(destination), exist_ok=True)
    print(f"Downloading model from {url} ...")
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(destination, 'wb') as f:
        for data in response.iter_content(chunk_size=1024):
            f.write(data)
    print(f"Downloaded model to {destination}")

# -----------------------------
# Build NIMA model
# -----------------------------
def build_model():
    base_model = InceptionResNetV2(include_top=False, input_shape=(299, 299, 3), weights='imagenet')
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dense(10, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=x)
    return model

# -----------------------------
# Load or download weights
# -----------------------------
download_model(MODEL_URL, MODEL_PATH)
model = build_model()
model.load_weights(MODEL_PATH)
print("Model loaded successfully.")

# -----------------------------
# Prediction function
# -----------------------------
def predict_aesthetic(img_path):
    """Returns aesthetic score for a given image path"""
    img = image.load_img(img_path, target_size=IMG_SIZE)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    preds = model.predict(x)[0]
    score = np.sum(preds * np.arange(1, 11))
    return round(float(score), 2)

# -----------------------------
# Test locally
# -----------------------------
# if __name__ == "__main__":
#     test_image = "img.jpg"
#     if os.path.exists(test_image):
#         print(f"Aesthetic Score: {predict_aesthetic(test_image)}")
#     else:
#         print(f"Test image '{test_image}' not found.")