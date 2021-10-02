# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:47:52 2021

@author: User
"""

import pandas as pd
import numpy as np
df=pd.read_csv('H:/data analyst/excel/house_pred.csv')

import math
df.bedrooms.median()
new_df= df.fillna(4)
new_df

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(new_df.drop("price",axis=1),df.price)   #......model(pass independent var,pass D.V.)

model.predict([[3100,4,10]])            # 730751.22364134 is predicted value

model.coef_              #coeff of x

model.intercept_             # y intercept
