#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
TC3 kinda gets stuck on the smallest element
Observation:
    A smallest element ALWAYS falls through the entire array to the front

This means that once a smallest element is in front, you are stuck in 
an infinite loop of tossing it back to the front.
Therefore, everything behind the first copy of the minimum value in the 
array must be sorted for it to be possible.
On the other hand, the nature of the algorithm is self-sorting, so 
if that is the case, it will work out

Possible iff everything behind first copy of min is sorted
Given that it's possible
Number of moves = Number of elements in front of first copy of min
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    m = min(a)         #Min element of a
    ind = a.index(m)   #Index of first instance of m in a

    #Check if it is possible
    possible = True
    for i in range(ind,n-1):
        if a[i] > a[i+1]:
            possible = False
            break
    
    if possible:
        print(ind)
    else:
        print(-1)
