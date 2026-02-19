import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model("models/plant_disease_cnn.h5")
classes = ["Healthy", "Rust", "Leaf Spot", "Blight"]

def predict_disease(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return classes[np.argmax(pred)]

if __name__ == "__main__":
    print(predict_disease("sample_data/leaf.jpg"))
