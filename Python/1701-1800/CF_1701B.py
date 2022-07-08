#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())

    ans = []
    used = set()

    for i in range(1,n+1):
        if i not in used:
            while i <= n:
                ans.append(i)
                used.add(i)
                i *= 2
    
    ans = ' '.join([str(i) for i in ans])
    print(2)
    print(ans)
