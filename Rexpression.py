#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:45:59 2017

@author: stevedeng
"""

import re
import urllib

url = "http://python-data.dr-chuck.net/regex_sum_230716.txt"
with urllib.request.urlopen(url) as hFile:
    hText = hFile.read()

pattern = re.compile('[0-9]+')
numList = re.findall(pattern,str(hText))

#print(numList)

sumOfNum = 0
for num in numList:
    sumOfNum += int(num)
print(sumOfNum)
