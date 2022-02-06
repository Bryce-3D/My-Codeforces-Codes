#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#gets gcd of 2 positive integers
def gcd(a,b):
	if a < b:
		a,b = b,a
	while b != 0:
		a,b = b,a%b
	return a

n = int(input())
l = [int(i) for i in input().split()]

gcd_l = l[0]
for i in range(1,n):
	gcd_l = gcd(gcd_l, l[i])

print(gcd_l*n)
