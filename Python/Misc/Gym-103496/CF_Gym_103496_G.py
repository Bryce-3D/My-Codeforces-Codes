n = int(input())
hallway = input()

#List of event flags and their locations in ascending order
#Each element is of the form [position, person]
flags = []
for i in range(n):
	if hallway[i] == 'A':
		flags.append([i, 'A'])
	elif hallway[i] == 'C':
		flags.append([i, 'C'])
l = len(flags) #Number of event flags

dist_A = [] #ith element will be the distance from position i to the nearest Alexa event flag
dist_C = [] #ith element will be the distance from position i to the nearest Cecille event flag

#Corner case of no event flags
if l == 0:
	dist_A = [-1 for i in range(n)]
	dist_C = [-1 for i in range(n)]

#Normal case
else:
	#let f_i refer to the position of the ith flag for this comment, where the indexing starts from 0
	#Intervals to be checked are: 
	#     [ 0, f_0 ),
	#then [ f_i, f_(i+1) ) for i = 0 to l-2
	#then [ f_(l-1), n )

	#[ 0, f_0 )
	f_0 = flags[0][0]
	if flags[0][1] == 'A':
		for i in range(f_0):
			dist_A.append(f_0 - i)
			dist_C.append(-1)
	elif flags[0][1] == 'C':
		for i in range(f_0):
			dist_A.append(-1)
			dist_C.append(f_0 - i)

	#[ f_i, f_(i+1) ) for i = 0 to l-2
	for i in range(l-1):
		l_i = flags[i+1][0] - flags[i][0] #Number of positions that will get checked in this cycle

		#A...C interval
		if flags[i][1] == 'A' and flags[i+1][1] == 'C':
			#Position f_i
			dist_A.append(0)
			dist_C.append(-1)
			#Positions between f_i and f_(i+1)
			for j in range(1, l_i):
				dist_A.append(j)
				dist_C.append(l_i - j)

		#C...A interval
		elif flags[i][1] == 'C' and flags[i+1][1] == 'A':
			#Position f_i
			dist_A.append(-1)
			dist_C.append(0)
			#Positions between f_i and f_(i+1)
			for j in range(1, l_i):
				dist_A.append(l_i - j)
				dist_C.append(j)

		#A...A interval
		elif flags[i][1] == 'A' and flags[i+1][1] == 'A':
			#Position f_i
			dist_A.append(0)
			dist_C.append(-1)
		
			half = l_i // 2
			#1st half of positions between f_i and f_(i+1)
			for j in range(1, half + 1):
				dist_A.append(j)
				dist_C.append(-1)
			#2nd half of positions between f_i and f_(i+1)
			for j in range(half + 1, l_i):
				dist_A.append(l_i - j)
				dist_C.append(-1)

		#C...C interval
		elif flags[i][1] == 'C' and flags[i+1][1] == 'C':
			#Position f_i
			dist_A.append(-1)
			dist_C.append(0)
		
			half = l_i // 2
			#1st half of positions between f_i and f_(i+1)
			for j in range(1, half + 1):
				dist_A.append(-1)
				dist_C.append(j)
			#2nd half of positions between f_i and f_(i+1)
			for j in range(half + 1, l_i):
				dist_A.append(-1)
				dist_C.append(l_i - j)

	#[ f_(l-1), n) interval
	f_last = flags[l-1][0]
	l_last = n - f_last    #Number of positions left to check
	if flags[l-1][1] == 'A':
		for i in range(l_last):
			dist_A.append(i)
			dist_C.append(-1)
	elif flags[l-1][1] == 'C':
		for i in range(l_last):
			dist_A.append(-1)
			dist_C.append(i)

#Turn the distances into strings so that they can be concatenated together
for i in range(n):
	dist_A[i] = str(dist_A[i])
	dist_C[i] = str(dist_C[i])

#Concatenate the distances
print(' '.join(dist_A))
print(' '.join(dist_C))
