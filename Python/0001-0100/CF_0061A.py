#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = input()
Madoka = input()
l = len(Homura)
ans = ''

for i in range(l):
	a = int(Homura[i])
	b = int(Madoka[i])
	c = a^b
	ans += str(c)

print(ans)
