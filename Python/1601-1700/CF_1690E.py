#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
First of all, can remove the "divisible part" and count it at the start.
Then just focus on the remainders that are left.

The remainders are all in the range [0,k-1]
Therefore, when two combine, they can either add 0 or 1 to the price.
The goal is to maximize the total number of pairs that sum to 1.

Can probably do this by being greedy from the top going down.
First sort the remainders (O(nlogn) daijobu for n = 2*10^5)
Take largest element
Bsearch for the smallest term that can complement it.
Have two tracers that trace inwards finding pairs until the pointers meet.
The number of pairs formed will be the bonus price attained.

EDIT: Wait I don't need to bsearch the first element to complement the 
largest, I can just start at the ends. It won't TLE anyway
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]
    prices = [int(i) for i in input().split()]

    int_parts = [i//k for i in prices]
    leftovers = [i%k for i in prices]
    leftovers.sort()

    L = 0
    R = n-1
    pairs = 0

    while L < R:
        if leftovers[L]+leftovers[R] >= k:   #If pair found
            pairs += 1
            L += 1
            R -= 1
        else:   #If pair too small
            L += 1
    
    ans = sum(int_parts) + pairs
    print(ans)
