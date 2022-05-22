#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
for all spots i with misplaced number j
Must have i and j in the same equiv class
'''

for Homu in range(int(input())):
    n = int(input())
    p = [int(i) for i in input().split()]

    ans = -1
    for i in range(n):
        if p[i] != i:
            cond = p[i] & i
            if ans == -1:
                ans = cond
            else:
                ans &= cond
    
    print(ans)
