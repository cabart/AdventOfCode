# Advent of Code - Day 6-1
# Custom Customs

group = set()
count = 0

f = open("input")
for line in f:
    if (line == "\n"):
        count += len(group)
        group = set()
    else:
        for i in range(len(line)-1):
            group.add(line[i])
print(count)
