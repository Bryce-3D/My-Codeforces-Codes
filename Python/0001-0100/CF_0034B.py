Homura = [int(i) for i in input().split()]
n = Homura[0]
m = Homura[1]
prices = sorted([int(i) for i in input().split()])
profit = 0
tracer = 0
while tracer < m and prices[tracer] < 0:
	profit -= prices[tracer]
	tracer += 1
print(profit)
