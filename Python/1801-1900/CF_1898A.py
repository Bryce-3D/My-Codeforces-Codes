#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Want k instances of B

= k -> Do nothing
> k -> replace front with A's till it works
< k 
'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    s = input()

    k0 = s.count('B')

    if k0 == k:
        print(0)
        continue
    print(1)
    
    if k0 > k:
        d = k0-k   #Number of B's that should change to A
        i = 0
        while True:
            if s[:i].count('B') == d:
                print(i, 'A')
                break
            else:
                i += 1
    else:   #k0 < k
        d = k-k0   #Number of A's that should change to B
        i = 0
        while True:
            if s[:i].count('A') == d:
                print(i, 'B')
                break
            else:
                i += 1
