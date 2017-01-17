#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:06:59 2017

@author: stevedeng
"""

from bs4 import BeautifulSoup
import urllib

hFile = urllib.request.urlopen('http://www.virtualityfit.com').read()
soup = BeautifulSoup(hFile,'lxml')
print(soup.prettify())

print(soup.head)