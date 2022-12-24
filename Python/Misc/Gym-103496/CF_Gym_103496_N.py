#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Thought process:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The positions of the pixels don't really matter, what matters is what pixels exist at the start
#We can then partition these pixels into sets based on their starting color
#If at any given point, one set's color is changed to be the same color as another set, then the two sets
#will merge to the same color and cannot be separated back to their original colors, making it impossible
#Otherwise, at any time through the process, all sets have pairwise distinct colors, so we can restore the photo
#by doing the reverse of what Cindy did (aka flip X is Y to Y is X and reverse the order of the steps),
#WITH THE EXCEPTION OF CHANGES THAT CHANGE NOTHING*** DO NOT FORGET THIS CORNER CASE WHEN CODING (aka A is B but
#there are no A's in the picture in the first place, since the reverse of this might actually change something)





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Gameplan:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Set up variables
#Main variables for the code:
	# colors   - store the colors that currently exist in the image
	# l_op     - list of relevant `X is Y` operations, where each element is represented as [X,Y]
	# possible - boolean value to store whether it is possible or not
#Process the image given and reduce it to a set containing all the colors that currently exist

#For each operation `X is Y`:
	# If `possible` is false, ignore and proceed to the next operation
	# Elif X=Y, ignore and proceed to the next operation
	# Elif X is not in the set of colors that exist, ignore and proceed to the next operation
	# Elif Y is not in the set of colors that exist, remove X and add Y to the set of colors that exist, 
	#     and add [X,Y] to a list of relevant operations (to be used for reversing purposes later)
	# Else (X != Y and both are in the set of colors that exist), the answer is `lmao no.` Have `possible`
	#     flip from True to False

#If `possible` is true, print 'YES', len(l_op), and the elements of l_op [X,Y] as Y is X from last to first
#Else, print 'NO'





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Actual Code
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Extracting the set of colors that exist in the current image
Homura = [int(i) for i in input().split()]
r = Homura[0]
c = Homura[1]

colors = set() #Set of the colors that currently exist in the image
for Mahou_Shoujo_Madoka_Magica in range(r):
	row = input()
	for i in range(c):
		colors.add(row[i])

l_op = []         #List of relevant operations
possible = True

n = int(input()) #Number of operations Cindy does
for Mahou_Shoujo_Madoka_Magica in range(n):
	op = input()
	X = op[0]
	Y = op[5]

	if possible == False:   #Already found a previous step that makes it impossible
		continue
	elif X == Y:            #Literally nothing changes
		continue
	elif X not in colors:   #Literally nothing changes part 2 electric boogaloo
		continue
	elif Y not in colors:   #X in colors, Y not in colors, a revertable change
		colors.remove(X)
		colors.add(Y)
		l_op.append([X,Y])
	else:                   #X != Y both in colors, makes it impossible
		possible = False


if possible:
	print('YES')
	l = len(l_op)
	print(l)

	for i in range(l):
		print(f"{l_op[l-1-i][1]} is {l_op[l-1-i][0]}")
else:
	print('NO')
