#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    h = [int(i) for i in input().split()]
    k = n//2

    if n%2 == 1:
        ans = 0
        for i in range(k):
            ind = 2*i+1
            if h[ind] <= max(h[ind-1],h[ind+1]):
                ans += max(h[ind-1],h[ind+1]) - h[ind] + 1
        print(ans)
    else:
        #coolify[i] is the number of floors needed to make the (i+1)-th building cool (0-indexed)
        coolify = [-1]
        for i in range(1,n-1):
            next = 0
            if h[i] <= max(h[i-1],h[i+1]):
                next = max(h[i-1],h[i+1]) - h[i] + 1
            coolify.append(next)
        
        #odd_cooling[i] is the floors needed to coolify the first i odd indices
        odd_cooling = [0]
        for i in range(k-1):
            ind = 2*i+1
            next = odd_cooling[-1] + coolify[ind]
            odd_cooling.append(next)
        #even_cooling[i] is the floors needed to coolify the last i even indices
        even_cooling = [0]
        for i in range(k-1):
            ind = n - 2*i - 2
            next = even_cooling[-1] + coolify[ind]
            even_cooling.append(next)

        #possible[i] is the ans if 1,3,...,2i-1,2i+2,2i+4,...,n-2 are coolified
        possible = [odd_cooling[i]+even_cooling[-i-1] for i in range(k)]
        ans = min(possible)
        print(ans)
