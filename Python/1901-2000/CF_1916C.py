from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Masha maximize -> wants to pick same parity
Olya minimize  -> wants to pick diff parity

Result of an op is always even
Olya needs odds to minimize
Therefore, Masha would try to pair up odds as quickly as possible

'''

#loss(o,n) = lost sum given o odds and n numbers
def loss(o,n):
    if n == 1:
        return 0
    if o%2 == 0:
        return 2*( (o+2)//6 )
    else:
        return 2*( (o-1)//6 ) + 1

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    pre_sum = [0]
    for i in range(n):
        pre_sum.append(pre_sum[-1]+a[i])
    
    pre_n_odd = [0]
    for i in range(n):
        if a[i]%2 == 0:
            pre_n_odd.append(pre_n_odd[-1])
        else:
            pre_n_odd.append(pre_n_odd[-1]+1)
    
    losses = [loss(pre_n_odd[i],i) for i in range(n+1)]

    # print(f'losses = {losses}')

    ans = [pre_sum[i+1]-losses[i+1] for i in range(n)]
    ans = [str(i) for i in ans]
    ans = ' '.join(ans)
    print(ans)
