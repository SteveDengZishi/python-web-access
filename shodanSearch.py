#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 02:54:17 2017

@author: stevedeng
"""

import shodan

SHODAN_API_KEY = 'qL3b6sfM0GG1p4SCovMvw92itrgHyPpU'
api = shodan.Shodan(SHODAN_API_KEY)

try:
    results = api.search('apache')
    print('Result found: %s' %results['total'])
    for result in results['matches']:
        print('IP: ', result['ip_str'])
        print(result['data'])
        print('')

except shodan.APIError as e:
    print('Error occurs: ', e)



