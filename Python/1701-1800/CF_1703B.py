#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    s = input()

    ans = 0
    solved = [False for i in range(26)]

    for q in s:
        i = ord(q) - ord('A')
        if solved[i]:
            ans += 1
        else:
            solved[i] = True
            ans += 2
    
    print(ans)
