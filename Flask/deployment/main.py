# creating flask_app
from flask import Flask,request
app = Flask(__name__)
# defining a routed_call
@app.route('/hello_sk')
def hello():
    return "Hello Sarvesh Kesharwani"
# 
@app.route('/add', methods=['GET'])
def add_GET1():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))
    
import pickle
model = pickle.load(open('Iris_SV_Classfier.pkl', 'rb'))
        
# 
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return 'please send post request!'
    elif request.method == 'POST':
        input_paras = request.get_json()
        
        sepal_length = input_paras['sepal_length']
        sepal_width = input_paras['sepal_width']
        petal_length = input_paras['petal_length']
        petal_width = input_paras['petal_width']
        
        import numpy as np
        input = np.array([[sepal_length, sepal_width, petal_length, petal_width]]) 
        # so basically this 2d array in input ka mutlib ye hai ki, this 1d array in [] is nothing
        # but a row, being passed for prediction to model
        
        prediction = model.predict(input)
        return str(prediction)
        
# running flask_app
app.run()
# http://127.0.0.1:5000/predict