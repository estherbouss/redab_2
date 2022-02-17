# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:12:30 2022

@author: bates
"""

from csv import reader
from csv import writer
from datetime import datetime


default_text = True
# Open the input_file in read mode and output_file in write mode
with open('datamining.csv', 'r') as read_obj, \
        open('datamining3.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    header= next(csv_reader)
    header.append('readableDate')
    csv_writer.writerow(header)
    for row in csv_reader:
        if row[0]=='Streamroot TV':
            #to make timestamp in seconds, not in milliseconds
            t= int(row[8])/1000
            t=t-60
            dt_object = datetime.fromtimestamp(t)
            dt=dt_object.strftime("%H:%M")
            row.append(dt)
            csv_writer.writerow(row)
        else:
            csv_writer.writerow(row)
            
write_obj.close()
read_obj.close()