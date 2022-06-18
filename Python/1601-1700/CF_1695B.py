#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Even -> They never interact
     -> The one with less total stones loses
        (If equal, first guy loses)

Odd -> Kill the first pile and P1 wins after the first cycle
WAIT NO LOOK AT MIN NOT SUM FFS
'''

for Homu in range(int(input())):
    n = int(input())
    piles = [int(i) for i in input().split()]

    if n%2 == 1:
        print('Mike')
    else:
        #Find first instance of smallest value
        min_M = piles[0]
        min_J = piles[1]
        i_min_M = 0
        i_min_J = 1

        for i in range(n//2):
            if piles[2*i] < min_M:
                min_M = piles[2*i]
                i_min_M = 2*i
            if piles[2*i+1] < min_J:
                min_J = piles[2*i+1]
                i_min_J = 2*i+1
        
        if min_M > min_J:
            print('Mike')
        elif min_M < min_J:
            print('Joe')
        elif i_min_M > i_min_J:
            print('Mike')
        else:
            print('Joe')
