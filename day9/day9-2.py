# Advent of Code - Day 9-2
# Enocding Error

import re
import sys

f = open("input")
data = [int(x) for x in f.readlines()]

size = len(data)
preamble = 25
sums = {}

def addSum(x):
    if(x in sums):
        sums.update({x:sums[x]+1})
    else:
        sums.update({x:1})

def removeSum(x):
    sums.update({x:sums[x]-1})

def findInvalid():
    for i in range(preamble):
        for j in range(i+1,preamble):
            s = data[i]+data[j]
            addSum(s)

    for i in range(preamble,len(data)):
        curSum = data[i]
        if (curSum not in sums):
            return curSum
        elif (sums[curSum] == 0):
            return curSum
        else:
            old = data[i-preamble]
            for j in range(i-preamble+1,i):
                removeSum(old+data[j])
                addSum(curSum + data[j])

def findSum(x):
    for i in range(size):
        acc = 0
        for j in range(i,size):
            acc += data[j]
            if(acc == x):
                print("range:",i,j)
                return min(data[i:j])+max(data[i:j])
            if(acc > x):
                break
            
invalid = findInvalid()
result = findSum(invalid)
print("result",result)
