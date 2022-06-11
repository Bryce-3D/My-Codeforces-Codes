#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Greedily take the lesser character between the two strings until 
one of the strings is empty.
Also make sure to not exceed k consecutive.
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    l1,l2,k = Kumi
    s1 = input()
    s2 = input()

    s1 = [i for i in s1]
    s1.sort()
    s1 = s1[::-1]

    s2 = [i for i in s2]
    s2.sort()
    s2 = s2[::-1]

    #Track number of consecutive moves
    c1 = 0
    c2 = 0

    ans = []
    while len(s1) != 0 and len(s2) != 0:
        if c1 == k:
            c1 = 0
            c2 = 1
            ans.append(s2.pop())
        elif c2 == k:
            c1 = 1
            c2 = 0
            ans.append(s1.pop())
        elif s1[-1] < s2[-1]:
            c1 += 1
            c2 = 0
            ans.append(s1.pop())
        else: #s1[-1] > s2[-1]
            c1 = 0
            c2 += 1
            ans.append(s2.pop())
    
    ans = ''.join(ans)
    print(ans)
