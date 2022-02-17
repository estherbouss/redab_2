# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:02:20 2022

@author: bates
"""
from csv import reader
from csv import writer



default_text = True
# Open the input_file in read mode and output_file in write mode
with open('datamining.csv', 'r') as read_obj, \
        open('datamining2.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    header= next(csv_reader)
    header.append('isFirstPayload')
    csv_writer.writerow(header)
    for row in csv_reader:
        add= 'True' if float(row[9])==120000.0 else 'False'
        row.append(add)
        csv_writer.writerow(row)
read_obj.close()
write_obj.close()