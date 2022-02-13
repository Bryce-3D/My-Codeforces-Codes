#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

grid = [input(), input(), input()]

if grid[0][0] != grid[2][2]:
	print('NO')
elif grid[0][1] != grid[2][1]:
	print('NO')
elif grid[0][2] != grid[2][0]:
	print('NO')
elif grid[1][2] != grid[1][0]:
	print('NO')
else:
	print('YES')
