# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt



# I considered that even when there is no data dowloaded from the CDN neither from the Peer to Peer 
# network, the payload is still being considered for the calculus of the concurrency

file= open('datamining3.csv', encoding= 'utf_8_sig')
r=csv.DictReader(file, delimiter=',', dialect=csv.excel)
#dict which associates the 'readableDate' to the counter of viewers at this 'readableDate' time
d=dict()
for row in r:
     if row['content']=='content-03808':
        if row['company']=='Streamroot TV':
            if row['readableDate'] not in d.keys():
                d[row['readableDate']]=1
            else:
                d[row['readableDate']]=d[row['readableDate']]+1
plt.plot(list(d.keys()), list(d.values()))
plt.xlabel("time")
plt.ylabel("concurrency")
plt.title("Concurrency")
plt.show()

            
   
            
   
    


            
        
        
    