#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        next = ord(s[i]) - ord('a')
        ans = max(next, ans) 
    print(ans+1)
