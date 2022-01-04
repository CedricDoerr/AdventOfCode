import sys

with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day4/input.txt') as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = numbers.split(',')
    boards = [[row.split() for row in board.split('\n')] for board in boards]

def isWinner(board, draw_numbers, draw_number):
    row_cols = [{n for n in row} for row in board]
    row_cols += [{n for n in col} for col in zip(*board)]
    for s in row_cols:
        if s.issubset(draw_numbers):
            all_numbers = {n for row in board for n in row}
            return sum(int(n) for n in (all_numbers - draw_numbers)) * int(draw_number)

draw_numbers = set()

for number in numbers:
    draw_numbers.add(number)
    for board in boards:
        if (bingo := isWinner(board, draw_numbers, number)):
            if(len(boards) == 1):
                print(bingo)
                sys.exit()
            boards.remove(board)
            

