# Advent of Code - Day 8-2
# Handheld Halting

import re

f = open("input")
code = [[y for y in x.split(" ")] for x in f.readlines()]
code = list(map(lambda x: [x[0],int(x[1]),False],code))

def runCode():
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
        if(pos == len(code)):
            return (True,acc)
    return (False,acc)

def swap(i):
    op = code[i][0]
    if op == "nop":
        code[i][0] = "jmp"
    elif op == "jmp":
        code[i][0] = "nop"

for i in range(len(code)):
    swap(i)
    result = runCode()
    swap(i)
    if(result[0]):
        print("result:",result[1])
    # cleanup
    for i in range(len(code)):
        code[i][2]=False
