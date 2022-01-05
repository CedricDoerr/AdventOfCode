reports = []
f = open('D:/Programmieren/adventofcode/day3/input.txt','r')
lines = f.read().splitlines()

reports.extend(lines)

generator = reports.copy()
scrubber = reports.copy()


""" gamma_str = ""
epsilon = 0 """

def mostCommonBit(position, list):
    help = 0
    for i in range(0, len(list)):
        help += int(list[i][position])
    return "1" if help >= len(list)/2 else "0"

def leastCommonBit(position, list):
    help = 0
    for i in range(0, len(list)):
        help += int(list[i][position])
    return "0" if help >= len(list)/2 else "1"

def remove(position, number, lists):
    limit = len(lists)
    i = 0
    while i < limit:
        if lists[i][position] == str(number): 
            i += 1
        else:
            print(i)
            lists.pop(i)
            limit += -1
            i += -1

generator_rating = 0
scrubber_rating = 0

for i in range (0, len(reports[0])):
    if len(generator) == 1: break
    print(generator, i, mostCommonBit(i, generator))
    remove(i, mostCommonBit(i, generator), generator)

for i in range (0, len(reports[0])):
    if len(scrubber)==1: break
    remove(i, leastCommonBit(i, scrubber), scrubber)

print(scrubber)
print(generator)
print(int(scrubber[0], 2)*int(generator[0], 2))
""" for i in range(0, len(reports[0])):
    gamma_str += mostCommonBit(i)

gamma = int(gamma_str, 2)
inverse_s = ''
  
for i in gamma_str:
    
    if i == '0':
        inverse_s += '1'
          
    else:
        inverse_s += '0'
epsilon = int(inverse_s, 2) """

