# Advent of Code - Day 13-1
# Shuttle Search

f = open("input")
data = [list(map(int,filter((lambda e: e!= 'x'),x.split(',')))) for x in f.readlines()]
f.close()
print(data)

time = data[0][0]
buses = data[1]

minWait = max(buses)
minBus = max(buses)

for i in buses:
    waitTime = i-(time%i)
    if waitTime < minWait:
        minWait = waitTime
        minBus = i

result = minWait * minBus

print('time to wait:',minWait,', bus number:',minBus)
print('result:',result)
