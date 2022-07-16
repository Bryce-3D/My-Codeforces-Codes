#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
There is no reason to not be greedy (I think).
Whenever you move a dirt forward, you always move it 
as much as possible.

Always greedily move leftmost 
 -> kinda like sum of everything not at the end + number of 0s in the middle?
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #Leftmost nonzero index
    L = 0
    while L < n and a[L] == 0:
        L += 1
    
    #Number of middle 0s
    zeroes = 0
    for i in range(L,n-1):
        if a[i] == 0:
            zeroes += 1
    
    #Sum of all except end
    s = sum(a) - a[-1]

    print(s+zeroes)
