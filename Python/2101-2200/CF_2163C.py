#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
A down-right path is essentially picking some column i where you
    - go right until col i
    - go down
    - go right until the end
Therefore, what is important is the min and max along a prefix of the 1st row 
and a suffix of the 2nd row.
Therefore, we can use a prefix max/min array and suffix max/min array 
for the 1st and 2nd rows.

===============================================================================

Pick the example 
6 6 5 7 9 12
1 4 2 8 5 6

prefix min 6 6 5 5 5  5
prefix max 6 6 6 7 9 12
           ------------
           1 2 2 5 5  6 suffix min
           8 8 8 8 6  6 suffix max
           ============
Req to use 1 2 2 5 5  5  l <= this (min of mins)
this col   8 8 8 8 9 12  this <= r (max of maxes)

===============================================================================

Therefore, it works iff at least one of the columns is usable, which is true 
iff at least one of the following pairs ineqs hold
    l <= 1, 8 <= r
    l <= 2, 8 <= r
    l <= 2, 8 <= r
    l <= 5, 8 <= r
    l <= 5, 9 <= r
    l <= 5, 12 <= r
By combining ones with the same bound for l, this list can be compressed to
    l <= 1, 8 <= r
    l <= 2, 8 <= r
    l <= 5, 8 <= r
Now consider each possible l=1,2,...,12
For at least one ineq above to hold, we have
    l = 12 -> NA
    ...
    l =  6 -> NA
    l =  5 -> 8 <= r
    l =  4 -> 8 <= r
    l =  3 -> 8 <= r
    l =  2 -> 8 <= r
    l =  1 -> 8 <= r
This gives an answer of 5 * 5 = 25 which is correct.
'''
for Homu in range(int(input())):
    n = int(input())
    r0 = [int(i) for i in input().split()]
    r1 = [int(i) for i in input().split()]

    #Prefix min/max of row 0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    r0_pre_min = [r0[0]]
    for i in range(1,n):
        r0_pre_min.append(
            min(r0[i], r0_pre_min[-1])
        )
    r0_pre_max = [r0[0]]
    for i in range(1,n):
        r0_pre_max.append(
            max(r0[i], r0_pre_max[-1])
        )

    #Suffix min/max of row 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    r1_suf_min = [r1[-1]]
    for i in range(1,n):
        r1_suf_min.append(
            min(r1[-i-1], r1_suf_min[-1])
        )
    r1_suf_min = r1_suf_min[::-1]
    r1_suf_max = [r1[-1]]
    for i in range(1,n):
        r1_suf_max.append(
            max(r1[-i-1], r1_suf_max[-1])
        )
    r1_suf_max = r1_suf_max[::-1]

    #min of mins and max of maxes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    l_mins = [
        min(r0_pre_min[i], r1_suf_min[i])
        for i in range(n)
    ]
    r_maxs = [
        max(r0_pre_max[i], r1_suf_max[i])
        for i in range(n)
    ]

    #l_val_to_r_limit[i] = the smallest r paired with l=i+1 above ~~~~~~~~~~~~~
    l_val_to_r_limit = [
        None for i in range(2*n)
    ]
    for i in range(n):
        l = l_mins[i] - 1
        r = r_maxs[i]
        if l_val_to_r_limit[l] is None:
            l_val_to_r_limit[l] = r
        else:
            l_val_to_r_limit[l] = min(
                r, l_val_to_r_limit[l]
            )

    #Propagate from back to front ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for i in range(2*n-2,-1,-1):
        if l_val_to_r_limit[i] is None:
            l_val_to_r_limit[i] = l_val_to_r_limit[i+1]
        elif l_val_to_r_limit[i+1] is None:
            pass
        else:
            l_val_to_r_limit[i] = min(
                l_val_to_r_limit[i], l_val_to_r_limit[i+1]
            )

    #Add number of possible r's for each l ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ans = 0
    for i in range(2*n):
        if l_val_to_r_limit[i] is None:
            continue
        ans += 2*n+1 - l_val_to_r_limit[i]

    print(ans)
