from collections import deque as dq
from itertools import permutations

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
CHEESE WITH 16900000

169000000...
106090000...
100600900...
...

961000000...
906010000...
900600100...
...

196000000...
610090000...
'''



for Homu in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue

    k = n//2
    for i in range(k):
        s = '1' + '0'*i + '6' + '0'*i + '9' + '0'*(n-2*i-3)
        print(s)
        s = '9' + '0'*i + '6' + '0'*i + '1' + '0'*(n-2*i-3)
        print(s)
    s = '196' + '0'*(n-3)
    print(s)
