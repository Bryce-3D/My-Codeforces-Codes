#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
AND z just weakens z, find best a_i AND z with and that's it.
'''

for Homu in range(int(input())):
    n,z = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    ans = 0
    for i in range(n):
        next = a[i] | z
        ans = max(ans, next)
    
    print(ans)
