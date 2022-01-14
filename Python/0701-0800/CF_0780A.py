#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
order = [int(i)-1 for i in input().split()] #Order of socks taken
count = [0 for i in range(n)]               #count[i-1] copies of sock i taken so far
table = 0                                   #Number of socks on the table
M_table = 0                                 #Maximum number of socks on the table

for i in range(2*n):
	sock = order[i]
	if count[sock] == 0:
		table += 1
		count[sock] += 1
		M_table = max(M_table,table)
	elif count[sock] == 1:
		table -= 1
		count[sock] += 1

print(M_table)
