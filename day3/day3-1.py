# Advent of Code - Day 3-1
# Check forest for number of collision

forest = []

f = open("input")
for line in f:
    forestLine = []
    for i in line:
        if (i == "."):
            forestLine.append(0)
        elif (i == "#"):
            forestLine.append(1)
    forest.append(forestLine)

#print(forest)

xDim = len(forest[0])
yDim = len(forest)
#print(xDim)
#print(yDim)

def isTree(x,y):
    return forest[y][x%xDim]

hitTrees = 0
curX = 0
curY = 0
while(curY<yDim):
    hitTrees += isTree(curX,curY)
    curX += 3
    curY += 1
print("number of hit trees:",hitTrees)

