# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:57:09 2022

@author: bates
"""

import csv
file=open('datamining2.csv',encoding='utf_8_sig')
r=csv.DictReader(file,delimiter=',', dialect= csv.excel)
d=dict()
for row in r:
    if row['company'] in d.keys() and row['isFirstPayload']=='True':
        d[row['company']]= d[row['company']]+1 
        
    if row['company'] not in d.keys() and row['isFirstPayload']=='True':
        d[row['company']]=1
        
for key, value in d.items():
    print(key,':',value)
file.close()