# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:51:14 2021

@author: User
"""

import pandas as pd
import numpy as np
from word2number import w2n

d=pd.read_csv('H:/data analyst/excel/hiring.csv')

d.experience =d.experience.fillna("zero")
d

d.experience=d.experience.apply(w2n.word_to_num)
d

import math
d['test_score(out of 10)']=d['test_score(out of 10)'].median()
d['test_score(out of 10)'].fillna(d['test_score(out of 10)'])
d

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
x=d.iloc[:,:3].values
y=d.iloc[:,-1].values
lm.fit(x,y)

lm.predict([[2,9,6]])
lm.predict([[10,9,9]])
lm.predict([[0,6,6]])

