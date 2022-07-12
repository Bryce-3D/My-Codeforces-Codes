#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Count the number of pairs (i,j) such that
    a_i < i < a_j < j

Clearly, any number in a pair must satisfy a_i < i
Given a j satisfying a_j < j, the number of possible i's that 
can pair up with j are the number of i's less than a_j such that a_i < i.

Use a "prefix count array", where 
    prefix[k] = number of integers i <= k such that a_i < i

Then the ans will be the sum of the terms of prefix corresponding to 
an index i satisfying a_i < i
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #prefix[k] = number of integers i <= k such that a_i < i
    #a_i here is 0 indexed
    prefix = [0]
    for i in range(n):
        if a[i] < i+1:
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])
    
    #Scan through all possible j's and add the number of pairs for each
    ans = 0
    for i in range(n):
        if a[i] < i+1 and a[i] > 0:   #Handle bug where a[i] = 0 makes a[i]-1=-1 and gets the last term
            ans += prefix[a[i]-1]
    
    print(ans)
