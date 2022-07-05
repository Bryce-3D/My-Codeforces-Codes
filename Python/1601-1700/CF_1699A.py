#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())

    if n%2 == 1:
        print(-1)
    else:
        print(n//2,n//2,0)
