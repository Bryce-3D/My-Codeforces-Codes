from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA

'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    prod = 1
    for i in b:
        prod *= i
    
    if 2023%prod == 0:
        print('YES')
        ans = [1 for i in range(k)]
        ans[0] = 2023//prod
        ans = [str(i) for i in ans]
        ans = ' '.join(ans)
        print(ans)
    else:
        print('NO')
