#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    r = Kumi[0]
    c = Kumi[1]

    min_cols = []
    for i in range(r):
        next_row = input()
        if 'R' in next_row:
            min_cols.append(next_row.index('R'))
        else:
            min_cols.append(-1)

    #Find the col of the topmost robot at the left
    corner_col = -1
    i = 0
    while corner_col == -1:
        corner_col = min_cols[i]
        i += 1
    
    #Check if all robots lie on or to the right of corner_col
    possible = True
    for i in range(r):
        if min_cols[i] != -1 and min_cols[i] < corner_col:
            possible = False
            break
    
    if possible:
        print('YES')
    else:
        print('NO')
