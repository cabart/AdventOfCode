# Advent of Code - Day 4-2
# Check passport for validity, each field
# <characteristic>:<value> " " | \n
# empty line: end of passport

import re
import string

validSet = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
def checkValidity (x):
    return validSet.issubset(x)

def checkField (x,y):
    if (x=='byr'):
        return (1920 <= int(y) <= 2002)
    elif (x == 'iyr'):
        return (2010 <= int(y) <= 2020)
    elif (x == 'eyr'):
        return (2020 <= int(y) <= 2030)
    elif (x == 'hgt'):
        if(y[-2:] == 'cm'):
            size = int(y[:-2])
            return (150 <= size <= 193)
        elif(y[-2:] == 'in'):
            size = int(y[:-2])
            return (59 <= size <= 76)
        return False
    elif (x == 'hcl'):
        if (len(y) == 7 and y[0]=='#'):
            return all(c in string.hexdigits for c in y[1:])
        return False
    elif (x == 'ecl'):
        colors = {'amb','blu','brn','gry','grn','hzl','oth'}
        return (y in colors)
    elif (x == 'pid'):
        if(len(y) == 9):
            return y.isnumeric()
        return False
    return True

valid = 0
currentPassport = set() 
currentValid = True

f = open("input")
for line in f:
    if(line == "\n"):
        if(checkValidity(currentPassport) and currentValid):
            valid += 1
        currentPassport = set()
        currentValid = True
    else:
        line = line.rstrip()
        line = line.split(" ")
        for i in line:
            i = i.split(":")
            check = checkField(i[0],i[1])
            currentValid = currentValid and check
            currentPassport.add(i[0])

print("number of valid passwords:",valid)
