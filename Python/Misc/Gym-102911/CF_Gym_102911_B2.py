'''NOTE
This got 80/100 points
'''

#link to prblems: https://codeforces.com/gym/102911
 
from sys import *
 
yeet = [ int(i) for i in stdin.readline().split() ]
n = yeet[0]
k = yeet[1]
row = [ int(i) for i in stdin.readline().split() ]
 
if k>2:
    total = 0
 
    req = 0
    for j in range(k):
        for z in range(n):
            if row[z] == j+1:
                req = max(req,z)
                break
    total += n - req
 
    for i in range(1,n):
        removed = row[i-1]
        if removed in row[i:req+1]:
            total += n - req
        else:
            try:
                for j in range(req+1,n+1):
                    if row[j] == removed:
                        req = j
                        total += n - req
                        break
            except:
                break
    
    print(total)
 
elif k == 2:
    swaps = [0]
    for i in range(n-1):
        if row[i] != row[i+1]:
            swaps.append(i+1)
    swaps.append(n)
    l = len(swaps)
    
    block = []
    for i in range(l-1):
        block.append( swaps[i+1]-swaps[i] )
    
    invalid = 0
    for i in range(l-1):
        invalid += block[i]*(block[i]+1)//2
 
    print( n*(n+1)//2 - invalid )
    
 
else:
    print( n*(n+1)//2 )
