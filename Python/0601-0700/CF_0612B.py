#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#For convenience, subtract the fragment number by 1 for all fragments

n = int(input())

#l_sec[i] is the fragment at sector i
l_sec = [int(i)-1 for i in input().split()]

#l_frag[i] is the sector of fragment i
l_frag = [0 for i in range(n)]
for i in range(n):
	l_frag[l_sec[i]] = i #Sector i has frag l_sec[i] -> frag at l_sec[i] at sector i

#Total distance needed
ans = 0
for i in range(n-1):
	ans += abs(l_frag[i+1]-l_frag[i])

print(ans)
