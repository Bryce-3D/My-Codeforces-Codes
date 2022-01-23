#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]

road = input()
streak = 0
possible = True

for i in range(n):
	if road[i] == '.':
		streak = 0
	elif road[i] == '#':
		streak += 1
		if streak == k:
			possible = False
			break

if possible:
	print('YES')
else:
	print('NO')
