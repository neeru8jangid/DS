from flask import Flask , render_template

app = Flask(__name__)
#127.0.0.1:2525/
@app.route('/') #URL
def home():
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)
