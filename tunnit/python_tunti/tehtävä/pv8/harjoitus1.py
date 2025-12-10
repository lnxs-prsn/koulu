steps = [48, -24, -10, 16, -11, 23, -1, -28, -5, 1, 25, -1, -32, 24, -18, -5, 36, -21, -1, 19,
14, -13, 1, 7, -12, 15, -21, -21, 40, -16, -26, 40, -28, 31, -34, 8, 7, -6, -11, -6, 24, -22,
34, -22, 13, -8, 16, -28, 11, 28]

""""
pos = 0


while True:
    steps[pos]
    pos -= steps[pos]
    if pos < 0:
        break"""

with open('harjoitus2.txt', 'r') as file:
    lines = file.readlines()
    for x in range(len(lines)):
        print(lines[x][x], end='')


""" for line in lines:
        print(line[4])"""
        
