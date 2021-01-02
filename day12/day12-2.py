# Advent of Code - Day 12-2
# Rain Risk

import re

f = open("input")
data = [[x[0],int(x[1:])] for x in f.readlines()]
f.close()

wX = 10
wY = 1
sX = 0
sY = 0

def moveWaypoint(d,n):
    global wX,wY
    if d == 'E':
        wX += n
    elif d == 'W':
        wX -= n
    elif d == 'N':
        wY += n
    elif d == 'S':
        wY -= n

def moveShip(n):
    global wX,wY,sX,sY
    sX += n * wX
    sY += n * wY

for i in data:
    d = i[0]
    pattern = re.compile("E|W|N|S")
    if pattern.match(d):
        moveWaypoint(d,i[1])
    elif i[0] == 'F':
        moveShip(i[1])
    else:
        if d == 'L':
            turn = int((i[1]/90)%4)
        else:
            turn = int(4-((i[1]/90)%4))
        for i in range(turn):
            tmp = wX
            wX = -wY
            wY = tmp

print(sX,sY)
result = abs(sX) + abs(sY)
print(result)
