#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea 1
Track the array and the sum
Query type 1 -> Easy to do (O(1))
Query type 2 -> Need to replace the entire array (O(n))

Fails for:
Spam Query type 2
O(nq) which is > 10^8
'''

'''Idea 2
Track the array and the sum AND have a set of indices and last type 1 query

a       = The array of numbers which tracks ONLY changes following queries of TYPE 1
sum     = Sum of the prev/curr query
updated = Set of indices that have been updated following a query of TYPE 2
refresh = The last number used for replacing from a query of type 2

Program flow:
Initialization
    a   = Given array
    sum = sum of given array
    updated = {0,1,...,n-1} (all indices are updated at the start)
    refresh = 0 (doesn't matter now)

For each query
    if type 1 query
        if index to change in updated:
            Get change in sum based on new val vs val in a
            Update a and sum
        elif index to change not in updated:
            Get change in sum based on new val vs refresh
            Add index to updated
            Update a and sum
    
    elif type 2 query
        Update refresh to the new value to replace everything
        Update updated to be the empty set (nothing in a is guaranteed to be correct)
        Update sum to be refresh * n
    
    Print the sum

Now each query is O(1) on average*
*Sets are O(1) on average cause yes hashing stuff
'''

#Processing inputs
Homu = [int(i) for i in input().split()]
n = Homu[0]
q = Homu[1]
a = [int(i) for i in input().split()]

#Preprocessing
Sum = sum(a)                      #Sum tracker
Updated = {i for i in range(n)}   #Indices updated since last type 2 query
Refresh = 0                       #Number from last type 2 query

#For each query
for Homu in range(q):
    #Process query input
    Kumi = [int(i) for i in input().split()]
    t = Kumi[0]
    
    #Type 1 query
    if t == 1:
        i = Kumi[1] - 1   #0 Index it
        x = Kumi[2]

        if i in Updated: #If i in Updated
            delta_sum = x - a[i]      #Change in sum
            a[i] = x                  #Update array
            Sum += delta_sum          #Update sum
        else:            #If i not in Updated
            Updated.add(i)            #Add i to updated
            delta_sum = x - Refresh   #Change in sum
            a[i] = x                  #Update array
            Sum += delta_sum          #Update sum
    
    #Type 2 query
    else:
        Refresh = Kumi[1]   #The new value that "replaces" a
        Updated = set()     #No indices of a are (surely) updated anymore
        Sum = Refresh * n   #Update the sum
    
    #Sum is now updated
    print(Sum)
