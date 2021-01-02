# Advent of Code - Day 12-1
# Rain Risk

import re

f = open("input")
data = [[x[0],int(x[1:])] for x in f.readlines()]
f.close()

x = 0
y = 0
directions = ['E','S','W','N']
direction = 0

def move(d,n):
    global x
    global y
    if d == 'E':
        x += n
    elif d == 'W':
        x -= n
    elif d == 'N':
        y += n
    elif d == 'S':
        y -= n

for i in data:
    d = i[0]
    pattern = re.compile("E|W|N|S")
    if pattern.match(d):
        move(d,i[1])
    elif i[0] == 'F':
        move(directions[direction],i[1])
    elif d == 'R':
        turn = int((i[1]/90)%4) + direction
        direction = turn%4
    elif d == 'L':
        turn = int(4-((i[1]/90)%4)) + direction
        direction = turn%4

print(x,y)
result = abs(x) + abs(y)
print(result)
