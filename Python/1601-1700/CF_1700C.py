#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Consider adjacent elements a,b. WLOG a >= b.

Only way to make equal is have a's side decrease by 
a-b times more than b.
Do this to every pair.
Afterwards all adjacent equal, so all equal.

Remaining question: How to figure out the total reduction?
Since all the same already just need to track one term's value.
'''

for Homu in range(int(input())):
    n = int(input())
    trees = [int(i) for i in input().split()]

    #Track the changes to the first tree
    tree_0 = trees[0]
    #Track number of operations of type 1 or 2 done
    equalizations = 0

    #Equalize every adjacent pair
    for i in range(n-1):
        L = trees[i]
        R = trees[i+1]
        if L > R:     #If left is bigger
            equalizations += L-R   #Equalize
            tree_0 -= L-R          #Left end gets decreased
        elif L < R:   #Elif right is bigger
            equalizations += R-L   #Equalize
        #Elif equal, do nothing
    
    #Number of moves to make all tree_0 to 0
    normalizations = abs(tree_0)

    #Print the ans
    ans = equalizations + normalizations
    print(ans)
    #print(equalizations, normalizations)
