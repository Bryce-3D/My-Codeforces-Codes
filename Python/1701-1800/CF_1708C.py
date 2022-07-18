#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Trace from the end?
Probably best to tank IQ towards the end.
Make some sort of a suffix array where
    suffix[i] = min IQ needed to handle the last I stuff
Then once suffix[i] = initial IQ then only take the ones that have 
difficulty < IQ?
'''

for Homu in range(int(input())):
    n,IQ = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    ind = n
    req = 0
    ans = []

    for i in range(n-1,-1,-1):
        if req == IQ:   #Only accept manageable rounds
            if a[i] <= IQ:
                ans.append('1')
            else:
                ans.append('0')
        else:   #Accepting everything at the end
            ans.append('1')
            if req < a[i]:   #If need extra IQ to take the end
                req += 1
    
    ans.reverse()
    ans = ''.join(ans)
    print(ans)
