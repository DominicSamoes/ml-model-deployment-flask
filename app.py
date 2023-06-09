#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:17:45 2023

@author: dominic
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Employee Salary should be E {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    For returning result when called as a POST request
    """
    data = request.get_json(force=True)
    int_features = [int(x) for x in list(data.values())]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)