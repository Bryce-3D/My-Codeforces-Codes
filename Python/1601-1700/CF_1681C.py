#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
1.) Sort a by moving the smallest term to the front repeatedly 
    while doing the swaps on b at the same time
2.) Find contiguous blocks of equal numbers in a by a linear scan 
3.) For each contiguous block, sort the corresponding block in b 
    by again repeatedly moving the smallest term to the front
4.) Check if it's sorted. If yes, print out the tracked swaps.
    Otherwise, it can't be done.

|swaps| <= 2 * 99 < 10^4

Time complexity: O(tn^2) <= 10^6 < 10^7
'''

#Returns the minimum element in l[i1:i2] of a list l
#REQUIRES i2 > i1
def subarr_min(l, i1, i2):
    Min = l[i1]
    for i in range(i1,i2):
        Min = min(Min, l[i])
    return Min




#Returns the min index of an element e in l[i1:i2]
#REQUIRES e to be in l[i1:i2]
def subarr_ind(l, i1, i2, e):
    for i in range(i1, i2):
        if l[i] == e:
            return i




for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    swaps = []   #Records the swaps done; is 0-indexed


    #Sort a
    for i in range(n-1):
        Min = subarr_min(a, i, n)          #Min amogrest
        i_min = subarr_ind(a, i, n, Min)   #Min index of Min
        if i_min != i:   #Wrong pos, needs a swap
            a[i],a[i_min] = a[i_min],a[i]
            b[i],b[i_min] = b[i_min],b[i]
            swaps.append([i,i_min])
    

    #Find contiguous subarrays of a with equal items
    #jumps contains indices i where a[i-1] != a[i]
    jumps = [0]   #Mark the start of the array
    for i in range(n-1):
        if a[i] != a[i+1]:
            jumps.append(i+1)
    jumps.append(n)   #Mark the end of the array
    

    #Sort b corresponding to each contiguous subarray 
    #of a with equal items
    for i in range(len(jumps)-1):
        i1 = jumps[i]
        i2 = jumps[i+1]
        #Sort b similar to a earlier
        for j in range(i1, i2-1):
            Min = subarr_min(b, j, i2)          #Min amogrest
            j_min = subarr_ind(b, j, i2, Min)   #Min index of Min
            if j_min != j:   #Wrong pos, needs a swap
                b[j],b[j_min] = b[j_min],b[j]
                swaps.append([j,j_min])
    

    #Checking if it worked
    sorted = True
    for i in range(n-1):
        if b[i] > b[i+1]:
            sorted = False
            break
    if sorted:
        print(len(swaps))
        for swap in swaps:
            print(swap[0]+1, swap[1]+1)   #Change back to 1-indexed
    else:
        print(-1)
