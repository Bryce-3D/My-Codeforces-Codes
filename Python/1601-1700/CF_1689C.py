#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
You will always cut one of the children of the bottomost infected node.
Recursion on left and right?

WAIT EPIPHANY
THE INFECTED IS BASICALLY A LINE
Therefore ans is like
"Min depth" + the ones that got cut
Wait no not necessarily
Rather find the highest node with only one child
Then the line can end there


HOLE:
Number of children of bottom most ending (0 or 1)
also affects number of survivors


WHY WA FFS

Can be shown that always better to cut a node that's about to get infected
'''

#import sys
#sys.setrecursionlimit(4 * 10 ** 5)



for Homu in range(int(input())):
    n = int(input())

    #adj_list[i] returns the neighbors of vertex i in order (0-indexed)
    adj_list = [[] for i in range(n)]
    #Process inputs
    for i in range(n-1):
        Kumi = [int(i) for i in input().split()]
        v1 = Kumi[0] - 1
        v2 = Kumi[1] - 1
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    #Sort neighbors of each node
    for neighbors in adj_list:
        neighbors.sort()
    


    #depth[i] returns the depth of the ith node (node 0 counts as depth 0)
    depth = [-1 for i in range(n)]

    frontier = []
    included = {0}
    depth[0] = 0
    #L = 0

    included.add(0)
    for ind in adj_list[0]:
        frontier.append([ind,1])
        included.add(ind)
    
    for L in range(n-1):
        #Set the current node
        curr_ind, dep = frontier[L]
        depth[curr_ind] = dep
        #Recurse on the children
        for ind in adj_list[curr_ind]:
            if ind not in included:
                frontier.append([ind,dep+1])
                included.add(ind)

    

    #Perform DFS/BFS
    #def set_depth(ind, dep):
    #    depth[ind] = dep   #Set current index
    #    for i in adj_list[ind]:   #For neightbors
    #        if depth[i] == -1:    #If not yet set (aka must be child)
    #            set_depth(i, dep+1)
    #Initiate the DFS/BFS
    #set_depth(0,0)

    #for i in range(1,n):
    #    parent = adj_list[i][0]
    #    depth[i] = depth[parent] + 1
    


    #children[i] returns the number of children of node i
    children = [0 for i in range(n)]

    children[0] = len(adj_list[0])
    for i in range(1,n):
        children[i] = len(adj_list[i]) - 1
    


    #Find min number of casualties
    #Initialize to n since you can't lose more than n nodes
    #WHETHER THIS NODE HAS 0 OR 1 CHILDREN ALSO MATTERS
    min_casualties = n

    for i in range(n):
        if children[i] != 2:
            curr_casualties = 2 * depth[i] + children[i] + 1
            min_casualties = min(curr_casualties, min_casualties)
    


    #Print the ans
    max_survivors = n - min_casualties
    print(max_survivors)

    #DEBUG
    #print(depth)
    #print(frontier)
