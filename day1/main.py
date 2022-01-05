#File Objects

numbers = []
f = open('D:/Programmieren/adventofcode/day1/input.txt','r')
lines = f.read().splitlines()
for line in lines:
    numbers.extend(line.split())

increased = 0

sums = []

for i in range(2, len(numbers)):
    x = int(numbers[i-2]) + int(numbers[i-1]) + int(numbers[i])
    sums.append(x)

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]: increased += 1

print(len(sums))
print(increased)



