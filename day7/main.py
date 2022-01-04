import statistics as sts
with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day7/input.txt') as f:
    data = [int(x) for x in f.read().split(',')]
median = sts.median(data)
fuel = 0

for crab in data:
    fuel += abs(crab - median)

print(fuel)