# Advent of Code - Day 3-2
# Check forest for number of collision
# Check for different slopes - multiply together

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

# x,y -> slopes
def checkCollision(x,y):
    hitTrees = 0
    curX = 0
    curY = 0
    while(curY<yDim):
        hitTrees += isTree(curX,curY)
        curX += x
        curY += y
    return hitTrees

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1
for i in slopes:
    result *= checkCollision(i[0],i[1])

print("number of hit trees:",result)

