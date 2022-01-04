from abc import abstractmethod


with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day5/input.txt') as f:
    data = f.read().split('\n')
    '''data = [[rows.split(' -> ') for rows in rows.split('\n')] for rows in data]'''
    data = [[n.split(',') for n in rows.split(' -> ')] for rows in data]

map = dict()

def addEntrys(row, horizontal):
    i = 0
    end = 0
    if(horizontal):
        if(int(row[0][0]) < int(row[1][0])):
            i = int(row[0][0])
            end = int(row[1][0])
        else:
            i = int(row[1][0])
            end = int(row[0][0])
        while i <= end:
            if(str(i)+':'+row[0][1] in map):
                map[str(i)+':'+row[0][1]] = 2
            else:
                map[str(i)+':'+row[0][1]] = 1
            i += 1
    else:
        if(int(row[0][1]) < int(row[1][1])):
            i = int(row[0][1])
            end = int(row[1][1])
        else:
            i = int(row[1][1])
            end = int(row[0][1])
        while i <= end:
            if(row[0][0]+':'+str(i) in map):
                map[row[0][0]+':'+str(i)] = 2
            else:
                map[row[0][0]+':'+str(i)] = 1
            i += 1

def addDiagonal(row, y_abs):
    x = 0
    y = 0
    end = 0
    richtung = True
    if(int(row[0][0]) < int(row[1][0])):
        x = int(row[0][0])
        y = int(row[0][1])
        end = int(row[1][0])
        if(y_abs < 0): richtung=True
    else:
        x = int(row[1][0])
        y = int(row[1][1])
        end = int(row[0][0])
        if(y_abs < 0): richtung=False
    while x <= end:
        if(str(x)+':'+ str(y) in map):
            map[str(x) +':'+ str(y)] = 2
        else:
            map[str(x)+':'+str(y)] = 1
        if(richtung):
            y += 1
        else:
            y -= 1
        x += 1


for row in data:
    if(row[0][1]==row[1][1]):
        addEntrys(row, True)
        data.remove(row)
    if(row[0][0]==row[1][0]):
        addEntrys(row, False)
        data.remove(row)
    
for row in data:
    y_abs = int(row[0][1]) - int(row[1][1])
    if(abs(int(row[0][0]) - int(row[1][0])) == abs(y_abs)):
        addDiagonal(row, y_abs)

counter = 0

for value in map.values():
    if (value == 2): counter += 1

print(counter)