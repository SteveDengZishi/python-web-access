#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:18:12 2017

@author: stevedeng
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode())

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data, end = '')

mysock.close()