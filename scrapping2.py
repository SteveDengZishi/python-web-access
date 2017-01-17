#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:55:55 2017

@author: stevedeng
"""

import urllib
from bs4 import BeautifulSoup
#import re

with urllib.request.urlopen('http://python-data.dr-chuck.net/comments_230721.html') as hFile:
    hText = hFile.read()

soup = BeautifulSoup(hText,'lxml')
#print(soup.prettify())

#listNum = re.findall('[0-9]+',hText)
#print(listNum) // wrong as cannot use findall string pattern on byte-like object.

#print(type(hText)) #<class 'bytes'>
#print(type(soup))  #<class 'bs4.BeautifulSoup'>

tags = soup('span')

sumVal = 0
for tag in tags:
    sumVal += int(tag.string)
print(sumVal)  


