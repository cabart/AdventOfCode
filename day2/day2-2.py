# Advent of Code - Day 2-2
# Check passwords for validity
# <first_position>-<second_position> <letter>: <password>

import re

valid = 0

f = open("input")
for line in f:
    line = re.split('-|:| |\n',line)
    firstPosition = int(line[0]) - 1 # index correction
    secondPosition= int(line[1]) - 1 # index correction
    letter = line[2]
    password = line[4]
    #print(lowerBound,"<",letter,"<",upperBound,":",password)
    check1 = password[firstPosition] == letter
    check2 = password[secondPosition] == letter

    if(check1 != check2):
        valid += 1

print("number of valid passwords:",valid)
