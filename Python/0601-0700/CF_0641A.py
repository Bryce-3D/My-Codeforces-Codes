#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
direction = input()
dist = [int(i) for i in input().split()]
visited = set()

cycle = False

i = 0
while i >= 0 and i < n:
	visited.add(i)

	if direction[i] == '<':
		i -= dist[i]
	elif direction[i] == '>':
		i += dist[i]

	if i in visited:
		cycle = True
		break
	
if cycle:
	print('INFINITE')
else:
	print('FINITE')
