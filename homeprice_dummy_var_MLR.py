# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:36:30 2021

@author: User
"""

import pandas as pd

d=pd.read_csv('H:/data analyst/excel/homeprices.csv')

dumy=pd.get_dummies(d.town)
dumy

new_d=pd.concat([d,dumy],axis=1)
new_d

final=new_d.drop(['town'],axis=1)
print(final)

final=final.drop(['monroe township'],axis=1)
final

x=final.iloc[:,[0,2,3]].values
y=final.iloc[:,1].values

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(x,y)

#price in west windser for 3400sqr.ft
lm.predict([[3400,0,1]])

#price in robinsville for 2800sq.ft
lm.predict([[2800,1,0]])

#price in monroe for 4500sq.ft
lm .predict([[4500,0,0]])


#ONE CODE ENCODING

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()                    #text column convert into a numbers
new=d
new.town=le.fit_transform(new.town)
new

x=new[["town","area"]].values
y=new["price"].values

#Now use one hot encoder to create dummy variables for each of the town
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('town',OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(x)
X=X[:,1:]

lm.fit(X,y)
lm.score(X,y)
lm.predict([[0,1,3400]])
lm.predict([[1,0,2800]])


