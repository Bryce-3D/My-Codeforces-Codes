#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    prod = 1
    for k in a:
        prod *= k
    ans = 2022*(prod + n - 1)
    print(ans)
