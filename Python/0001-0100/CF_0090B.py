#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]

grid = []
for i in range(m):
	grid.append(input())

ans = ''
for i in range(m):
	for j in range(n):
		#Number of instances in the row
		row = grid[i].count(grid[i][j])
		#Number of instances in the column
		col = 0
		for k in range(m):
			col += grid[k][j] == grid[i][j]

		if row == 1 and col == 1:
			ans += grid[i][j]

print(ans)
