# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:55:03 2021

@author: User
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

excel=pd.read_csv('H:/data analyst/excel/canada_per_capita_income.csv')
print(type(excel))

X=excel.iloc[:,0:1].values
y=excel.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=2/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.coef_)
print(regressor.intercept_)

y_pred=regressor.predict(X_test)

regressor.predict([[2020]])

from sklearn.metrics import r2_score
r2_score(y_pred,y_test)

compare={'actual income':y_test,
         'predicted income':y_pred}
abc=pd.DataFrame(compare)
print(abc)

plt.scatter(y_test,X_test,c='red',marker='+')
plt.scatter(y_pred,X_test,c='green',marker='.')
plt.xlabel('income in US$')
plt.ylabel('year')
plt.title('canda income per capita')

