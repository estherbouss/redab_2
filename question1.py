# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:00:01 2022

@author: bates
"""
import matplotlib.pyplot as plt
import csv
"""  The metric I used is the percentage of data downloaded from the P2p among the data dowloaded from 
the cdn + p2p . It's thus the percentage p2p/ (p2p + cdn)"""


file= open('datamining.csv', encoding= 'utf_8_sig')
r=csv.DictReader(file, delimiter=',', dialect=csv.excel)

p2p= dict()
cdn= dict()
for row in r:
    if row['company'] in p2p.keys():
        p2p[row['company']]= p2p[row['company']]+ float(row['p2p'])
        cdn[row['company']]= cdn[row['company']]+ float(row['cdn'])
    else:
        p2p[row['company']]= float(row['p2p'])
        cdn[row['company']]= float(row['cdn'])
frequence=[]
for key, value in p2p.items():
    print(key, 100*(p2p[key])/( p2p[key]+ cdn[key]))
    frequence.append(100*(p2p[key])/(p2p[key]+ cdn[key]))

plt.bar(list(p2p.keys()),frequence)
plt.xlabel('company')
plt.ylabel('frequence')
plt.title('metric')
for i in range(len(list(p2p.keys()))):
        plt.text(i,frequence[i],str("{:.2f}".format(frequence[i]))+"%", ha='center')
plt.show()
file.close()

