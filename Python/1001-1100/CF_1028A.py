#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]

#ith element is the ith row
grid = []
for i in range(m):
	grid.append(input())

i = 0

while i < m:
	if 'B' in grid[i]:
		top_row = i
		break
	i += 1

bottom_row = m-1
while i < m:
	if 'B' not in grid[i]:
		bottom_row = i-1
		break
	i += 1

left_col = grid[top_row].index('B')
s = bottom_row - top_row

r = (top_row + bottom_row)//2 + 1
c = left_col + s//2 + 1
print(r,c)
