#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
WLOG let x >= y
    (2^x,2^y) = (2^y,2^x)
<=> x * 2^y = y * 2^x
<=> x/y = 2^(x-y)

Let x = k+y
<=> 1 + k/y = 2^k

x=y -> good
x>y -> k>1 and get

k+1 >= k/y + 1 = 2^k

Only y=1, k=1 can satisfy this

Therefore the only pairs that works are
    x=y
    {x,y} = {1,2}


UPSOLVING
Got hacked gdi must be hash collision again
'''
import random
salt = random.randint(0,1023)

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #count[i] = number of occurences of i in a
    count = {}
    for i in a:
        if i^salt in count:
            count[i^salt] += 1
        else:
            count[i^salt] = 1
    
    ans = 0
    #Number of pairs such that x=y
    for i in count:
        c = count[i]
        ans += (c*(c-1))//2
    
    #Number of pairs such that {x,y}={1,2}
    if (1^salt in count) and (2^salt in count):
        ans += count[1^salt]*count[2^salt]
    
    print(ans)
