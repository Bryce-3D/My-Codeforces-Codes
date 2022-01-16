#Idea
#Convert req to the total score required
#For each test, just toss the number of marks that can be obtained into
#a total score and toss the number of bonus marks attainable into the
#value of key i in a dictionary where i is the number of essays required
#per bonus mark

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
n = Homura[0]
r = Homura[1]
avg = Homura[2]

total = 0
desired = avg * n
available = {}
for i in range(1,10**6+1):
	available[i] = 0

for i in range(n):
	Kumiko = [int(i) for i in input().split()]
	total += Kumiko[0]
	available[Kumiko[1]] += r - Kumiko[0]

req = desired - total

essays = 0
workload = 1
while req > 0:
	if req >= available[workload]:
		req -= available[workload]
		essays += workload * available[workload]
		workload += 1
	else:
		essays += req * workload
		break

print(essays)
