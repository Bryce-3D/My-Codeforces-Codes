#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
10
1 8 2 5 3 5 3 1 1 3
2 9 2 4 8 2 3 5 3 1

Best swap is (1,2) with (8,9) or (2,2) with (8,9)

Suppose we do the swap
    A B  -> A B
    C D  -> D C

WLOG let A >= B
    A <= C,D or B >= C,D -> no change

i.e. at least one of C,D must be strictly between A,B to have an effect

Case 1: A > C,D > B
    This changes the value by |C-D|
    If C>D, this is an increase
    i.e. want 
        A > C > D > B
Case 2: A > C > B only
    If D >= A, this is bad
    If D <= B, this is good
    i.e. want 
        A > C > B >= D
Case 3: A > D > B only
    This is analogous to case 2 and we need C >= A for an increase
    i.e. we want
        C >= A > D > B

Note that in every case an increase only happens when min(A,C) > max(B,D)
And in every case the increase is 2 * (min(A,C)-max(B,D))

ALGO:
For every index i
    Get max(a[i],b[i]) and min(a[i],b[i])
Let M be the max of mins
Let m be min of maxs

ans = original absolute beauty + 2*max(0,M-m)
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    maxs = [max(a[i],b[i]) for i in range(n)]
    mins = [min(a[i],b[i]) for i in range(n)]

    M = max(mins)
    m = min(maxs)

    diffs = [abs(a[i]-b[i]) for i in range(n)]
    ans = sum(diffs) + 2*max(0,M-m)
    print(ans)
