# Advent of Code - Day 13-2
# Shuttle Search

import math
from functools import reduce

def toInt (x):
    if x == 'x':
        return 0
    else:
        return int(x)

def lcm (a,b):
    return abs(a*b) // math.gcd(a,b)

f = open("input")
data = [list(map(toInt,x.split(','))) for x in f.readlines()]
f.close()

buses = data[1]

t = buses[0]
curLCM = buses[0]
iterations = 0

for i in range(1,len(buses)):
    if (buses[i] == 0):
        continue
    else:
        found = False
        while(not found):
            iterations += 1
            check = buses[i]-(t%buses[i]) == i%buses[i]
            if(check):
                curLCM = lcm(curLCM,buses[i])
                found = True
            else:
                t += curLCM
print('result:',t,'found in',iterations,'iterations')
