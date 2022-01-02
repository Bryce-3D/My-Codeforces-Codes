Homura = [int(i) for i in input().split()]
n = Homura[0]
m = Homura[1]
l_t = []
for i in range(n):
	Madoka = [int(i) for i in input().split()]
	l_t.append(Madoka[0]*Madoka[1])
l_m = [int(i) for i in input().split()]

song = 0
time = 0

for i in range(m):
	while time < l_m[i]:
		time += l_t[song]
		song += 1
	print(song)
