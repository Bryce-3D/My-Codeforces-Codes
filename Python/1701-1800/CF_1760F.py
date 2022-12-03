#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Given a k, it seems it shouldn't be too hard to find the 
maximum amount that can be earned in d days.
Binary search for k?

Infinity - Doing the best min(d,n) quests is enough
Impossible - Doing the best quest on all d days is not enough
'''

for Homu in range(int(input())):
    n,c,d = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    
    #Sort a in descending order
    a.sort()
    a = a[::-1]

    #pre_sum[i] = value of i best quests
    pre_sum = [0]
    for i in range(n):
        next = pre_sum[-1] + a[i]
        pre_sum.append(next)

    #Deal with corner cases
    if pre_sum[min(d,n)] >= c:
        print('Infinity')
    elif a[0] * d < c:
        print('Impossible')
    
    #Main case
    else:
        #The answer will always be in the range [L:R]
        L,R = 0,1

        #Double R until k=R cannot work
        while True:
            cyc = d // (R+1)       #Number of full cycles of R+1 quests
            rem = d % (R+1)        #Number of remaining quests in the last cycle
            rem = min(n, rem)
            cyc_len = min(R+1,n)   #Number of quests per cycle (cannot exceed n)

            #Compare profit when k = R+1
            profit = cyc * pre_sum[cyc_len] + pre_sum[rem]
            if profit < c:   #If not enough
                break        #Stop
            else:            #If still enough
                R *= 2       #Double R
        
        #Binary search in [L:R]
        while R-L > 1:
            M = (L+R)//2   #Middle

            #Check if k=M works
            cyc = d // (M+1)       #Number of full cycles of M+1 quests
            rem = d % (M+1)        #Number of remaining quests in the last cycle
            rem = min(n, rem)
            cyc_len = min(M+1,n)   #Number of quests per cycle (cannot exceed n)
            #Max profit when k = M
            profit = cyc * pre_sum[cyc_len] + pre_sum[rem]
            if profit < c:   #If M is too big
                R = M        #Go left
            else:            #If M still works
                L = M        #Go right
        
        print(L)
