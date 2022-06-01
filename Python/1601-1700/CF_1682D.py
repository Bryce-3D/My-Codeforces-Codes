#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
As long as a tree exists, then intersections can be uncrossed like 
in the given example where (2,4),(3,6) became (2,3),(4,6).
Just keep uncrossing the edges until the sum of |v2-v1| over all 
edges (v1,v2) is minimized, which necessitates no intersections.
Uncrossing decreases this sum by at least 1 each time and a minimum must 
exist since there are finite ways to connect it.
Therefore it will eventually reach the minimum and be uncrossed.
Now just have to construct...

Can be shown that as long as there's at least 2 odd degrees and that the 
sum of the degrees is even, the tree exists.
Now just need to make it not intersect on the circle.

Idea:
1.) Split into contiguous blocks of 100...00 (1 followed by k 0s for some 
    k>=0). Call the 1 in front the tail and the last 0 (possibly the 1 
    itself if there are no 0s) the head.
2.) Connect them consecutively. The tail will be a leaf, and only the head 
    will get anymore connections after this
3.) Designate one head as the central power. Connect all other heads to 
    this central power.
4.) Since there are an even number of 1s, there will be an even number of 
    blocks. It can then be checked that all parities are satisfied when 
    connecting all block's heads to a central power.
'''

for Homu in range(int(input())):
    n = int(input())
    s = input()
    parity = [int(s[i]) for i in range(n)]
    n1 = parity.count(1)
    
    if n1 == 0 or n1%2 == 1:   #If not possible
        print('nO')    #Print nO
    else:   #If possible
        print('YeS')   #Print YeS

        #Print out all edges within a 10...0 block (clockwise)
        if parity[0] == 0:
            print(1,n)
        for i in range(1,n):
            if parity[i] == 0:
                print(i, i+1)
        
        #Find indices with 1 (0-indexed, take 0 as n)
        ind = []
        for i in range(1,n):
            if parity[i] == 1:
                ind.append(i)
        if parity[0] == 1:
            ind.append(n)

        #Print out all edges connecting heads of blocks
        #The indices of heads when 1-indexed coincides with the 
        #positions of the 1s when 0-indexed
        central_power = ind.pop()
        for i in ind:
            print(i, central_power)
