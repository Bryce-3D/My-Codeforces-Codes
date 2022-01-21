#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
ans = 6 * n * (n+1) // 2 + 1
print(ans)
