#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
INDUCTION => gcd(a_i,i) = i for all i
'''

for Homu in range(int(input())):
    n,L,R = [int(i) for i in input().split()]

    possible = True
    ans = []

    for k in range(1,n+1):
        rem = L%k
        x = L-rem
        if rem != 0:
            x += k
        
        if x <= R:
            ans.append(x)
        else:
            possible = False
            break
    
    if possible:
        print('YeS')
        ans = [str(i) for i in ans]
        ans = ' '.join(ans)
        print(ans)
    else:
        print('nO')
