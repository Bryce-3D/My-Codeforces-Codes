#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
a_2 = 0 => a_1 | a_2
        => can make a_2 = a_1
        => a_3=0 iff a_1 | a_3
        => ...
a_1 must divide everything?
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    possible = True
    for i in range(1,n):
        if a[i] % a[0] != 0:
            possible = False
            break
    
    if possible:
        print('YeS')
    else:
        print('nO')
