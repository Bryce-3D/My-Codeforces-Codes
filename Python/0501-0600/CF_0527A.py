#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
a = Homura[0]
b = Homura[1]

ans = 0
while a*b > 0:
	if a >= b:
		ans += a//b
		a = a%b
	else:
		ans += b//a
		b = b%a

print(ans)
