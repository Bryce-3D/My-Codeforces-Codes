#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Due to the given constraints, a linear search should be sufficient
#Learn how to prime factorize with code sometime in the future

n = int(input())
ans = 0
for i in range(2, n+1):
	if n%i == 0:
		ans += 1
print(ans)
