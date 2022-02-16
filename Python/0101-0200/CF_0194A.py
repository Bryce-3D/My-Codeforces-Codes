#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]

#Subtract all scores by 2, range of each score is now [0,3]
k -= 2*n

if k >= n:
	print(0)
else:
	print(n-k)
