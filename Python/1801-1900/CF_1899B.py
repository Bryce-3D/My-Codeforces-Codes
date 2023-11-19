#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Given n boxes
k boxes will go to each truck
We want k such that the diff between max truck and min truck is as small as 
possible.

Check all n possible values of k?
O(n) check if div
O(sigma(n)) < O(nlgn) to check each case
Can use a prefix sum array to make queries faster
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #s_a[i] = sum of first i elements of a
    s_a = [0]
    for i in range(n):
        s_a.append(s_a[-1]+a[i])

    #Record the best ans
    ans = -1

    #Check all possible values of k
    for k in range(1,n+1):
        #Skip if not divisible
        if n%k != 0:
            continue

        m = s_a[k]   #Min weight truck
        M = s_a[k]   #Max weight truck
        
        L,R = 0,k       #Left and right end of array
        trucks = n//k   #Number of trucks

        #For each truck
        for Kumi in range(trucks):
            #Get the total
            tot = s_a[R] - s_a[L]
            #Update the max and min
            m = min(tot,m)
            M = max(tot,M)
            #Increment to the next truck
            L += k
            R += k
        
        ans = max(M-m,ans)
    
    print(ans)
