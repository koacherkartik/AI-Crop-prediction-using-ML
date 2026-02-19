import numpy as np
import pandas as pd
import joblib

model = joblib.load("models/crop_recommendation_mlp.pkl")

def recommend_crop(N, P, K, temp, humidity, ph, rainfall):
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)
    return prediction[0]

if __name__ == "__main__":
    crop = recommend_crop(90, 42, 43, 20.8, 82.0, 6.5, 202.9)
    print("Recommended Crop:", crop)
