#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    s = input()
    k = n//2

    #Even case
    if n%2 == 0:
        i = k
        while i < n and s[i] == s[k]:
            i += 1
        count = i - k
        print(2 * count)
    #Odd case
    else:
        i = k
        while i < n and s[i] == s[k]:
            i += 1
        count = i-k
        print(2 * count - 1)
