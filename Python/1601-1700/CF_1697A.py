#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n,m = [int(i) for i in input().split()]
    dist = [int(i) for i in input().split()]

    req = sum(dist)-m
    ans = max(req,0)
    print(ans)
