#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Split into partitions of all alternating parities along consecutive 
elements of the same parity

Within each such partition, any subarray is legal.
The challenge now is to find the contiguous subarray with the max sum...

n <= 2x10^5 -> n^2 would be too slow, cannot compute all possible nC2 
subintervals...

Consider the prefix sum array `s`
We want to pick i,j such that s[j]-s[i] is maximal
Suppose we fix j
We want to pick i from i=0,1,...,j-1 such that s[i] is minimal
This can be done by taking the min prefix array of s
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    ans = -999999

    #i is in same_par iff a[i-1] and a[i] have the same parity
    same_par = [0]
    for i in range(n-1):
        if (a[i+1]-a[i])%2 == 0:
            same_par.append(i+1)
    same_par.append(n)

    #Split a into maximal contiguous subarrays of alternating parity
    for Kumi in range(len(same_par)-1):
        a_ = a[same_par[Kumi]:same_par[Kumi+1]]

        #s[i] = sum of first i elements of a_
        s = [0]
        for i in range(len(a_)):
            s.append(s[-1]+a_[i])

        #Debug
        #print(len(a_),len(s))
        
        #pre_min_s[i] = minimum of first i elements of s
        pre_min_s = [s[0]]
        for i in range(len(s)):
            pre_min_s.append( min(pre_min_s[-1],s[i]) )

        #For each possible right end R
        for R in range(1,len(s)):
            ans = max(ans, s[R]-pre_min_s[R])

    
    #DEBUG
    # print(same_par)
        
    print(ans)
