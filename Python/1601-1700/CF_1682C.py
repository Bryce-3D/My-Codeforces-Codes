#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Basically force it out and make it symmetric kinda
Suppose
    a values with 1 copy
    b values with >1 copy
If max or min value has only one copy
    a -= 1
    b += 1
This is because it can be used as a pivot and count for both
Ans is
    b + floor(a/2)

ERROR:
Can intertwine the two sequences and set the largest solo as their 
intersection, so you can always reduce solo by 1
'''

for Homu in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    #Max = max(l)
    #Min = min(l)
    counts = {}   #counts[i] returns the number of instances of i in l
    for x in l:
        if x in counts:   #Already appeared
            counts[x] += 1
        else:             #New distinct value
            counts[x] = 1
    
    #Counting number of solos and dupes
    solo = 0
    dupe = 0
    for i in counts:
        if counts[i] == 1:
            solo += 1
        else:
            dupe += 1
    #Taking into account using max or min as a pivot
    if solo > 0:
        solo -= 1
        dupe += 1
    
    ans = solo//2 + dupe
    print(ans)
