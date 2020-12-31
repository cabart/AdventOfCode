# Advent of Code - Day 7-2
# Handy Haversacks
# extremely ugly solution

import re

allBags = {}

def calculate (x):
    if allBags[x][0] == -1:
        count = 0
        for i in allBags[x][1]:
            count += int(i[0]) * calculate(i[1]) + int(i[0])
        allBags.update({x:(count,allBags[x][1])})
        return count
    else:
        return allBags[x][0]


f = open("input")
for line in f:
    bags = line.split(" bags contain ")
    if(bags[1].startswith("no other")):
        allBags.update({bags[0]:(0,[])})
    else:
        s = list(filter(None, re.split('\sbags?[\.\n|,\s]+',bags[1])))
        finalList = []
        for i in s:
            finalList.append([i[0],i[2:]])
        allBags.update({bags[0]:(-1,finalList)})

print(calculate("shiny gold"))
#for i in allBags:
#    print(i,allBags[i])
