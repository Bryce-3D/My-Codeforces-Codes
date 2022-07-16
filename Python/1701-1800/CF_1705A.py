#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n,x = [int(i) for i in input().split()]
    heights = [int(i) for i in input().split()]

    heights.sort()
    possible = True
    for i in range(n):
        if heights[i+n] - heights[i] < x:
            possible = False
            break

    if possible:
        print('YeS')
    else:
        print('nO')
