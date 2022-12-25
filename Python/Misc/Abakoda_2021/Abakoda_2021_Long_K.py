#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Thought process to solve the math part of the problem
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Designate U as the a-vector, RD as the b-vector, and the starting city as the origin
#Every movement can be represented in terms of a and/or b
	# U  = a
	# D  = -a
	# RD = b
	# LU = -b
	# RU = a+b
	# LD = -a-b
#As a result, each player's final position can be represented ia+jb for some integers i,j
#If two players are at ia + jb and xa + yb, the vector from the first to the second is (x-i)a + (y-j)b
#If the vector from point A to point B is ia + jb, then the number of moves to get from A to B is
	# max(|a|, |b|)    if ab >= 0
	# a + b            if ab <= 0

#The position at ia + jb wrt the starting town will be represented as [i,j]





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Processing and storing information about the players
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Direction dictionary: contains the corresponding vector for each possible movement
dir_dir = {'U':[1,0], 'D':[-1,0], 'RD':[0,1], 'LU':[0,-1], 'RU':[1,1], 'LD':[-1,-1]}

n = int(input()) #Number of players
names = []       #Name of each of the players
positions = []   #Corresponding final positions of each of the players

#Adding each player into names and positions
for i in range(n):
	names.append(input())   #Add the new name to the list

	m = int(input())        #Number of movements of the player
	pos = [0,0]             #Current position of the player

	#Edit the current position for each of the m movements
	for i in range(m):
		Homura = input().split()
		direction = Homura[0]
		dist = int(Homura[1])

		#Vector that describes the current movement
		movement = dir_dir[direction]
		movement = [dist * i for i in movement]

		pos = [pos[0] + movement[0], pos[1] + movement[1]]

	positions.append(pos)     #Add the final position of the player to the list





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Answering the queries
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

q = int(input()) #Number of queries

#Answering each query
for i in range(q):
	Kumiko = input().split()
	P1 = Kumiko[0] #Player 1 to be considered
	P2 = Kumiko[1] #Player 2 to be considered

	i = names.index(P1)
	j = names.index(P2)

	pos1 = positions[i]
	pos2 = positions[j]

	#The path is the vector [path_a, path_b]
	path_a = pos2[0] - pos1[0]
	path_b = pos2[1] - pos1[1]

	if path_a * path_b >= 0:
		print(max( abs(path_a), abs(path_b) ))
	else:
		print(abs(path_a) + abs(path_b))
