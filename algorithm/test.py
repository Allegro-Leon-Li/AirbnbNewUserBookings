# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:38:29 2016

@author: Administrator
"""

import numpy as np
#import pandas as pd
import pickle
#from sklearn.preprocessing import LabelEncoder
#from xgboost.sklearn import XGBClassifier
from random import randint

xgb_1 = pickle.load(open("0001_model","rb"))
le = pickle.load(open("le_model","rb"))
user_x = np.random.randint(1,size=(1,161))
cts = []

for i in range(100):
    age = randint(-25,40)
    year = randint(2013,2016)
    month = randint(1,12)
    day = randint(1,30)
    user_x[0][0] = age
    user_x[0][1] = year
    user_x[0][2] = month
    user_x[0][3] = day
#    year = randint(2013,2016)
#    month = randint(1,12)
#    day = randint(1,30)
    user_x[0][4] = year
    user_x[0][5] = month
    user_x[0][6] = day
    gender = randint(7,9)
    user_x[0][gender] = 1
    signup = randint(11,14)
    user_x[0][signup] = 1
    flow = randint(15,32)
    user_x[0][15] = 1
    language = randint(39,40)
    user_x[0][language] = 1
    channel = randint(59,66)
    user_x[0][channel] = 1
    provider = randint(67,84)
    user_x[0][provider]=1
#    tracked = randint(85,92)
    user_x[0][92] = 1
    app = randint(93,96)
    user_x[0][app]=1
    device=randint(97,105)
    user_x[0][device] =1 
    browser = randint(106,120)
    user_x[0][browser] = 1
    temp = []
    y_pred = xgb_1.predict_proba(user_x)
    temp += le.inverse_transform(np.argsort(y_pred[0])[::-1])[:6].tolist()
#    max_index[i] = y_pred[0].tolist().index(max(y_pred[0]))
    if "NDF" in temp:
        temp.remove("NDF")
    cts.append(temp[:5])
    

