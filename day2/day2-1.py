# Advent of Code - Day 2-1
# Check passwords for validity
# <lower_bound>-<upper_bound> <letter>: <password>

import re

valid = 0

f = open("input")
for line in f:
    line = re.split('-|:| |\n',line)
    lowerBound = int(line[0])
    upperBound = int(line[1])
    letter = line[2]
    password = line[4]
    #print(lowerBound,"<",letter,"<",upperBound,":",password)
    occurences = 0
    for elem in password:
        if (elem == letter):
            occurences += 1
    if (lowerBound <= occurences <= upperBound):
        valid += 1
        #print("valid\n")
    else:
        valid = valid
        #print("invalid\n")

print("number of valid passwords:",valid)
