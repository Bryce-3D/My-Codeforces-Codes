#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n,l = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    s = ['B' for i in range(l)]

    for ind in a:
        i_1 = min(ind-1, l-ind)
        i_2 = max(ind-1, l-ind)

        if s[i_1] != 'A':
            s[i_1] = 'A'
        else:
            s[i_2] = 'A'
    
    s = ''.join(s)
    print(s)
