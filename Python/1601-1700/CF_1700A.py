#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Stay at top then at right.
[1+2+...+(C-1)] + (C+2C+...+RC)
= (C-1)(C)/2 + CR(R+1)/2
'''

for Homu in range(int(input())):
    R,C = [int(i) for i in input().split()]
    ans = (C-1)*C // 2 + C*R*(R+1) // 2
    print(ans)
