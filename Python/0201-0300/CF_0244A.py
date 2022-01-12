#For fast I/O
import sys
input = sys.stdin.readline

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]
l = [int(i) for i in input().split()]

etc = [int(i) for i in range(1,n*k+1)]
for i in l:
	etc.remove(i)

for i in range(k):
	l_i = [l[i]]
	for j in range(n-1):
		l_i.append(etc[i*(n-1)+j])
	l_i = [str(Madoka) for Madoka in l_i]
	print(' '.join(l_i))
