with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day8/input.txt') as f:
    data = f.read().split('\n')
    data = [[line.split() for line in line.split(' | ')] for line in data]
count = 0

for line in data:
    for digit in line[1]:
        x = len(digit)
        if(x == 2 or x == 4 or x == 3 or x == 7):
            count += 1

print(count)