#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Number of secretaries
n = int(input())
#Call id/not-in-a-call indicator list
l = [int(i) for i in input().split()]

#Index for scanning
i = 0
#Number of calls between secretaries
calls = 0
possible = True

while possible and i < n:
	c = l.count(l[i])
	if l[i] == 0:
		#If there's no call, then nothing to do
		pass
	elif c == 2:
		#If there are two instances, it's a secretary call
		calls += 1
	elif c > 2:
		#If there are more than two, it's impossible
		possible = False
		break
	i += 1

if possible:
	#Divide by 2 due to double counting
	calls //= 2
	print(calls)
else:
	print(-1)
