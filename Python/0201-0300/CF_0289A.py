#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]

total = 0
for i in range(n):
	Kumiko = [int(i) for i in input().split()]
	total += Kumiko[1] - Kumiko[0] + 1

r = total%k
if r == 0:
	print(0)
else:
	print(k-r)
