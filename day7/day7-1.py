# Advent of Code - Day 7-1
# Handy Haversacks
# extremely ugly solution

import re

allBags = {}

def calculate (x):
    if allBags[x][0] == -1:
        count = 0
        for i in allBags[x][1]:
            count += calculate(i)
        allBags.update({x:(count,allBags[x][1])})
        return count
    else:
        return allBags[x][0]


f = open("input")
for line in f:
    bags = line.split(" bags contain ")
    s = []
    if(bags[1].startswith("no other")):
        allBags.update({bags[0]:(0,s)})
    else:
        s = list(filter(None, re.split('\sbags?[\.\n|,\s]+|[0-9]+\s',bags[1])))
        allBags.update({bags[0]:(-1,s)})

    if bags[0] == "shiny gold":
        allBags.update({bags[0]:(1,s)})

count = -1 # subtract shiny gold itself
for i in allBags:
    if (calculate(i) > 0):
        count += 1
print(count)
