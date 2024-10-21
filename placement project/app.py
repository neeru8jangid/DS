from flask import Flask, request, jsonify,render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template ('front.html')

# Define an endpoint to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method =='POST':
        Gender = int(request.form['Gender'])
        Stream = int(request.form['Stream'])
        Internships = int(request.form['Internships'])
        CGPA = int(request.form['CGPA'])
        HistoryOfBacklogs = int(request.form['HistoryOfBacklogs'])
        certificates = int(request.form['certificates'])

        user_data = [[Gender,Stream ,Internships,CGPA,HistoryOfBacklogs,certificates]]
        pred = model.predict(user_data)[0]
        prediction = str(round(pred,2))

        dt = {'0':'not getting placed','1':'getting placed'}
        result = dt[prediction]
        
        return render_template('front.html',prediction_text=result)
    
if __name__ == '__main__':
    app.run(debug=True)
