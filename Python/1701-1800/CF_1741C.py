#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Ideas
n <= 2000, t <= 100
tn^2 -> 4 * 10^8?

Check if the first k elements are together from k=1 to n
Can also stop it once the sum of the first k elements > half the total
Can also stop it if the sum of the first k elements doesn't divide the total
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #pre_sum[i] = sum of first i elements of a
    pre_sum = [0]
    for i in range(n):
        next = pre_sum[-1] + a[i]
        pre_sum.append(next)

    
    ans = n
    #Check all positive first segments
    for k in range(1,n+1):
        s = pre_sum[k]   #Common sum to be used
        if pre_sum[-1] < 2*s:
            break
        if pre_sum[-1] % s != 0:
            continue

        width = k
        #Segment stored in a[L:R]
        L = k
        R = k
        curr_sum = 0
        possible = True
        while R < n:
            curr_sum += a[R]
            R += 1
            if curr_sum > s:      #If segment exceeds
                possible = False
                break
            elif curr_sum == s:   #If segment is filled
                width = max(R-L, width)
                L = R
                curr_sum = 0
        
        if possible and curr_sum == 0:
            ans = min(width, ans)
    
    print(ans)
