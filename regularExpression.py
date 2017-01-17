#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:27:53 2017

@author: stevedeng
"""

import re

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
host = re.findall('^From.*@([^ ]*)',line)
host2 = re.findall('@(\S+)',line)
print(host)
print(host2)