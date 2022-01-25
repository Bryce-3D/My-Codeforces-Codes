#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]
no_color = True
count = 0

for i in range(m):
	s = input()
	if 'C' in s or 'Y' in s or 'M' in s:
		no_color = False
		break

if no_color:
	print('#Black&White')
else:
	print('#Color')
