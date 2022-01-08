#Idea:
#Obviously, we just need to spam the maximum score n until the average is high enough
#a mark of k-i will need 2i-1 k's to raise the average to k-0.5

#For fast I/O
import sys
input = sys.stdin.readline

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]
marks = [int(i) for i in input().split()]

ans = 0
for i in marks:
	i = k-i
	ans += 2*i-1

print(max(ans,0))
