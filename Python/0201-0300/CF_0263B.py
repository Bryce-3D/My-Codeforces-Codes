#For fast I/O
import sys
input = sys.stdin.readline

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]
l = sorted([int(i) for i in input().split()])

if k > n:
	print(-1)
else:
	print(l[n-k],l[n-k])
