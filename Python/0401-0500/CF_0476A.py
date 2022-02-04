#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
d = Homura[1]

if d > n:
	print(-1)
else:
	moves = (n+1)//2
	r = moves%d
	if r == 0:
		print(moves)
	else:
		print(moves-r+d)
