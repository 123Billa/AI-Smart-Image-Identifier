import tensorflow as tf 

import numpy as np
from PIL import Image
#Load pretrained model ONCE

model = tf.keras.applications.MobileNetV2(weights="imagenet")

def preprocess_image(image: Image.Image):
    image = image.resize(224, 224)
    image = np.array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

def predict(image: Image.Image):
    processed = preprocess_image(image)
    predictions = model.predict(processed)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
    results = []
    for _, label, confidence in decoded:
        results.append({
            "label": label,
            "confidence": float(confidence)
        })
    return results 

