#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Ans is at most 2, mexing the entire array either yields a 
constant 0 or constant nonzero array. In the latter, just 
mex the whole thing again.

0 mexes -> all 0
1 mex -> ?
1 mex possible iff only 1 contiguous block of nonzero
Can check by tracking all indices of nonzero elements and seeing 
if they're consecutive.
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    nonzero_ind = []
    for i in range(n):
        if a[i] != 0:
            nonzero_ind.append(i)
    
    if len(nonzero_ind) == 0:
        print(0)
    else:
        one_possible = True
        for i in range(len(nonzero_ind)-1):
            if nonzero_ind[i+1] != nonzero_ind[i] + 1:
                one_possible = False
                break
        
        if one_possible:
            print(1)
        else:
            print(2)
