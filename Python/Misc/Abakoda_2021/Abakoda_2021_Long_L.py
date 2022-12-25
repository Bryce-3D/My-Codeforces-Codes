#The lazer can be described using 3 values: drt (direction), row (row no), col (column no)
#drt is U, D, L, R for up, down, left, right
#Locations will be represented as [row no, col no]
#Let the corners have coordinates as shown
	#[ 0 , 0 ]   [ 0 ,c-1]
	#
	#[r-1, 0 ]   [r-1,c-1]

#For example, a lazer that is coming in from L1 can be represented with
	#dir = 'R'
	#loc = [0,0]
#If it then hits a \ barrier there, it will become
	#dir = 'D'
	#loc = [1,0]
#since it will deflect it downwards towards the cell in the row below

#Fast input
import sys
input = sys.stdin.readline



Kumiko = [int(i) for i in input().split()]
r = Kumiko[0] #Number of rows
c = Kumiko[1] #Number of columns

#The ith element of the maze will be the ith row
#maze[r][c] contains the element in the rth row and cth column,
#where rows and columns are zero indexed
maze =[]
for Mahou_Shoujo_Madoka_Magica in range(r):
	maze.append(input())



q = int(input()) #Number of queries
#Loop through q queries
for Mahou_Shoujo_Madoka_Magica in range(q):
	#Checking what the starting state of the lazer beam is
	Homura = input().split()
	Homura[1] = int(Homura[1]) - 1 #Making the entry row/col number an integer and zero indexed
	#drt = direction, row = row number, col = column number
	if Homura[0] == 'L': 
		drt = 'R'
		row = Homura[1]
		col = 0
	elif Homura[0] == 'R':
		drt = 'L'
		row = Homura[1]
		col = c-1
		loc = [Homura[1], c-1]
	elif Homura[0] == 'T':
		drt = 'D'
		row = 0
		col = Homura[1]
	elif Homura[0] == 'B':
		drt = 'U'
		row = r-1
		col = Homura[1]

	#Check where the light goes while it's inside the maze, aka 0 <= row <= r-1 and 0 <= col <= c-1
	while 0 <= row <= r-1 and 0 <= col <= c-1:
		if maze[row][col] == '/':
			if drt == 'U':
				drt = 'R'
				col += 1
			elif drt == 'D':
				drt = 'L'
				col -= 1
			elif drt == 'L':
				drt = 'D'
				row += 1
			elif drt == 'R':
				drt = 'U'
				row -= 1
		elif maze[row][col] == '\\':
			if drt == 'U':
				drt = 'L'
				col -= 1
			elif drt == 'D':
				drt = 'R'
				col += 1
			elif drt == 'L':
				drt = 'U'
				row -= 1
			elif drt == 'R':
				drt = 'D'
				row += 1

	#Checking where the lazer went out
	if row < 0:
		print(f'T {col+1}')
	elif row > r-1:
		print(f'B {col+1}')
	elif col < 0:
		print(f'L {row+1}')
	elif col > c-1:
		print(f'R {row+1}')
