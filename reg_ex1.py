#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:26:30 2017

@author: stevedeng
"""

import re
from django.utils.encoding import smart_text

infile = open('regex_sum_42.txt','r')
for line in infile:
    line = force_text(line, encoding='utf-8', strings_only=False, errors='strict')
    print(line)
#num = []
#for line in infile:
    #num.extend(re.findall('[0-9]+',line))

#total = sum(num)
#print(total)
    
    