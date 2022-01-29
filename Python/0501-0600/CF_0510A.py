#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]

e = '#'*n
o1 = '.'*(n-1)+'#'
o2 = '#'+'.'*(n-1)

for i in range(m):
	if i%2 == 0:
		print(e)
	elif i%4 == 1:
		print(o1)
	elif i%4 == 3:
		print(o2)
