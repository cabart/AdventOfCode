# Advent of Code - Day 1-1
# find x,y s.t. x + y = 2020 and output x * y

numbers = []

f = open("input")
for line in f:
    numbers.append(int(line))

#print(numbers)

print("Result:")
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if(numbers[i] + numbers[j] == 2020):
            result = numbers[i] * numbers[j]
            print(numbers[i],"+",numbers[j],"=",result)


