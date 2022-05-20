#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
For each row, sort it.
Note that this sorted order is the unique possible way to order this row 
such that it's nondecreasing.
Check for differences between the sorted row and the og row.

No difference -> continue to next row
2 differences -> These 2 corresponding columns MUST be swapped, check if 
    the grid as a whole works in this case. 
    Yes -> print the cols; No -> print -1
>2 differences -> Impossible, print -1
*1 difference is not possible, otherwise the two rows have diff elements
'''

#Checks if an r by c grid is good after swapping columns x and y
#x and y are 0-indexed here
def check(grid, r, c, x, y):
    good = True
    for i in range(r):   #For each row
        #Make a copy and perform the swap
        swap_row_i = [j for j in grid[i]]
        swap_row_i[x], swap_row_i[y] = swap_row_i[y], swap_row_i[x]

        #Check for each pair of adjacent columns
        for j in range(c-1):   
            if swap_row_i[j] > swap_row_i[j+1]:   #If it fails, record and break
                good = False
                break
        
        #If it failed, break
        if not good:
            break
    return good

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    r = Kumi[0]
    c = Kumi[1]
    grid = []   #grid[i][j] returns the element in the ith row and jth col
    for i in range(r):
        grid.append([int(i) for i in input().split()])
    
    to_swap = [1,1]   #Columns to swap, change to -1 if a row has >2 differences
    for i in range(r):
        sorted_row_i = [j for j in grid[i]]
        sorted_row_i.sort()

        diff = []   #Indices with diff numbers
        for j in range(c):
            if grid[i][j] != sorted_row_i[j]:   #If diff numbers
                diff.append(j)   #Record the index
        
        if len(diff) > 2:   #Row cannot be sorted
            to_swap = -1
            break
        elif len(diff) == 2:   #Columns to swap are fixed
            to_swap = diff
            break
        #Else, continue checking
    
    if to_swap == -1:   #If a row is dead
        print(-1)
    elif to_swap[0] == to_swap[1]:   #All the rows are already sorted
        print(1,1)
    else:   #Check if it works 
        if check(grid, r, c, to_swap[0], to_swap[1]):
            print(to_swap[0]+1, to_swap[1]+1)   #Change from 0-index to 1-index
        else:
            print(-1)
