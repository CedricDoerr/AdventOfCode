from os import confstr
import statistics as sts
with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day7/input.txt') as f:
    data = [int(x) for x in f.read().split(',')]
mean = round(sts.mean(data))

def findFuel(dist):
    cost = 0
    for i in range(0,dist+1):
        cost += i
    return cost

def algorithm(lvl, crabs):
    fuel = 0
    for crab in crabs:
        fuel += findFuel(abs(crab-lvl))
    return fuel

fuelcost = 0
guess = mean

while True:
    if(algorithm(guess-1, data) < algorithm(guess, data)):
        guess -= 1
    if(algorithm(guess+1, data) < algorithm(guess, data)):
        guess += 1
    else:
        fuelcost = algorithm(guess, data)
        break

print(fuelcost)