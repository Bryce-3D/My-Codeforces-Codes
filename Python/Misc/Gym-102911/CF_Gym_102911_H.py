'''NOTE
This got 70/100 points
'''

n = int(input())
hs = [ int(i) for i in input().split() ]
ws = [ int(i) for i in input().split() ]
 
total = 0
for z in range(n-1):
    i = hs.index( min(hs) )
    lefts = 0
    for j in range(i):
        lefts += ws[j]
    total += lefts*ws[i]
 
    hs.pop(i)
    ws.pop(i)
 
print(total)
