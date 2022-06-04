#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()
 
'''Ideas
Can first use E queries with only one 1 to get the weight of each indiv edge
 
 
Random ideas for guess patterns
1.) (Weight of )
    10000...
    01000...
    00100...
    00010...
    ...
2.) 
    10000...
    11000...
    11100...
    11110...
    ...
 
COMBINE THEM AND GET KRUSKAL'S (kinda)
But need to sort after doing 1
'''
 
Homu = [int(i) for i in input().split()]
V = Homu[0]
E = Homu[1]
 
 
#e_weight[i] returns the weight of edge i+1
e_weight = []
 
 
 
#Get the weight of each individual edge
query = ['0' for i in range(E)]
for i in range(E):
    query[i] = '1'
    print('? ' + ''.join(query))
    sys.stdout.flush()
    query[i] = '0'
    e_weight.append(int(input()))
 
 
 
#Bubblesort indices based on edge weight
#Fine since E <= 500 anyway
sorted_indices = [i for i in range(E)]
for Homu in range(E-1):
    for i in range(E-1):
        L = sorted_indices[i]
        R = sorted_indices[i+1]
        if e_weight[L] > e_weight[R]:
            sorted_indices[i], sorted_indices[i+1] = R,L
 
 
 
#Perform Kruskal's
included = ['0' for i in range(E)]
prev_sum = 0
for i in range(E):
    ind = sorted_indices[i]   #Next index to check
    included[ind] = '1'       #Include for next query
 
    #Query
    print('? ' + ''.join(included))
    sys.stdout.flush()
 
    curr_sum = int(input())
 
    if curr_sum - prev_sum == e_weight[ind]:   #Included
        prev_sum = curr_sum
    else:   #Not included
        included[ind] = '0'
    
 
 
#Print the ans
print('! ' + str(prev_sum))
sys.stdout.flush()
