#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	s = input()
	l = sorted(s)
	ans = ''
	for i in l:
		ans += i
	print(ans)
