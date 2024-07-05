from flask import Flask,render_template,url_for,request
from sklearn.preprocessing import StandardScaler
import joblib
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
model = joblib.load('model.lb')
# countvectorizer = joblib.load('countvectorizer.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
       text = str(request.form['text'])
       tweet = [text]
       transform_text = model.transform(tweet)
       print(transform_text.shape)
       prediction = str(model.predict(transform_text)[0])
       print(prediction)
       dt ={'0':'negative','1':'positive','2':'neutral','3':'irrelevant'}


       ##fit() train ho jao,
       #  fit_transform() aapne jo knowledge ki hai apply karo
       # transform() pehle se fit ho rkahai to ab apply ker do
        
       result =  dt[prediction]
       
       
       with open('tweet.txt', 'a') as file:
            file.write(f"{result}\t{text}\n")
       return render_template('result.html', prediction=result)
        
    return render_template('home.html')
           
    

if __name__=="__main__":
    app.run(debug=True)