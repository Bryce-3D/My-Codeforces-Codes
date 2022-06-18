#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#for garbage collect

'''Idea
First of all, m+n should obv be odd

dp all possible values but too many?
WAIT r,c BOUNDED CAN ELIMINATE TOO BIG VALUES(?)
Also actl at most 2000 values per node now that 
I think of it.

2000 * 10^6 > 10^8 which is too big tho
Need to bound by 
    "x units away" -> "|curr sum| < x"

Idea after getting a hint:
Can always +-2 by bending corners, just need to track max/min 
and use IVT
'''

for Homu in range(int(input())):
    R,C = [int(i) for i in input().split()]

    #0-indexed
    grid = []
    for i in range(R):
        grid.append([int(i) for i in input().split()])
    
    mins = [[0 for i in range(C)] for i in range(R)]
    maxs = [[0 for i in range(C)] for i in range(R)]

    #Set the top row
    curr_sum = 0
    for c in range(C):
        curr_sum += grid[0][c]
        mins[0][c] = curr_sum
        maxs[0][c] = curr_sum
    
    #Set the left column
    curr_sum = 0
    for r in range(R):
        curr_sum += grid[r][0]
        mins[r][0] = curr_sum
        maxs[r][0] = curr_sum
    
    #Set the rest
    for r in range(1,R):
        for c in range(1,C):
            mins[r][c] = min(mins[r-1][c],mins[r][c-1]) + grid[r][c]
            maxs[r][c] = max(maxs[r-1][c],maxs[r][c-1]) + grid[r][c]
    
    #Check if 0 in range
    #Also check parity
    if (R+C)%2 == 0:
        print('nO')
    elif 0 >= mins[-1][-1] and 0 <= maxs[-1][-1]:
        print('YeS')
    else:
        print('nO')
