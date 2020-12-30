# Advent of Code - Day 4-1
# Check passport for validity
# <characteristic>:<value> " " | \n
# empty line: end of passport

import re

validSet = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
def checkValidity (x):
    return validSet.issubset(x)


valid = 0
currentPassport = set() 

f = open("input")
for line in f:
    if(line == "\n"):
        if(checkValidity(currentPassport)):
            valid += 1
        currentPassport = set()
    else:
        line = line.rstrip()
        line = line.split(" ")
        for i in line:
            i = i.split(":")
            #print(i)
            currentPassport.add(i[0])

print("number of valid passwords:",valid)
