#I couldn't figure out the coding, but quickly saw hwere the answer should be.
#This python code from the solved thread by user onursina (page 8) seemed quite logical.
#Will research into itertools library


import itertools

a = []
a.append(list(map(int,"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split())))
...
a.append(list(map(int,"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split())))

high = []
for x, y in itertools.product(range(17), range(17)): #right diagonal
    high.append(a[y][x]*a[y+1][x+1]*a[y+2][x+2]*a[y+3][x+3])
for x, y in itertools.product(range(3,20), range(17)): #left diagonal
    high.append(a[y][x]*a[y+1][x-1]*a[y+2][x-2]*a[y+3][x-3])
for x, y in itertools.product(range(20), range(17)): #up
    high.append(a[y][x]*a[y+1][x]*a[y+2][x]*a[y+3][x])
for x, y in itertools.product(range(17), range(20)): #adjacent
    high.append(a[y][x]*a[y][x+1]*a[y][x+2]*a[y][x+3])

print(max(high))
