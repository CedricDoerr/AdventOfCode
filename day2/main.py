commands = []
f = open('D:/Programmieren/adventofcode/day2/input.txt','r')
lines = f.read().splitlines()

commands.extend(lines)

horizontal = 0
depth = 0
aim = 0

for command in commands:
 
    help = command.split()
    if help[0]=="up": aim-=int(help[1])
    if help[0]=="down": aim+=int(help[1])
    if help[0]=="forward":
         horizontal+=int(help[1])
         depth+=aim*int(help[1])

print(horizontal, depth)
print(horizontal*depth)
