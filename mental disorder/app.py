import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle
from sklearn.decomposition import PCA

 

app = Flask(__name__) #Initialize the flask App


model = pickle.load(open('survey.pkl', 'rb'))
 

 

@app.route('/')
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/abstract')
def abstract():
	return render_template('abstract.html')

@app.route('/future')
def future():
	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)
        
@app.route('/home')
def home():
    return render_template('test.html')

  


@app.route('/predict',methods=['POST'])
def predict():
    
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    y_pred = model.predict(final_features)
    if y_pred[0] == 1:
       label="Mental disorder"
    elif y_pred[0] == 0:
       label="Normal person"
    return render_template('test.html', prediction_text=label)
@app.route('/chart')
def chart():
	return render_template('chart.html')  
    
    
if __name__ == "__main__":
    app.run(debug=False)
