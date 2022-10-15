#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Sweep in from both sides
Find leftmost 1 and rightmost 0
While leftmost 1 to left of rightmost 0
    toss the 1 onto that 0 and discard it
Repeat till leftmost 1 to right of rightmost 0
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    L = 0
    R = n-1
    ans = 0
    while L < R:
        while L <= n-1 and a[L] != 1:
            L += 1
        while R >= 0 and a[R] != 0:
            R -= 1
        if R > L:
            ans += 1
            L += 1
            R -= 1
    
    print(ans)
