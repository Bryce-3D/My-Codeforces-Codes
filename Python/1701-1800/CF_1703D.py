#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Why is anything I think of O(n^2)

WAIT DO OTHER WAY
Instead of find substrings that concatenate together to make s, 
break s apart and check if the 2 halves exist
O(7n) = O(n)
Use a hash to store what exists
'''

for Homu in range(int(input())):
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    
    exist = set()
    for s in strings:
        exist.add(s)
    
    ans = ['0' for i in range(n)]
    for i in range(n):
        s = strings[i]
        l = len(s)
        for cut in range(1,l):
            s1 = s[0:cut]
            s2 = s[cut:l]
            if s1 in exist and s2 in exist:
                ans[i] = '1'
    
    ans = ''.join(ans)
    print(ans)
