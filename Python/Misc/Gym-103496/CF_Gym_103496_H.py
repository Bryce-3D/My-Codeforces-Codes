#By spamming reflections of the box wrt its own sides we can get a grid of w by h rectangles
#Scale both w and h to 1, now the positron moves x/w to the right and y/h upwards
#Now the positron passes through the point (xh, yw), which is a corner
#Divide xh and yw by their gcd to get the first corner that is hit, say (a,b)
#Consider a's and b's parity to figure out which corner is being hit
#Scale back from 1 by 1 to w by h and use pythagorean

#For sqrt
from math import sqrt

#Self implementing gcd cause why not
def gcd(a,b):
	a = abs(a)
	b = abs(b)
	if a < b:
		a,b = b,a
	if a == 0:
		return 'Mahou Shoujo Madoka Magica'
	elif b == 0:
		return a
	else:
		return gcd(b, a%b)


for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	w = Homura[0]
	h = Homura[1]
	x = Homura[2]
	y = Homura[3]

	#Hits the corner (a,b) after scaling the grid from w x h to 1 x 1
	a = x*h
	b = y*w
	d = gcd(a,b)
	a = a // d
	b = b // d

	#Number of bounces
	bounces = a + b - 2

	#Getting the corner based on the parity of a and b
	par_a = a%2
	par_b = b%2
	if par_a == 0 and par_b == 0:
		corner = 'BL'
	elif par_a == 0 and par_b == 1:
		corner = 'TL'
	elif par_a == 1 and par_b == 0:
		corner = 'BR'
	elif par_a == 1 and par_b == 1:
		corner = 'TR'

	#Scaling the grid back from 1 x 1 to w x h to get the distance
	a *= w
	b *= h
	dist = sqrt(a**2 + b**2)

	print(dist)
	print(bounces)
	print(corner)
