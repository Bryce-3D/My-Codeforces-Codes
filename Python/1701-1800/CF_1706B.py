#For fast I/O
from itertools import chain
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Disjoint segments can be connected iff even number 
of blocks exist between.

Generalization: Note that 0 is fucking even also

Take as blocks ocnsdier the aintervale abetween see even number between can connect as is eotherwise -1 tnad it wyeh handles caseds
'''

'''
for Homu in range(int(input())):
    n = int(input())
    colors = [int(i)-1 for i in input().split()]   #0-indexed

    last_seen = [-1 for i in range(n)]
    curr_height = [0 for i in range(n)]
    max_height = [0 for i in range(n)]

    for i in range(n):
        c = colors[i]
        if last_seen[c] == -1:
            last_seen[c] = i
            curr_height[c] = 1
        elif (i - last_seen[c])%2 == 1:
            last_seen[c] = i
            curr_height[c] += 1
        else:
            last_seen[c] = i
            max_height[c] = max(max_height[c], curr_height[c])
            curr_height[c] = 1
    
    for i in range(n):
        max_height[i] = max(max_height[i], curr_height[i])

    ans = [str(i) for i in max_height]
    ans = ' '.join(ans)
    print(ans)
'''

for Homu in range(int(input())):
    n = int(input())
    colors = [int(i)-1 for i in input().split()]   #0-indexed

    #chains[i] returns a list with elements of the form [L,R], indicating that 
    #the Lth to Rth block are all of color i, and that the (L-1)th and (R+1)th 
    #block either don't exist or have a diff color
    chains = [[] for i in range(n)]

    curr_color = colors[0]
    curr_L = 0
    for i in range(1,n):
        if colors[i] != curr_color:   #End of a chain
            chains[curr_color].append([curr_L,i-1])
            curr_color = colors[i]
            curr_L = i
    chains[curr_color].append([curr_L,n-1])
    
    #Check longest per color
    ans = []
    for i in range(n):
        chain_i = chains[i]
        if len(chain_i) == 0:
            ans.append(0)
        else:
            ans_i = chain_i[0][1] - chain_i[0][0] + 1
            for i in range(1,len(chain_i)):
                ans_i += chain_i[i][1] - chain_i[i][0] + 1
                if (chain_i[i][0] - chain_i[i-1][1]) % 2 == 0:
                    ans_i -= 1
            ans.append(ans_i)
    
    ans = [str(i) for i in ans]
    ans = ' '.join(ans)
    print(ans)
