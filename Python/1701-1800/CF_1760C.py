#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Only need to track top 2

Also what the fuck vscode why do you suddenly 
not have a linter installed wasted like 10 mins
'''

for Homu in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]

    M0, M1 = max(l[0],l[1]), min(l[0], l[1])
    for i in range(2,n):
        if l[i] >= M0:
            M0, M1 = l[i], M0
        elif l[i] >= M1:
            M1 = l[i]
        #else: no update
    
    ans = []
    for i in range(n):
        next = l[i]
        if next == M0:
            ans.append(next - M1)
        else:
            ans.append(next - M0)
    
    ans = [str(i) for i in ans]
    ans = ' '.join(ans)
    print(ans)
