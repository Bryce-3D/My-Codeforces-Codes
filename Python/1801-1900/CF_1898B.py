#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Suppose that a_i splits into n_i numbers
Then you can always make everything be ceil(a_i/n_i) and floor(a_i/n_i)

You split each number from right to left splitting as little as possible 
each time.
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    cap = a[-1]   #Upper bound/capacity
    ans = 0

    for i in range(n-2,-1,-1):
        x = a[i]

        #No need to split
        if x <= cap:
            cap = x
            continue

        #Need to split
        n = (x-1)//cap + 1   #ceil(x/cap) = number of terms to split into
        cap = x//n           #Smallest value when x is split into n parts
        ans += n-1
    
    print(ans)
