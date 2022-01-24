#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
cost = 0
price = 100

for i in range(n):
	Homura = [int(i) for i in input().split()]
	price = min(price, Homura[1])
	cost += Homura[0] * price

print(cost)
