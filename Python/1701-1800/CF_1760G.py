#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Backtracking just cancels the last move => does nothing

Two paths, p1 before and p2 after teleporting
    p1 starts at a
    p2 ends at b
    p2 non-empty since cannot teleport directly

Suppose p1 and p2 overlap
Then you can cancel out the common edges
Common edges bet p1 and p2 must be consecutive (otherwise 
we'd get a loop, contradicting the fact that we are on a tree)

A tree works iff there exists two paths p1,p2 such that
    p1 has an end point at a
    p2 has an end point at b
    p2 has at least one edge
    XOR along p1 = XOR along p2


BFS outwards from a and get all XORs?
No, DFS would be better in this case, backtracking means 
we can track the current XOR of the path more easily

DFS outwards from a,b, and get all possible values of XOR 
paths for p1 and p2 (exlucing the case where p2 has no edges).
Possible iff there exists a common possible value for p1 and p2.

*use adjacency list to store the edges
HOW TO DFS
    to_visit = stack to push and pop next vertices to visit
    marked   = set of vertices that have been pushed into to_visit
             = used to prevent going through the same vertex twice

The ff should work for DFS on a tree specifically at least
'''

'''DFS Template
*A vertex could be pushed onto the stack more than once (it's degree 
to be exact), but it will only be processed the first time it's popped

to_visit = [a]   #Stack of vertices to visit
processed = {}   #Set of vertices that have been processed

while to_visit is not empty:
    next = to_visit.pop()
    if next not in processed:
        *process vertex*

        push next's neighbors into to_visit
        processed.add(next)

But how to get edges???
Maybe it's easier to just get the vertices in DFS order, then handle 
the edges afterwards
'''

'''
I give up trying to implement iterative DFS with edge processing

Use BFS instead:

par_a = [-1 for i in range(n)]
BFS = [a]
seen = {a}

for i in range(n):
    next = BFS[i]
    for nei in neighbors of next:
        if nei not in seen:
            BFS.append(nei)
            seen.add(nei)
            par_a[nei] = i

for v in BFS:

'''

'''ERROR
You cannot pass by vertex b in the process...
Need to prune off the branches of the subtree rooted at b 
when doing BFS with root a.
'''


for Homu in range(int(input())):
    #Input processing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    n,a,b = [int(i) for i in input().split()]
    a,b = a-1,b-1   #0-index the vertices

    #adj[i] = dictionary with key = neighbor, value = weight of edge
    #adj[i][j] = weight of (i,j) if the edge exists, error otherwise
    adj = [{} for i in range(n)]
    for Kumi in range(n-1):
        u,v,w = [int(i) for i in input().split()]
        u,v = u-1,v-1   #0-index the vertices
        #Record the edge weight from both ends
        adj[u][v] = w
        adj[v][u] = w



    #Getting a BFS order and parents wrt a starting root ~~~~~~~~~~~~~~~~~~~~~~
    #BFS from root a excluding the children of the subtree rooted at b
    BFS_a = [a]                        #BFS traversal starting from a
    par_a = [-1 for i in range(n)]     #par_a[i] = parent of i wrt a
    seen = [False for i in range(n)]   #seen[i] = True iff i is in BFS_a
    seen[a] = True
    i = 0
    while i < len(BFS_a):   #While there are more nodes to traverse
        v = BFS_a[i]
        #If we are at v, prune it's branches
        if v != b:
            for nei in adj[v]:
                if not seen[nei]:       #If v is a child
                    BFS_a.append(nei)   #Add child to BFS
                    par_a[nei] = v      #Record `next` as parent
                    seen[nei] = True    #Record v as seen
        i += 1
    #BFS from root b
    BFS_b = [b]                        #BFS traversal starting from b
    par_b = [-1 for i in range(n)]     #par_a[i] = parent of i wrt b
    seen = [False for i in range(n)]   #seen[i] = True iff i is in BFS_b
    seen[b] = True
    for i in range(n):
        v = BFS_b[i]
        for nei in adj[v]:
            if not seen[nei]:       #If v is a child
                BFS_b.append(nei)   #Add child to BFS
                par_b[nei] = v      #Record `next` as parent
                seen[nei] = True    #Record v as seen



    #Getting the XOR of the path to each vertex from a starting root ~~~~~~~~~~
    #Starting root = a
    val_a = [0 for i in range(n)]   #val_a[i] = xor of path from a to i
    for i in range(1,len(BFS_a)):
        v = BFS_a[i]              #Next vertex in the BFS
        par = par_a[v]            #Parent of v with a as the root
        e = adj[v][par]           #Weight of edge from `par` to v
        v_val = val_a[par] ^ e    #xor value of v with root a
        val_a[v] = v_val          #Record xor value of v

    #Starting root = b
    val_b = [0 for i in range(n)]   #val_b[i] = xor of path from b to i
    for i in range(1,n):
        v = BFS_b[i]
        par = par_b[v]           #Parent of v with b as the root
        e = adj[v][par]          #Weight of edge from `par` to v
        v_val = val_b[par] ^ e   #xor value of v with root b
        val_b[v] = v_val         #Record xor value of v



    #Possible xor values when teleporting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Exclude path from a to b
    valid_val_a = set()
    for i in range(len(BFS_a)):
        if BFS_a[i] != b:
            val = val_a[BFS_a[i]]
            valid_val_a.add(val)
    #Exclude path from b to itself
    valid_val_b = set()
    for i in range(n):
        if i != b:
            valid_val_b.add(val_b[i])



    #Solving the problem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    possible = False
    if val_a[b] == 0:   #If a direct path is possible
        possible = True
    else:               #If teleportation is needed
        #Check if there's two "teleport-valid" paths with the same xor
        for val in valid_val_a:
            if val in valid_val_b:
                possible = True
                break
    
    if possible:
        print('YES')
    else:
        print('NO')
