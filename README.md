# AI Crop Prediction System using Machine Learning

This project is an AI-driven agricultural decision support system that helps farmers and researchers make informed decisions using machine learning and deep learning models.

The system performs crop recommendation, yield prediction, fertilizer suggestion, and plant disease detection using real-world agricultural data.

## Key Features

- Crop recommendation based on soil nutrients and weather conditions
- Crop yield prediction using regression models
- Fertilizer recommendation using rule-based logic
- Plant disease detection from leaf images using CNN
- End-to-end ML pipeline with preprocessing, training, and inference

## Plant Disease Detection (Sample Output)

The model classifies plant diseases from leaf images using a trained Convolutional Neural Network.

Input: Tomato leaf image  
Output: Tomato Yellow Leaf Curl Virus

The example below demonstrates inference on a sample image.

```python
image_path = "sample_data/tomato_leaf.jpg"
predicted_class = predict_disease(image_path)
print("Predicted Disease:", predicted_class)

