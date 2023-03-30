import json
import pickle
import math 

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=pickle.load(open('regmodel - Copy.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/templates/property-grid.html')
def property():
    return render_template('property-grid.html')
@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')



@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    output=regmodel.predict(final_input)[0]
    output = math.ceil(output) 
    return render_template("home.html",prediction_text="The House price prediction is {}$.".format(output))

if __name__=="__main__":
    app.run(debug=True)
   
     
