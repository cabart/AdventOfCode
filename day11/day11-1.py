# Advent of Code - Day 11-1
# Seating System

f = open("input")
data = [[y for y in list(x)] for x in f.readlines()]
f.close()
new = []

sizeX = len(data[0])
sizeY = len(data)
print(sizeX,sizeY)

def numberNeighbours(x,y):
    acc = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
           if(i == x and j == y):
               continue
           elif(i<0 or i>=sizeX or j<0 or j>=sizeY):
               continue
           else:
               if(data[j][i] == "#"):
                   acc += 1
    return acc

def changeSeat(x,y):
    n = numberNeighbours(x,y)
    if(data[y][x] == "L" and n == 0):
        new[y][x] = "#"
    elif(data[y][x] == "#" and n >= 4):
        new[y][x] = "L"
    else:
        new[y][x] = data[y][x]

def numberOfSeats():
    acc = 0
    for i in range(sizeY):
        for j in range(sizeX):
            if(data[i][j] == "#"):
                acc += 1
    return acc

def hasChanged():
    for i in range(sizeX):
        for j in range(sizeY):
            if(data[j][i] != new[j][i]):
                return True
    return False

changed = True
iterations = 0
while(changed):
    iterations += 1
    new = [ ["" for _ in range(sizeX)] for _ in range(sizeY)] 
    for i in range(sizeX):
        for j in range(sizeY):
            changeSeat(i,j)
    
    changed = hasChanged()
    data = new

result = numberOfSeats()
print("no more changes after",iterations,"iterations")
print("resulting number used seats:",result)
