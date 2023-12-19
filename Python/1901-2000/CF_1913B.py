from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Find maximal prefix such that 
    #0s in prefix <= #1s in whole string
    #1s in prefix <= #0s in whole string
'''

for Homu in range(int(input())):
    s = input()
    l = len(s)

    a0 = [0]
    a1 = [0]
    for i in range(l):
        if s[i] == '0':
            a0.append(a0[-1]+1)
            a1.append(a1[-1])
        else:
            a0.append(a0[-1])
            a1.append(a1[-1]+1)
    
    ind = l
    while a0[ind] > a1[-1] or a1[ind] > a0[-1]:
        ind -= 1
    
    ans = l-ind
    print(ans)
