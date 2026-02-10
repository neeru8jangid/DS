from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load pretrained model + scaler
model = joblib.load("modelrandclf.pkl")
scaler = joblib.load("standscaler.pkl")

# Your crop dictionary (label → number)
crop_dict = {
    'rice': 1,
    'maize': 2,
    'jute': 3,
    'cotton': 4,
    'coconut': 5,
    'papaya': 6,
    'orange': 7,
    'apple': 8,
    'muskmelon': 9,
    'watermelon': 10,
    'grapes': 11,
    'mango': 12,
    'banana': 13,
    'pomegranate': 14,
    'lentil': 15,
    'blackgram': 16,
    'mungbean': 17,
    'mothbeans': 18,
    'pigeonpeas': 19,
    'kidneybeans': 20,
    'chickpea': 21,
    'coffee': 22
}

# Reverse mapping: number → crop name
label_to_crop = {v: k for k, v in crop_dict.items()}

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/crop-tips")
def crop_tips():
    return render_template("crop_tips.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Extract & convert all features to float
    features = np.array([[
        float(data["N"]),
        float(data["P"]),
        float(data["K"]),
        float(data["temperature"]),
        float(data["humidity"]),
        float(data["ph"]),
        float(data["rainfall"])
    ]])

    # Scale using StandardScaler
    scaled = scaler.transform(features)

    # Predict (NumPy → Python int)
    pred_label = int(model.predict(scaled)[0])

    # Convert label → name
    crop_name = label_to_crop.get(pred_label, "Unknown crop")

    return jsonify({
        "recommended_crop": crop_name
    })

if __name__ == "__main__":
    app.run(debug=True)