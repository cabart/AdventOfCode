# Advent of Code - Day 11-2
# Seating System
# Really slow due to repetedly reinitializing array

f = open("input")
data = [[y for y in list(x)] for x in f.readlines()]
f.close()
new = []

sizeX = len(data[0])
sizeY = len(data)
#print(sizeX,sizeY)

def numberNeighbours(x,y):
    acc = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if (not (i == 0 and j == 0)):
                found = False
                stop = False
                locX = x + i
                locY = y + j
                while(locX >= 0 and locX<sizeX and locY>=0 and locY<sizeY and (not stop)):
                    # test
                    if(data[locY][locX] == "#"):
                        found = True
                        stop = True
                    elif(data[locY][locX] == "L"):
                        stop = True
                    # increment
                    locX += i
                    locY += j
                if found:
                    acc += 1
    return acc

def changeSeat(x,y):
    n = numberNeighbours(x,y)
    if(data[y][x] == "L" and n == 0):
        new[y][x] = "#"
    elif(data[y][x] == "#" and n >= 5):
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
    
    # exitfor i in data:
        # exitprint(i)
    # exitprint("--------")

result = numberOfSeats()
print("no more changes after",iterations,"iterations")
print("resulting number used seats:",result)
