#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Increase the number i by (n+1)-i
Anything to it's left is at most n, so no inversions with stuff to its left
Other operations can't harm it
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i)-1 for i in input().split()]

    #index[i] returns the index of element i in a (1-indexed)
    index = [-1 for i in range(n)]
    for i in range(n):
        index[a[i]] = i+1
    
    #k at index i -> must do the (n-k)th op there
    ans = [str(i) for i in index[::-1]]
    ans = ' '.join(ans)
    print(ans)
