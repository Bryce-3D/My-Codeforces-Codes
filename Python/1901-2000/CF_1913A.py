from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA

'''

for Homu in range(int(input())):
    s = input()
    l = len(s)
    k = l//2

    if l%2 == 0:
        done = False
        for i in range(1,k):
            if s[i] != '0':
                print(s[:i],s[i:])
                done = True
                break
        if not done:
            if int(s[:k]) < int(s[k:]):
                print(s[:k], s[k:])
            else:
                print(-1)
    
    else:
        done = False
        for i in range(1,k+1):
            if s[i] != '0':
                print(s[:i], s[i:])
                done = True
                break
        if not done:
            print(-1)
