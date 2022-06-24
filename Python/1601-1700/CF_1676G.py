#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
1 <= a_i < i -> children always have larger index then parent.
Iterate from highest to lowest index.

childrens[i] returns the childrens of node i (0-indexed)
black[i] returns the number of black vertices at the subtree rooted at i
white[i] similar
'''

for Homu in range(int(input())):
    n = int(input())
    #parents[i] returns the parent of node i (0-indexed)
    #except for parent[0] which returns -1
    parent = [-1]
    parent += [int(i)-1 for i in input().split()]
    colors = input()

    #childrens[i] returns a list of the childrens of node i (0-indexed)
    childrens = [[] for i in range(n)]
    for i in range(1,n):
        par = parent[i]           #Parent of i
        childrens[par].append(i)   #Add i to list of it's parent
    
    #black/white[i] returns the number of black/white 
    #vertices in the subtree rooted at i
    black = [0 for i in range(n)]
    white = [0 for i in range(n)]

    for ind in range(n-1,-1,-1):
        children = childrens[ind]
        b = 0
        w = 0
        for child in children:
            b += black[child]
            w += white[child]
        if colors[ind] == 'B':
            b += 1
        else:
            w += 1
        black[ind] = b
        white[ind] = w
    
    ans = 0
    for i in range(n):
        if black[i] == white[i]:
            ans += 1
    print(ans)
