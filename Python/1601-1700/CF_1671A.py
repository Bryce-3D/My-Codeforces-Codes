#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#As long as there's no "single letter" only
for Homura in range(int(input())):
    possible = True
    s = input()
    a = 0
    b = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            a = b
            b = i+1
            if b-a == 1:
                possible = False
                break
    if len(s)-b == 1:
        possible = False
    if possible:
        print('YES')
    else:
        print('NO')
