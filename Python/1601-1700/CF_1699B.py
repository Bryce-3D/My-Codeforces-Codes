#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    r,c = [int(i) for i in input().split()]

    row0 = ['0' for i in range(c)]
    row1 = ['0' for i in range(c)]

    for i in range(c):
        if i%4 == 0 or i%4 == 3:
            row0[i] = '1'
        else:
            row1[i] = '1'
    
    row0 = ' '.join(row0)
    row1 = ' '.join(row1)

    for i in range(r):
        if i%4 == 0 or i%4 == 3:
            print(row0)
        else:
            print(row1)
