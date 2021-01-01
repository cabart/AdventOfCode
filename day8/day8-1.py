# Advent of Code - Day 8-1
# Handheld Halting

import re

f = open("input")
code = [[y for y in x.split(" ")] for x in f.readlines()]
code = list(map(lambda x: [x[0],int(x[1]),False],code))

acc = 0
pos = 0

while(not code[pos][2]):
    op = code[pos][0]
    code[pos][2] = True
    if(op == "nop"):
        pos += 1
    elif(op == "acc"):
        acc += code[pos][1]
        pos += 1
    elif(op == "jmp"):
        pos += code[pos][1]

print(acc)
