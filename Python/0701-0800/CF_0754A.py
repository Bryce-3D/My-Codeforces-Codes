#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
l = [int(i) for i in input().split()]

s = sum(l)
if s != 0:
	print('YES')
	print(1)
	print(1,n)
else:
	possible = False

	for i in range(n):
		if l[i] != 0:
			possible = True
			print('YES')
			print(2)
			print(1,i+1)
			print(i+2,n)
			break

	if not possible:
		print('NO')
