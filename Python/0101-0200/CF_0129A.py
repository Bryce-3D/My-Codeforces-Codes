#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
l = [int(i) for i in input().split()]

odd = 0
for i in l:
	if i%2 == 1:
		odd += 1

if odd%2 == 1:
	print(odd)
else:
	print(n-odd)
