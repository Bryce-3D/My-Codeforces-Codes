#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #Prefix array
    a_pre_sum = [0]
    for i in range(n):
        next = a_pre_sum[-1] + a[i]
        a_pre_sum.append(next)
    
    #exists[i] = True iff i <= n and i is a possible sum
    exists = [False for i in range(n+1)]
    for i in range(n+1):
        for j in range(i+2,n+1):
            Sum = a_pre_sum[j] - a_pre_sum[i]
            if Sum <= n:
                exists[Sum] = True
    
    ans = 0
    for i in a:
        if exists[i] == True:
            ans += 1
    print(ans)
