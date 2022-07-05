#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
The 0s need to be in the same spot (take l=r=index of 0 in a).
This immediately satisfies the condition for any subarray not 
including 0 since the MEX is 0.

The 1s also need to be in the same spot (take {l,r} = {i_0,i_1} 
vs {l,r} = {i_0,i_1+-1} (aka exclude the 1)


Place 0 -> Only subarrays involving 0 are relevant
Place 1 -> Only subarrays involving 0,1 are relevant
Place 2 -> Only subarrays involving 0,1,2 are relevant
...
Place 0,1,...,i -> Only subarrays involving 0,1,...,i are relevant


Let S_i denote the smallest interval containing all numbers <= i in a.
    i+1 within S_i -> i+1 must be within S_i, but precise location doesn't matter
    i+1 not within S_i -> i+1 must be at the exact same location
INDUCT THIS UPWARDS

Have an array called ind where
    ind[i] = index of i in a
Have L and R to keep track of S_i, grow if needed

At each step, if i+1 within S_i = [L,R] (interval), then
    i+1 numbers already previously placed
    R-L+1 numbers in S_i
    (R-L+1)-(i+1) = R-L-i spots left to put i+1
'''

#Return total mod p
p = 10**9+7

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #ind[a_i] returns i, the index of a_i
    ind = [-1 for i in range(n)]
    for i in range(n):
        a_i = a[i]
        ind[a_i] = i
    
    #Place 0 and initialize stuff
    L = ind[0]   #Left border of S_i (inclusive, 0-indexed)
    R = ind[0]   #Right border of S_i (inclusive, 0-indexed)
    ans = 1
    for i in range(n-1):   #Consider the number i+1
        index = ind[i+1]

        if index < L:     #If extend left
            L = index
        elif index > R:   #If extend right
            R = index
        else:             #If it's inside
            ans *= R-L-i
            ans %= p
    
    print(ans)
