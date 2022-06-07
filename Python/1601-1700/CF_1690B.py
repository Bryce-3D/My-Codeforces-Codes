#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Linear scan to get a[i] - b[i] for all
Note that the decrement amount must be max of this
Any more decrements can work iff it was already all 0s in b
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    diff = [a[i]-b[i] for i in range(n)]
    max_diff = max(diff)

    possible = True

    if max_diff < 0:
        possible = False
    else:
        for i in range(n):
            if diff[i] != max_diff and b[i] != 0:   #If the ith element doesn't match
                possible = False
                break
    
    if possible:
        print('YeS')
    else:
        print('nO')
