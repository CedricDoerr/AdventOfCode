from collections import defaultdict
from typing import DefaultDict


with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day6/input.txt') as f:
    data = f.read().split(',')

data = list(map(int, data))

X = defaultdict(int)
for fish in data:
    if(fish not in X):
        X[fish] = 1
    else:
        X[fish]+=1

for i in range(0, 256):
    Y = defaultdict(int)
    for n, value in X.items():
        if(n == 0):
            Y[6] += value
            Y[8] += value
        else:
            Y[n-1] += value
    X = Y

print(sum(X.values()))