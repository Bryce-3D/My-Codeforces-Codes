#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
prev = 4126
sure_rated = False
maybe_unrated = False

for i in range(n):
	Homura = [int(i) for i in input().split()]
	if Homura[0] != Homura[1]:
		sure_rated = True
		break
	elif Homura[0] > prev:
		maybe_unrated = True
	prev = Homura[0]

if sure_rated:
	print('rated')
elif maybe_unrated:
	print('unrated')
else:
	print('maybe')
