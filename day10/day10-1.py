# Advent of Code - Day 10-1
# Adapter Array


f = open("input")
data = [int(x) for x in f.readlines()]
f.close()

data.append(0)
data.sort()
data.append(data[len(data)-1]+3)

diff = [0,0,0]

for i in range(len(data)-1):
    diff[data[i+1]-data[i]-1] += 1

result = diff[0] * diff[2]
print(result)
