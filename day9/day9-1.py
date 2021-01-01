# Advent of Code - Day 9-1
# Enocding Error

import re
import sys

f = open("input")
data = [int(x) for x in f.readlines()]
#print(data)

preamble = 25
sums = {}

def addSum(x):
    if(x in sums):
        sums.update({x:sums[x]+1})
    else:
        sums.update({x:1})

def removeSum(x):
    sums.update({x:sums[x]-1})

for i in range(preamble):
    for j in range(i+1,preamble):
        s = data[i]+data[j]
        addSum(s)
#print(sums)

for i in range(preamble,len(data)):
    curSum = data[i]
#    print("curSum:",curSum)
    if (curSum not in sums):
        print(curSum,"not valid")
        sys.exit()
    elif (sums[curSum] == 0):
        print(curSum,"not valid")
        sys.exit()
    else:
        old = data[i-preamble]
        for j in range(i-preamble+1,i):
            removeSum(old+data[j])
            addSum(curSum + data[j])
            
