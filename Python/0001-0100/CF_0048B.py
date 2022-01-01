Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]

garden = []
for i in range(m):
	garden.append([int(i) for i in input().split()])

Madoka = [int(i) for i in input().split()]
a = Madoka[0]
b = Madoka[1]

ans = a*b

for i in range(m+1-a):
	for j in range(n+1-b):
		trees = 0
		for x in range(a):
			for y in range(b):
				trees += garden[i+x][j+y]
		ans = min(ans,trees)

for i in range(m+1-b):
	for j in range(n+1-a):
		trees = 0
		for x in range(b):
			for y in range(a):
				trees += garden[i+x][j+y]
		ans = min(ans,trees)

print(ans)
