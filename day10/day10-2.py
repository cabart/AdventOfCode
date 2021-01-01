# Advent of Code - Day 10-2
# Adapter Array


f = open("input")
data = [int(x) for x in f.readlines()]
f.close()

data.append(0)
data.sort()
data.append(data[len(data)-1]+3)

possible = [0] * len(data)
possible[0] = 1

for i in range(1,len(data)):
    acc = 0
    for j in range(max(0,i-3),i):
        if data[i] - data[j] <= 3:
            acc += possible[j]
    possible[i] = acc

result = possible[len(data)-1]
print(result)
