#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:29:14 2017

@author: stevedeng
"""

import subprocess
import cmd
import sys

while(True):
    command = input("Steves-MacBook-Pro:~ stevedeng$ ")
    
    if command == "exit":
        sys.exit(0)
        
    command = command.split()
    
    rc = subprocess.check_output(command)
    rc = rc.decode('utf-8').split('\n')
    for line in rc:
        print(line)
    #child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
    #child.communicate("vamei".encode())