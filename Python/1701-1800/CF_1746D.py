#For fast I/O
from email.mime import base
import sys
input = lambda: sys.stdin.readline().strip()

#For recursion
#sys.setrecursionlimit(2 * 10**5 + 5)

'''Idea
99% sure this is some sort of dp

If c_i is even, then there must be an equal number of left and 
right paths from i
If c_i is odd, then there are two ways to divide c_i = 2k+1, 
k,k+1 or k+1,k

Even -> splits into 2 evens or 2 odds (odd -> more work)
Odd -> Propagates itself down both sides

Each node has at most 2 possible number of paths (induct from top downwards)
Therefore it should be O(n)?


Algorithm
Make array 'children' where children[i] returns a list of the children of node i
'''



#Define the "base number" of paths through a vertex to be the lower bound for 
#the number of paths through a vertex of the tree.
#It can be shown by induction from top to bottom that each vertex has at most 
#2 different possible number of paths, so if k is the base number of a vertex, 
#then there must be either k or k+1 paths through it.

for Homu in range(int(input())):
    #Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #n = number of nodes, z = total number of paths
    n,z = [int(i) for i in input().split()]
    parent_ = [int(i)-1 for i in input().split()]   #0-index the vertices
    parent = [None]
    for i in range(n-1):
        parent.append(parent_[i])
    score = [int(i) for i in input().split()]

    #children[i] will return a list of the children of node i (0-indexed)
    children = [[] for i in range(n)]
    for i in range(1,n):
        children[parent[i]].append(i)



    #BFS Initializing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #list of vertices traversed in BFS order
    BFS_ord = [0]
    #n_paths[i] = Base number of paths through a vertex i
    n_paths = [0 for i in range(n)]
    n_paths[0] = z
    #ex_paths[i] = Number of excess paths left from i after dividing its
    #base paths equally among its children
    ex_paths = [-1 for i in range(n)]

    #Perform the BFS
    for i in range(n):
        next = BFS_ord[i]        #Next vertex in the BFS
        l = len(children[next])   #Number of children of next

        #If next has children
        if l != 0:
            k = n_paths[next]   #Base number of paths through this vertex
            k_0 = k // l        #Base number of paths through the children of next
            ex = k % l          #Number of excess paths on next

            ex_paths[next] = ex   #Update the excess for next
            for child in children[next]:   #For each child
                BFS_ord.append(child)      #Add to BFS order
                n_paths[child] = k_0    #Store number of base paths into children

        #Otherwise, excess is not meaningful and no children to update



    #Reverse BFS Solving ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Process the nodes reverse BFS order
    rev_BFS = BFS_ord[::-1]
    #ans[i] = [maximum total with the base number of paths rooted at i, 
    #          extra total from adding 1 extra path rooted at i]
    ans = [[-1,-1] for i in range(n)]
    for i in range(n):
        r = rev_BFS[i]     #Root of current subtree
        s_r = score[r]     #Score associated with the current root
        k = n_paths[r]     #Base number of paths through r
        ex = ex_paths[r]   #Number of excess paths through r; -1 if a leaf

        #If leaf
        if len(children[r]) == 0:
            ans[r] = [s_r * k, s_r]

        #If not leaf
        else:
            #Check the base total from the children
            base_total = 0
            for child in children[r]:
                base_total += ans[child][0]
            
            #Check extra from remainder/excess paths
            child_extra = []
            for child in children[r]:
                child_extra.append(ans[child][1])
            #Sort in descending order since we want to be greedy
            child_extra.sort()
            child_extra = child_extra[::-1]
            #Get the `excess` largest extras greedily
            excess_total = sum(child_extra[:ex])
            bonus_path = child_extra[ex]   #Extra total if it were k+1 instead

            #Don't forget to add the node itself
            node_total = s_r * k

            #Store it in ans
            ans[r] = [base_total+excess_total+node_total, bonus_path+s_r]
    
    print(ans[0][0])



    # #Finds the answer if the root were r and k as well as the extra if a 
    # #(k+1)-th path were allowed
    # #Returns [ans with k paths, extra from (k+1)-th path]
    # def helpme(r, k):
    #     global children
    #     global score
    #     s_r = score[r]

    #     #Base case: Leaf
    #     if len(children[r]) == 0:
    #         return [s_r*k, s_r]
        
    #     l = len(children[r])   #Number of children of r
    #     k_0 = k // l           #Number of paths for each child of r (or k_0+1)
    #     excess = k % l         #Number of paths left after letting each node have k_0

    #     #Recursively solve the maximum for 
    #     child_ans = []
    #     for child in children[r]:
    #         child_ans.append(helpme(child, k_0))
        
    #     #Check the base total from the children
    #     base_total = sum(i[0] for i in child_ans)

    #     #Check extra from the remainder/excess paths
    #     #Sort in descending order since we want to be greedy
    #     child_extra = [i[1] for i in child_ans]
    #     child_extra.sort()
    #     child_extra = child_extra[::-1]
    #     excess_total = sum(child_extra[:excess])
    #     bonus_path = child_extra[excess]   #Extra total if it were k+1 instead

    #     #Don't forget to add the node itself
    #     node_total = s_r * k

    #     ans = [base_total+excess_total+node_total, bonus_path+s_r]
    #     return ans
    
    # print(helpme(0, k_)[0])
