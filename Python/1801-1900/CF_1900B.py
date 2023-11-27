#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Suppose our goal is only 1s at the end
Doing
    1,2 -> 3
    2,3 -> 1
    3,1 -> 2
doesn't really help since we could kinda instead do
    2,3 -> 1
    2,3 -> 1
directly

Note that the parity of b+c is invariant
In the end we want b+c=0, so we need b+c to be even

Suppose b+c is even, when will it become impossible
Greedily nuke pairs of 2's and 3's -> get |b-c|=d etc's leftover
d is even since b+c is even
Suppose at least d/2 1's
Use to get d/2 2's, d/2 3's, then nuke them to 1's
Probably no better way

WA???
    1,2 -> 3
    1,3 -> 2
These 2 moves just burn two 1's
Therefore you will never use both simultaneously

OH THE 1S CAN BE REUSED
    2 6 0
    0 4 2
    2 2 0
    1 1 1
    0 0 0


    1  n  0
    0 n-1 1
    1 n-2 0
    ...
    1  0  0
*n is even

Suppose b+c is even
Only impossible if one of b,c is 0 and a is 0
Otherwise can generate a one
But we are given a,b,c >= 1 lmao ok then
'''

for Homu in range(int(input())):
    a,b,c = [int(i) for i in input().split()]
    ans = [0,0,0]

    #Is all 1s possible
    if (b+c)%2 == 0:
        ans[0] = 1

    #Is all 2s possible
    if (c+a)%2 == 0:
        ans[1] = 1

    #Is all 3s possible
    if (a+b)%2 == 0:
        ans[2] = 1
    
    ans = ' '.join([str(i) for i in ans])
    print(ans)
