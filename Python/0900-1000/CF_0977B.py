#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = input()

l_2gram = []
l_count = []

for i in range(n):
	gram = s[i:i+2]
	if gram in l_2gram:
		i = l_2gram.index(gram)
		l_count[i] += 1
	else:
		l_2gram.append(gram)
		l_count.append(1)

M = max(l_count)
i = l_count.index(M)
print(l_2gram[i])
