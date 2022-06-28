#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Note that you can't have 2 consecutive tall blocks.

k = 1 -> can force 2nd, 4th, ... to all be too tall.

k >= 2 -> doesn't help
I think
'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    if k == 1:
        print((n-1)//2)
    else:
        ans = 0
        for i in range(1,n-1):
            if a[i] > a[i-1]+a[i+1]:
                ans += 1
        print(ans)
