from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Max val is 2^29 * 10^5 < 2^46
O(46) per check should be fine
'''

S = {}   #Multiset as a dict

for Homu in range(int(input())):
    Kumi,v = [int(i) for i in input().split()]

    #ADD v
    if Kumi == 1:
        if v in S:
            S[v] += 1
        else:
            S[v] = 1
        continue

    #GET v_i
    S0 = {}
    for i in S:
        S0[i] = S[i]
    
    pow = 0   #Pow of 2 rn
    possible = True
    while v != 0:
        if v%2 == 0:
            if pow in S0:
                if (pow+1) in S0:
                    S0[pow+1] += S0[pow]//2
                else:
                    S0[pow+1] = S0[pow]//2
        else:
            if pow not in S0 or S0[pow] == 0:
                possible = False
                break
            S0[pow] -= 1
            if (pow+1) in S0:
                S0[pow+1] += S0[pow]//2
            else:
                S0[pow+1] = S0[pow]//2

        #DEBUG
        #print(S0)
        
        v >>= 1
        pow += 1
    
    if possible:
        print('YES')
    else:
        print('NO')
