# Advent of Code - Day 6-2
# Custom Customs

group = set()
count = 0
new = True

f = open("input")
for line in f:
    if (line == "\n"):
        count += len(group)
        group = set()
        new = True
    else:
        mine = set()
        for i in range(len(line)-1):
            mine.add(line[i])
        if new:
            group = mine
            new = False
        else:
            group = group.intersection(mine)
print(count)
