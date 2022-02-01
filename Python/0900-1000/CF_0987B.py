#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

Homura = [int(i) for i in input().split()]
x = Homura[0]
y = Homura[1]

def compare(a,b):
	if a < b:
		print('<')
	elif a == b:
		print('=')
	elif a > b:
		print('>')

if min(x,y) > 2:
	compare (y,x)
elif min(x,y) == 1:
	compare(x,y)
elif max(x,y) > 4:
	compare(y,x)
else:
	compare(x**y,y**x)
