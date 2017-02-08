#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:20:14 2017

@author: stevedeng
"""

import csv

csvFile = open('SAT_Results.csv','r')
excelFile = open('Clean_Data_SAT.csv','w')

header = csvFile.readline();
header = header.strip().split(',');
header[0]='id'
header.append('Mean Total')
header.append('Highest Section')
header = ','.join(header)
print(header,file=excelFile)


csvReader = csv.reader(csvFile, delimiter=',',quotechar='"')
count=0
for row in csvReader:
    if(row[3]==row[4]==row[5]=='s'):
        continue
    count+=1
    row[0]=count
    
    row.append(int(row[3])+int(row[4])+int(row[5]))
    if(int(row[3])>int(row[4]) and int(row[3])>int(row[5])):
        row.append('CR')
    elif(int(row[4])>int(row[3]) and int(row[4])>int(row[5])):
        row.append('Math')
    else:
        row.append('Writing')
    row = ','.join(str(x) for x in row)
    print(row,file=excelFile)
        
        
        




