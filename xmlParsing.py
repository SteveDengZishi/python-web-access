#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:13:02 2017

@author: stevedeng
"""

import urllib
import xml.etree.ElementTree as ET

xFile = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_230718.xml')
xInput = xFile.read()

#print(type(xInput)) // <class 'bytes'>

tree = ET.fromstring(xInput) #similiar to Beautifulsoup way to make soup
#then one can make query on the object

countsList = tree.findall('.//count')
sumOfCount = 0
for count in countsList:
    sumOfCount += int(count.text)
print(sumOfCount)