import os

# Suppress TensorFlow info and warning messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = all messages, 1 = remove info, 2 = remove warnings, 3 = remove errors

import tensorflow as tf
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib  # for loading the scaler
from tensorflow.keras.models import load_model
import pandas as pd

app = Flask(__name__)

# Load the trained ANN model
model = load_model(r"C:\Users\Neeru Jangid\OneDrive\Desktop\ds trainning\loan approval (DL)\ann_model.h5")

# Load the saved scaler
scaler = joblib.load(r"C:\Users\Neeru Jangid\OneDrive\Desktop\ds trainning\loan approval (DL)\scaler.lb")

# Define feature names used in training (same as during model training)
feature_names = ['no_of_dependents', 'education', 'self_employed',
                 'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
                 'residential_assets_value', 'commercial_assets_value',
                 'luxury_assets_value', 'bank_asset_value']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from the form
        dependents = int(request.form['no_of_dependents'])
        education = 1 if request.form['education'] == "Graduate" else 0
        self_employed = 1 if request.form['self_employed'] == "Yes" else 0
        income_annum = float(request.form['income_annum'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        cibil_score = float(request.form['cibil_score'])
        residential_assets_value = float(request.form['residential_assets_value'])
        commercial_assets_value = float(request.form['commercial_assets_value'])
        luxury_assets_value = float(request.form['luxury_assets_value'])
        bank_asset_value = float(request.form['bank_asset_value'])

        # Prepare data for model
        user_input = np.array([[
            dependents, education, self_employed, income_annum, loan_amount,
            loan_term, cibil_score, residential_assets_value, commercial_assets_value,
            luxury_assets_value, bank_asset_value
        ]])

        # Convert to DataFrame to ensure feature order is correct
        user_df = pd.DataFrame(user_input, columns=feature_names)

        # Apply StandardScaler
        user_df_scaled = scaler.transform(user_df)

        # Make prediction
        prediction = model.predict(user_df_scaled)

        # Convert prediction to "Approved" or "Rejected"
        result = "Approved" if prediction[0] > 0.5 else "Rejected"

        return jsonify({"Loan Status": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
