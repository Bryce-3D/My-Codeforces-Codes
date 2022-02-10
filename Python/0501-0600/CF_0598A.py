#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Mahou_Shujo_Madoka_Magica in range(int(input())):
	n = int(input())
	total = n*(n+1)//2

	#Highest power of 2 less than or equal to n
	max_pow_2 = 1
	while max_pow_2 <= n:
		max_pow_2 *= 2
	max_pow_2 //= 2

	remove = 2 * max_pow_2 - 1

	print(total - 2 * remove)
