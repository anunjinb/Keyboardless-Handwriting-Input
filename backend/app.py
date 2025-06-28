# --- backend/app.py ---
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

model = load_model("mnist_model.h5")  # Load your pre-trained model

def preprocess_image(base64_str):
    header, encoded = base64_str.split(',', 1)
    img_data = base64.b64decode(encoded)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.reshape(1, 28, 28, 1) / 255.0
    return img

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    image_data = data["image"]
    img = preprocess_image(image_data)
    prediction = model.predict(img)
    predicted_class = int(np.argmax(prediction))
    return jsonify({"letter": str(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
