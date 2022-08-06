#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    seen = set()
    l = 0

    while l < n:
        if a[-l-1] not in seen:
            seen.add(a[-l-1])
            l += 1
        else:
            break
    
    print(n-l)
