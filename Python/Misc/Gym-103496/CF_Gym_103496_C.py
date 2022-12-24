Homura = [int(i) for i in input().split()]
n = Homura[0]
h = Homura[1]
k = Homura[2]

r = 0

for i in range(n):
	nut = [int(i) for i in input().split()]
	x = nut[0]
	y = nut[1]
	dist = ((x - h) ** 2 + (y - k) ** 2) ** 0.5
	r = max(r, dist)

print(2 * r)
