#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Start from the bottommost vertex, and add as much as possible?

IDEA:
ONLY UPDATE THE PARENT, NO NEED TO TRACE ALL THE WAY UP THE TREE!!!
Keep a variable called 'max_add' where 'max_add[i]' returns the maximum 
value added to node i from it's children's chains.
This is sufficient info since 
    If chains can add up to k to a node, then it can add up to k also 
    for it's children (or the r_i of this node, whichever is smaller)

Increase number of needed operations by 1 everytime max_add[i] is 
not enough to satisfy the required amount.
Always add as much as possible at every step, no harm capping every time.

ALSO if a node is enough but it's parent isn't, just start at the parent, 
no need to inc the child


Code flow:

'''

for Homu in range(int(input())):
    n = int(input())

    #parent[i] returns the parent of node i (0-indexed)
    #The parent of node 0 is taken to be -1 cause yes
    parent = [-1]
    parent += [int(i)-1 for i in input().split()]

    #limit[i] returns [l_i,r_i], the bound for the ith node
    limit = []
    for i in range(n):
        limit.append([int(i) for i in input().split()])

    #max_inc[i] contains the maximum addition possible to node i 
    #By the chains coming from below it
    max_inc = [0 for i in range(n)]

    #Required number of chains
    req = 0

    #For nodes n-1 to 1
    for i in range(n-1, 0, -1):
        p_i = parent[i]   #Parent of i

        #If max_inc is not enough and need to start chain
        if max_inc[i] < limit[i][0]:
            req += 1                  #Increase req
            i_limit = limit[i][1]     #Upper limit for i
            max_inc[p_i] += i_limit   #Increase max_inc of parent
        
        #If max_inc is enough and no need to start chain
        else:
            i_max_inc = max_inc[i]   #max_inc for i
            i_limit = limit[i][1]   #Upper limit for i
            max_inc[p_i] += min(i_max_inc, i_limit)    #max_inc to parent is i's limit or max_inc
    
    #Check if node 0 needs one last chain for itself
    if max_inc[0] < limit[0][0]:
        req += 1
    
    print(req)
