#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:26:20 2023

@author: dominic
"""

# Importing libraries
import pandas as pd
import pickle

dataset = pd.read_csv('Data/hiring.csv')

# Feature Engineering

dataset['experience'].fillna(0, inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

X = dataset.iloc[:, :3]

# Converting words to integer values
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
                 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
                 'eleven':11, 'twelve':12, 'zero':0, 0:0}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

# Target/Dependent feature
y = dataset.iloc[:, -1]

# Since dataset is very small, Training will be done with all available data

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Fitting model with training data
regressor.fit(X, y)

# Saving model to pkl file
pickle.dump(regressor, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
