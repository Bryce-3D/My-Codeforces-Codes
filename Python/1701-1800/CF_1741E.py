#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
block = contiguous subarray where one of the ends 
        is equal to the number of other elements
count = number at the end of the block that indicates 
        how many other elements are in the block
R-block = block with count at the right
L-block = block with count at the left


Probably dp?

Since hard to check for the rightmost block if the count 
is at the left end rather than the right end, maybe try 
building it up during the dp?
Also dp is usually bottom up not top down wtf am I doing

possible[i] = True iff it's possible for a[0:i] (first i elements)
Initialize all to false
If something gets flipped to True, check a[i], then check that 
the next block to the right with count a[i] doesn't fly out 
and set that to True also
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #possible[i] = True iff possible for a[0:i]
    possible = [False for i in range(n+1)]
    possible[0] = True   #Vacuously works

    for i in range(n):
        #Extending a[0:i] using an L-block at the right end
        if possible[i]:
            l_L = a[i]+1   #Length of the next L-block
            l_ext = i+l_L   #Length of prefix extended with next L-block
            if l_ext <= n:
                possible[l_ext] = True
        
        #Building a[0:i+1] using an R-block at the right end
        l_R = a[i]+1   #Length of the last R-block
        rem = (i+1)-l_R   #Length after removing the last R-block
        if rem >= 0 and possible[rem]:
            possible[i+1] = True
        
    if possible[n]:
        print('YeS')
    else:
        print('nO')
