#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:34:46 2017

@author: stevedeng
"""

import json
import urllib

jsHandle = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_230722.json')
jsData = jsHandle.read()

#print(type(jsData)) byte-like object
#print(jsData)

jsDict = json.loads(jsData.decode())#you have to use byte.decode() instead of str(byte)
sumCount = 0;
for item in jsDict['comments']:
    sumCount += item['count']
print(sumCount)
    
    
    
