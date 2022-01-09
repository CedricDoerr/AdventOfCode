
with open('/Users/cedricdorr/Documents/Programmieren/AdventOfCode/day8/input.txt') as fin:
    data = [line for line in fin.read().strip().split('\n')]

def part2():
    inputs = [line.split('|')[0].strip().split(' ') for line in data]
    outputs = [line.split('|')[1].strip().split(' ') for line in data]

    totalSum = 0
    for i in range(len(data)):
        # Map each KNOWN digit to a number
        digitMap = {}

        # Update digitMap
        for digit in inputs[i]:
            if len(digit) == 2:
                digitMap[1] = digit
            elif len(digit) == 4:
                digitMap[4] = digit
            elif len(digit) == 3:
                digitMap[7] = digit
            elif len(digit) == 7:
                digitMap[8] = digit

        # Check for unknown digits
        for digit in inputs[i]:
            # For digits 0, 6, and 9 
            if len(digit) == 6:
                # 4 is part of 9 
                if set(digitMap[4]).issubset(set(digit)):
                    digitMap[9] = digit
                
                # 1 is part of 0
                elif set(digitMap[1]).issubset(set(digit)):
                    digitMap[0] = digit

                else:
                    digitMap[6] = digit
                
        # Check for unknown digits
        for digit in inputs[i]:
            # For digits 2, 3, and 5
            if len(digit) == 5:
                if set(digit).issubset(set(digitMap[6])):
                    digitMap[5] = digit
                elif set(digitMap[1]).issubset(set(digit)):
                    digitMap[3] = digit
                else:
                    digitMap[2] = digit

        number = []
        # Decode the outputs
        for digit in outputs[i]:
            for key, value in digitMap.items():
                if set(digit) == set(value):
                    number.append(str(key))
        
        number = int(''.join(number))
        totalSum += number
    
    return totalSum
            
print(f'Answers to part 2: {part2()}')