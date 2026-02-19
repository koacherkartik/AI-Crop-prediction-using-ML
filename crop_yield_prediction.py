import joblib
import pandas as pd

model = joblib.load("models/crop_yield_rf.pkl")

def predict_yield(area, season, crop):
    df = pd.DataFrame([[area, season, crop]],
                      columns=["Area", "Season", "Crop"])
    return model.predict(df)[0]

if __name__ == "__main__":
    yield_pred = predict_yield(5.0, "Kharif", "Rice")
    print("Predicted Yield:", yield_pred)
