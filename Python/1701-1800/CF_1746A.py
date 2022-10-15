#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Only operation 2 can kill 0s
If there's at least 1 0 left, you must do operation 2

Wait I only need at least one 1 with an array of length k to win.
Strat: spam min pairs such that you always leave at least one 1 left 
until you have k terms left then max

When k = 2:
    Just spam max, works iff there's at least one 1
When k = 3:
    xxx...xxx 1 yyy...yyy
    x1y or xx1 or 1yy (x+y >= 2 so one of these *will* work)
'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    if sum(a) > 0:
        print('YES')
    else:
        print('NO')
