#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:36:42 2017

@author: stevedeng
"""

import urllib
import json

api = 'http://python-data.dr-chuck.net/geojson'

while True:
    location = input("Please Enter a Location: ")
    if len(location) < 1:
        break
    
    url = api + '?' + urllib.parse.urlencode({'sensor' : 'false', 'address' : location})
    print('Retriving data from: ', url)
    
    jsHandle = urllib.request.urlopen(url)
    jsData = jsHandle.read()
    
    try:jsDict = json.loads(jsData.decode())
    except:jsDict = None
    
    #print(json.dumps(jsDict, indent = 4))
    
    idNum = jsDict['results'][0]['place_id']
    print(idNum)
    
    
    