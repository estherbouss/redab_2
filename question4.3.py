# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:05:47 2022

@author: bates
"""
import matplotlib.pyplot as plt
import csv
from csv import reader
import numpy as np

#Answer 4.3 and 4.4
"""After careful review, I saw that the performance didn't increase significantly with the concurrency, 
which I found very surprising, since it it's the whole goal of the Peer to Peer Technology.
That's why I don't have an answer for this 4.4 question, because the answer I would give doesn't make 
so much sense. I tried to plot the graph performance/ concurrency for different contents, and again I 
haven't found any true correlation between the two, which is as I said, surprising.
Also, there were payloads where the amount of data of p2p and of cdn was 0 wheras the upload wasn't null.
These payloads have been taken into account for the calculus of the concurrency but they've just made the 
performance decrease. I would be happy to hear from you back to solve this apperant problem."""

def date_conc(content):
    file= open('datamining3.csv', encoding= 'utf_8_sig')
    r=csv.DictReader(file, delimiter=',', dialect=csv.excel)
#dict which associates the 'readableDate' to the counter of viewers at this 'readableDate' time
    d=dict()
    p= dict()
    for row in r:
        if row['content']==content:
            if row['company']=='Streamroot TV':
                num=100*float(row['p2p'])
                denom=float(row['cdn'])+float(row['p2p'])
                if row['readableDate'] not in d.keys():
                    d[row['readableDate']]=1
                    p[row['readableDate']]=0
                    if denom!=0.0:
                        p[row['readableDate']]=num/denom
                else:
                    d[row['readableDate']]=d[row['readableDate']]+1
                    if denom!=0.0:
                        p[row['readableDate']]=p[row['readableDate']]+num/denom
    for i in p.keys():
        p[i]=p[i]/d[i]
    
        
    
    plt.scatter(list(d.values()), list(p.values()))
    plt.plot(list(d.values()), np.full(len(d),80),color="red")
    plt.show()
        
    
date_conc('content-05335')
            