#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())

    if n == 3:
        print(-1)
    else:
        k = n//2
        ans = [(k+i)%n + 1 for i in range(n)]
        ans = ' '.join([str(i) for i in ans])
        print(ans)
