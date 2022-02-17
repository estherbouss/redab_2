# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:37:19 2022

@author: bates
"""

import csv

file= open('datamining.csv', encoding= 'utf_8_sig')
r=csv.DictReader(file, delimiter=',', dialect=csv.excel)

total=0

before_total=0
count_session=0
line=1
for row in r:
    if float(row['sessionDuration'])==120000.0 and before_total >0:
        total=total+1
    before_total= int(row['totalPlaybackErrorCount'])
    before= float(row['sessionDuration'])
#if the last session's viewer had errors
if(before_total)>0:
    total=total+1

print(total)
        
file.close()  