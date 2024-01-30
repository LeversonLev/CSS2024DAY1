# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:37:17 2024

@author: 202200128
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes

