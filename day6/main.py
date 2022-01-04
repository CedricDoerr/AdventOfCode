with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day6/input.txt') as f:
    data = f.read().split(',')

data = list(map(int, data))
print(data)
for i in range(0, 256):
    for x, fish in enumerate(data):
        if(data[x]==0):
            data[x] = 6
            data.append(9)
        else:
            data[x] -= 1

print(len(data))