#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = input()
    l = [int(n[i]) for i in range(6)]
    if l[0]+l[1]+l[2] == l[3]+l[4]+l[5]:
        print('YES')
    else:
        print('NO')
