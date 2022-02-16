# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:35:47 2022

@author: User
"""


import pandas as pd

table1={'userid':[1,2],'last_connection':['2/8/2017','12/19/2017']}
df1=pd.DataFrame(table1)
df1

table2={'userid':[2,2,3],'most_recent':['4/2/2018','5/7/2018','4/6/2018']}
df2=pd.DataFrame(table2)
df2


#They had a previous connection in last_connection and a connection in the last month in recent_connection
print(pd.merge(df1,df2, on='userid', how='inner'))

#They had a previous connection in last_connection but do not have a connection in the last month in recent_connection
print(pd.merge(df1,df2, on='userid', how='left'))

#They did not have a previous connection in last_connection but do have a connection in the last month in recent_connection
print(pd.merge(df1,df2, on='userid', how='right'))
