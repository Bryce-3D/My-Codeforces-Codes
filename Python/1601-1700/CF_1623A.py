#Let the row i be the line x=i and column j be the line y=j
#(r/d)(x/y) means (robot/dirt)'s (x/y)-coordinate

#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	m = Homura[0]
	n = Homura[1]
	rx = Homura[2]
	ry = Homura[3]
	dx = Homura[4]
	dy = Homura[5]

	#How long it takes the robot to reach the same x-coordinate as the dirt
	if dx >= rx:
		sx = dx-rx
	else:
		sx = 2*m-rx-dx

	#How long it takes the robot to reach the same y-coordinate as the dirt
	if dy >= ry:
		sy = dy-ry
	else:
		sy = 2*n-ry-dy

	print(min(sx,sy))
