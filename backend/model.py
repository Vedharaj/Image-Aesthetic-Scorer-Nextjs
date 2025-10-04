import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image

# Build NIMA model using InceptionResNetV2 base
base_model = InceptionResNetV2(include_top=False, input_shape=(299, 299, 3), weights='imagenet')
x = GlobalAveragePooling2D()(base_model.output)
x = Dense(10, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=x)

# ✅ Load weights that match this architecture
model.load_weights("./models/inception_resnet_weights.h5")

def predict_aesthetic(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    preds = model.predict(x)[0]
    score = np.sum(preds * np.arange(1, 11))
    return round(float(score), 2)

# if __name__ == "__main__":
#     # Test the model with a sample image
#     test_image_path = "img.jpg"
#     print(f"Aesthetic Score: {predict_aesthetic(test_image_path)}")
    