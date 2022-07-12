#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Can probably induct from back end to front end?
But how to track number of odd numbers, cause the rounding error 
can pose an issue. (No way to distinguish between 3,0,0 and 1,1,1. When 
halved, one becomes 1,0,0, other becomes 0,0,0)

Maybe can do a bigger dp?
    dp[b,m] is the maximum profit from the last n-m chests after having 
    b bad keys among the first m chests.

Then we'd have
    dp[b,m] = max(dp[b,m+1]-k + (m+1)-th chest after b bad keys, 
                  dp[b+1,m+1] + (m+1)-th chest after b+1 bad keys)
*(m+1)-th here is not 0-indexed

Since the number of coins per chest is at most 10^9, then 30 bad keys is 
guaranteed to make everything 0. So we can instead make dp[m,30] be the 
max profit after having at least 30 keys, and it'll just be 0 cause by then 
you'd just spam bad keys all the way.

This is O(30n) so it shud work???

Fill up dp by filling up the bottom row (b=30) and rightmost column (m=n) first 
with all 0s and then go b=29 from right to left, b=28 from right to left, and so on
'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    #dp[b][m] returns the maximum profit that can be obtained from the 
    #remaining chests after b bad keys have been used for the first m chests
    dp = [[0 for i in range(n+1)] for j in range(31)]

    for b in range(29,-1,-1):
        for m in range(n-1,-1,-1):
            curr_chest = a[m]
            for i in range(b):
                curr_chest //= 2
            
            good = dp[b][m+1] - k + curr_chest
            bad = dp[b+1][m+1] + curr_chest//2

            best = max(good,bad)
            dp[b][m] = best
    
    print(dp[0][0])
