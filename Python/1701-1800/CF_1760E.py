#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Inversion iff 1 to left of 0

pre_1 = Prefix array with number of 1s
suf_0 = SUffix array with number of 0s
can calculate number of inversions in O(n) time with this

To find the effect of a change on k:
    (a0 0s, a1 1s) k (b0 0s, b1 1s)
k changes 0 -> 1:
    Delta = -a1 + b0 
k changes 1 -> 0:
    Delta = a1 - b0
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #pre_1[i] = number of 1s among the first i numbers
    pre_1 = [0]
    for i in range(n):
        if a[i] == 0:
            next = pre_1[-1]
        else:
            next = pre_1[-1]+1
        pre_1.append(next)
    
    #suf_0[i] = number of 0s among the last i numbers
    suf_0 = [0]
    for i in range(n):
        if a[-i-1] == 1:
            next = suf_0[-1]
        else:
            next = suf_0[-1]+1
        suf_0.append(next)
    
    #Count number of inversions by 
    #    sum_{indices with 0} (number of 1s to the left)
    count = 0
    for i in range(n):
        if a[i] == 0:
            count += pre_1[i]   #i numbers before a[i]
    
    #Find the flip with the best improvement 
    #(or possibly just leave as is)
    max_delta = 0
    for i in range(n):
        #i numbers before and n-1-i numbers after a[i]
        if a[i] == 0:
            delta = suf_0[n-1-i] - pre_1[i]
        else:
            delta = pre_1[i] - suf_0[n-1-i]
        max_delta = max(delta, max_delta)
    
    #Add together and print the ans
    print(count + max_delta)
