#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
m = Homura[1]

ans = 0

for Mahou_Shoujo_Madoka_Magica in range(n):
	floor = [int(i) for i in input().split()]
	for i in range(m):
		ans += (floor[2*i] + floor[2*i+1]) > 0

print(ans)
