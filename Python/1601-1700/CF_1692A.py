#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    a,b,c,d = [int(i) for i in input().split()]
    ans = 0
    if b > a:
        ans += 1
    if c > a:
        ans += 1
    if d > a:
        ans += 1
    print(ans)
