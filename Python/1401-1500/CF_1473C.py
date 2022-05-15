#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
About time to put this problem to rest.
I finally proved it a day or two after the round but never
got around to actually writing up the code.
Still remember the idea after a year kinda.

Claim: b's inversions doesn't exceed a iff the first 
    (2k-n-1) terms are 1, 2, ..., 2k-n-1
Proof:
    We first show that the current sequence a actually has the least 
    possible number of inversions.

    Divide ay sequence of such a form into 2 regions
    Region 1: First 2k-n-1 -> Just normal
    Region 2: Last 2n-2k+1 -> Symmetric part

    3 possible pairs to consider based on the regions they're from
        1 & 1: Sequence a has 0 inversions here
        2 & 2: For convenience, let n-k = t
            There are 2t+1 numbers
            It can be shown that this part will always have exactly 
                [(2t+1)C2 - t]/2 = t^2
            inversions (t pairs involve equal numbers, all other pairs 
            have a corresponding symmetric pair, and exactly one of these
            is an inversion).
        1 & 2: Sequence a has 0 inversions here
    
    Therefore a has (n-k)^2 inversions and no permutation p can create a b
    with less inversions.
    Therefore, the b we want must also have exactly (n-k)^2 inversions.
    By a similar argument with the 2 regions above, this can happen iff 
    the smallest (2k-n-1) terms all appear in region 1 in increasing order.


Now to make b lexicographically maximum, it must be
    1, 2, 3, ..., 2k-n-1, k, k-1, ..., 2k-n+1, 2k-n, 2k-n+1, ..., k-1, k
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]

    region_1 = [str(i) for i in range(1, 2*k-n)]
    region_2 = [str(i) for i in range(k, 2*k-n-1, -1)]
    b = region_1 + region_2

    ans = ' '.join(b)
    print(ans)
