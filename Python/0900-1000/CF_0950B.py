#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Essentially scan through the two lists simultaneously while keeping a subtotal. Call the two
#sequences X and Y. If the subtotals are not equal, get an element from the sequence with the smaller
#subtotal and add it in. If they are equal, we have found a possible end for a file. Add one to the
#max possible number of files and continue scanning. When the subtotals are equal, default to picking
#a term from the first sequence.

#For fast I/O
import sys
input = sys.stdin.readline

Homura = [int(i) for i in input().split()]
m = Homura[0]
n = Homura[1]

l_x = [int(i) for i in input().split()]
l_y = [int(i) for i in input().split()]

sub_x = 0 #Current subtotal for sequence X
sub_y = 0 #Current subtotal for sequence Y
i_x = 0 #Current index while scanning sequence X
i_y = 0 #Current index while scanning sequence Y
ans = 0 #Answer aka max number of possible files

#Terminate when one of the sequences has been fully scanned
while i_x < m and i_y < n:
	if sub_x == sub_y: #Equal subtotals
		ans += 1          #Possible file start
		sub_x += l_x[i_x] #Default add a term to X's subtotal
		i_x += 1          #Move X's scanner up
	elif sub_x < sub_y: #X has a smaller subtotal
		sub_x += l_x[i_x] #Add a term to X's subtotal to close the gap
		i_x += 1          #Move X's scanner up
	elif sub_x > sub_y: #Y has a smaller subtotal
		sub_y += l_y[i_y] #Add a term to Y's subtotal to close the gap
		i_y += 1          #Move Y's scanner up

print(ans)
