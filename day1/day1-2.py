# Advent of Code - Day 1-2
# find x,y,z s.t. x + y + z = 2020 and output x * y * z

numbers = []

f = open("input")
for line in f:
    numbers.append(int(line))

#print(numbers)

print("Result:")
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        for k in range(j,len(numbers)):
            if(numbers[i] + numbers[j] + numbers[k] == 2020):
                result = numbers[i] * numbers[j] * numbers[k]
                print(numbers[i],"+",numbers[j],"+",numbers[k],"=",result)


