#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
An operation is basically taking 2 adjacent distinct digits 
and deleting the left of them.

Therefore, a binary string is paranoid iff it's last 2 digits 
are distinct. (?)

Yeh reduce to either 010101... then finish it off
'''

for Homu in range(int(input())):
    n = int(input())
    s = input()

    ans = n   #Count strings of length 1
    for i in range(1,n):   #Substring ends at index i
        if s[i] != s[i-1]:
            ans += i
    
    print(ans)
