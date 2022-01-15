#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]

#lengths[i] contains the number of passwords of length i+1
lengths = [0 for i in range(100)]
for i in range(n):
	lengths[len(input())-1] += 1
#l is the length of the correct password
l = len(input())

#m is the minimum number of passwords needed
#M is the maximum number of passwords needed
M = 0
for i in range(l):
	M += lengths[i] #All passwords of length <= l
m = M - lengths[l-1] + 1

#w_m is the number of waits for m attempts
#w_M is the number of waits for M attempts
w_m = (m-1)//k
w_M = (M-1)//k

#t_m is the time taken for m attempts
#t_M is the time taken for M attempts
t_m = m + 5 * w_m
t_M = M + 5 * w_M

print(t_m, t_M)
