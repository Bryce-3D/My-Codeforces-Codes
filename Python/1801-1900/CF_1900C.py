#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Looks like standard dp

Let x = min number of changes to get to a leaf from subtree rooted 
        at the left child
    y = min number of changes to get to a leaf from subtree rooted 
        at the right child

if root = U:
    ans = min(x+1,y+1)
elif root = L:
    ans = min(x,y+1)
elif root = R:
    ans = min(x+1,y)
'''

for Homu in range(int(input())):
    n = int(input())
    s = input()

    #chi[i] = [left child of i, right child of i]
    chi = []
    for i in range(n):
        chi.append([int(i)-1 for i in input().split()])   #0-index

    #par[i] = parent of node i
    par = [-1 for i in range(n)]

    #BFS traversal of the nodes in the tree
    BFS = [0]
    for i in range(n):
        v = BFS[i]
        v_l = chi[v][0]
        v_r = chi[v][1]
        if v_l != -1:
            BFS.append(v_l)
            par[v_l] = v
        if v_r != -1:
            BFS.append(v_r)
            par[v_r] = v
    
    #ans[i] = answer for the subtree rooted at node i
    ans = [0 for i in range(n)]
    
    #Traverse upwards in reverse BFS order
    for v in BFS[::-1]:
        #Retreive info about children
        v_l = chi[v][0]
        v_r = chi[v][1]

        #If no children
        if v_l == -1 and v_r == -1:
            ans[v] = 0
            continue

        #If only left child exists
        if v_r == -1:
            if s[v] == 'L':
                ans[v] = ans[v_l]
            else:
                ans[v] = ans[v_l]+1
            continue
        
        #If only right child exists
        if v_l == -1:
            if s[v] == 'R':
                ans[v] = ans[v_r]
            else:
                ans[v] = ans[v_r]+1
            continue
        
        #If both children exist
        ans_l = ans[v_l]
        ans_r = ans[v_r]
        if s[v] == 'L':
            ans[v] = min(ans_l,ans_r+1)
        elif s[v] == 'R':
            ans[v] = min(ans_l+1,ans_r)
        elif s[v] == 'U':
            ans[v] = min(ans_l+1,ans_r+1)
    
    print(ans[0])
