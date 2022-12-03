#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Valley iff rightmost dec to left of leftmost inc
    ... \ / ...
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    max_dec = -1    #max index i such that a[i] > a[i+1]
    min_inc = n-1   #min index i such that a[i] < a[i+1]

    for i in range(n-1):
        if a[i] > a[i+1]:
            max_dec = i
        elif a[i] < a[i+1]:
            min_inc = min(i, min_inc)
    
    if max_dec < min_inc:
        print('YeS')
    else:
        print('nO')
