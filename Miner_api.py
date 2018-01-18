#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:26:21 2018

@author: stevedeng
"""
import requests
import sys

base_api = "https://api.ethermine.org"
pool_stat = "/poolStats"
miner_stat = "/miner/0x3DFDedeBD8c6BF9F31844161962762c700D97cb4/workers"
 
def checkMiner():
    url = base_api + miner_stat
    print("Retrieving data from url: %s\n" %url)
    r = requests.get(url)
    r_data = r.json()["data"]
    
    online_machines = len(r_data)
    print("Currently %d machines online\n" %online_machines)
    
    hashSum = 0.0
    for i in range(online_machines):
        dataDict = r_data[i]
        print("Status for %s" %dataDict["worker"])

        if dataDict["reportedHashrate"] != None:
            rh = float(dataDict["reportedHashrate"])/1000000
            ch = float(dataDict["currentHashrate"])/1000000
            print("The reported hashrate is %.2f MH/s" %rh)
            print("The current hashrate is %.2f MH/s\n" %ch)
            hashSum += rh
        else:
            print("The reported hashrate is 0.00 MH/s")
            print("The current hashrate is 0.00 MH/s\n")
        
    
    print("The total Hashrate is %.2f MH/s" %hashSum)
    
def checkPool():
    url = base_api + pool_stat
    print("Retrieving data from url: %s\n" %url)
    r = requests.get(url)
    r_data = r.json()["data"]
    
    poolStatDict = r_data["poolStats"]
    totalHash = poolStatDict["hashRate"]
    TH_hash = float(totalHash)/1000000000000
    minersNum = poolStatDict["miners"]
    minerK = int(minersNum)/1000
    machineNum = poolStatDict["workers"]
    machineK = int(machineNum)/1000
    blocksPerHour = poolStatDict["blocksPerHour"]
    diffIndex = float(blocksPerHour)/TH_hash
    
    print("The ethermine.org pool hashrate is: %.2f TH/s" %TH_hash)
    print("The total number of Miners is %dK" %minerK)
    print("The total number of Machines Mining in pool network is %dK" %machineK)
    print("The difficulty index (blocksPerHour/hash_TH)in ethermine pool is %.3f" %diffIndex)
    
    try:
        checkFile = open("data.csv","r")
        checkFile.close()
        appendFile = open("data.csv","a")
        appendFile.write(",%.2f,%.3f" %(TH_hash, diffIndex))
        appendFile.close()
    except FileNotFoundError:
        file = open("data.csv","w")
        file.write("%.2f,%.3f" %(TH_hash, diffIndex))
        file.close()
    
    
def main():
    
    while True: 
        
        target = input("What status do you want to check, miner or pool:\n")
        
        if target.lower() == "miner":
            checkMiner()
        elif target.lower() == "pool":
            checkPool()
        elif target.lower() == "exit":
            sys.exit()
        
if __name__ == "__main__":
    main()    
            