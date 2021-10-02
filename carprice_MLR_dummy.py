# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:58:57 2021

@author: User
"""

import pandas as pd 
cp=pd.read_csv('H:/data analyst/excel/carprices.csv')
cp
import seaborn as sns
sns.pairplot(cp)

dumy=pd.get_dummies(cp["Car Model"])
dumy
carprices=pd.concat([cp,dumy],axis=1)
carprices
carprices=carprices.drop(['Car Model'],axis=1)
carprices=carprices.drop(['Audi A5'],axis=1)

x=carprices.iloc[:,[0,2,3,4]].values
y=carprices.iloc[:,1].values

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(x,y)

lm.score(x,y)

#Q1=price of mercediz benz that 4 yr old 45000 milege
lm.predict([[45000,4,0,1]])

#Q2=price of bmw that 15 yr old 70000 milege
lm.predict([[70000,15,1,0]])

#Q3= audi 5 yr old ,35000 milege
lm.predict([[35000,5,0,0]])
