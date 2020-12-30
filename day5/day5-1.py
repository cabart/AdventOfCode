# Advent of Code - Day 5-1
# Binary Boarding

import re

def binSearch(a,b,rem):
    if(len(rem) == 1):
        if (rem == "F" or rem == "L"):
            return a
        elif (rem == "B" or rem == "R"):
            return b
        else:
            print("shouldn't happen")
    else:
        cur = rem[0]
        rem = rem[1:]
        if (cur == "F" or cur == "L"):
            print("F: ",a,b,rem)
            return binSearch(a,a+int((b-a)/2),rem)
        else:
            print("B: ",a,b,rem)
            return binSearch(a+int((b-a)/2)+1,b,rem)


allSeats = []

f = open("input")
for line in f:
    rowL = line[0:7]
    columnL = line[7:10]
    resRow = binSearch(0,127,rowL)
    resCol = binSearch(0,7,columnL)
    allSeats.append(resRow*8+resCol)
    #print(line,"->",rowL,columnL,";")

print(max(allSeats))

