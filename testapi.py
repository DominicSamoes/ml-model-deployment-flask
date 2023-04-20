#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:57:39 2023

@author: dominic
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())