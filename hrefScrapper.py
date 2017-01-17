#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: stevedeng
"""

import urllib
from bs4 import BeautifulSoup

url = input('Please enter a url: ')
count = int(input('Please enter a count: '))
position = int(input('Please enter a position: '))

with urllib.request.urlopen(url) as hFile:
    print('Retrieving: ', url)
    hText = hFile.read()

soup = BeautifulSoup(hText,'lxml')
#print(soup.prettify())

for i in range(count):
    tags = soup('a')
    url = tags[position-1]['href']
    with urllib.request.urlopen(url) as hFile:
        print('Retrieving: ', url)
        hText = hFile.read()
        soup = BeautifulSoup(hText,'lxml')