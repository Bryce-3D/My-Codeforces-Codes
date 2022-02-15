#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
k = Homura[0]
d = Homura[1]

if d != 0:
	print(str(d) + (k-1) * '0')
elif k == 1:
	print(0)
else:
	print('No solution')
