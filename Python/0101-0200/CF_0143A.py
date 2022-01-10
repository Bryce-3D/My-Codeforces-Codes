#Answer is arranged as 
# a b
# c d

#For fast I/O
import sys
input = sys.stdin.readline

r = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]

if r[0]+r[1] != c[0]+c[1] or r[0]+r[1] != d[0]+d[1]: #Solution DNE
	print(-1)
elif ( r[0]+c[0]-d[1] )%2 != 0: #Non-integer values
	print(-1)
else:
	a = (r[0]+c[0]-d[1])//2
	b = r[0]-a
	c = c[0]-a
	d = d[0]-a
	
	if len({a,b,c,d}) != 4: #There is a repeated element
		print(-1)
	elif min(a,b,c,d) < 1 or max(a,b,c,d) > 9: #Out of range
		print(-1)
	else: #Works
		print(a,b)
		print(c,d)
