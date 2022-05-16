#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
Given a person of weight p
Cannot fit - [0, p)
Like       - [p, 2p]
Dislike    - (2p, inf)

v1 > v2 > v3 >= 1, vm
c1 > c2 > c3

Need:
v1, 2vm+1 <= c1 <= 2v1
v2, 2vm+1 <= c2 <= 2v2
v3, vm    <= c3 <= 2v3, 2vm

Ideally,
    c1 = 2v1
    c2 = 2v2
    c3 = max(v3, vm)
This fails iff one of the ff holds
     - max(v3,vm) > 2*min(v3,vm)
     - v2 <= vm
'''

Homu = [int(i) for i in input().split()]
v1 = Homu[0]
v2 = Homu[1]
v3 = Homu[2]
vm = Homu[3]

if max(v3,vm) <= 2*min(v3,vm) and v2 > vm:
    print(2 * v1)
    print(2 * v2)
    print(max(v3,vm))
else:
    print(-1)
