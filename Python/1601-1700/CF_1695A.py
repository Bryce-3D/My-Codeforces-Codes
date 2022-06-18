#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Either include max or not.
Therefore must ensure contain max.
'''

for Homu in range(int(input())):
    R,C = [int(i) for i in input().split()]

    #grid[r][c] returns the number at (r,c) (0-indexed)
    grid = []
    for i in range(R):
        next_row = [int(i) for i in input().split()]
        grid.append(next_row)
    
    #Max number of the grid
    Max = max([max(row) for row in grid])

    #Find the coord of the max
    for i in range(R):
        for j in range(C):
            if grid[i][j] == Max:
                r = i
                c = j

    #Find the min size to ensure the max is contained
    min_r = max(r+1, R-r)
    min_c = max(c+1, C-c)
    area = min_r * min_c
    print(area)
