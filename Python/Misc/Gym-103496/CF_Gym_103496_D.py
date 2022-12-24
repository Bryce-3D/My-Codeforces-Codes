n = int(input())
shy = sorted([int(i) for i in input().split()])

stop = n
for i in range(n):
	if shy[i] > i:
		stop = i
		break

print(stop)
