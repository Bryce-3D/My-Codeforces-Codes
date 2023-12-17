from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
Read the editorial
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    #Generate the initial prefix MEX list
    seen = [False for i in range(n)]
    ind = 0
    pre_MEX = []
    for i in range(n):
        #Mark the ith element as seen
        seen[a[i]] = True
        #Move ind up until the smallest unseen element
        while ind < n and seen[ind] == True:
            ind += 1
        #Record the MEX of the first (i+1) elements
        pre_MEX.append(ind)
    
    #Find the cost of the original permutation
    cost = sum(pre_MEX)
    ans = cost

    #Compress pre_MEX into [MEX, count] form in a deque
    pre_MEX_com = dq()
    v = pre_MEX[0]   #Value of current chain
    c = 0            #Count of current chain
    for k in pre_MEX:
        #Chain continues
        if v == k:
            c += 1
            continue
        #Chain broken
        pre_MEX_com.append([v,c])
        v,c = k,1
    pre_MEX_com.append([v,c])

    #Iterate through the n-1 other cyclic shifts
    for i in range(n-1):
        #The ith element of the original permutation gets tossed out
        x = a[i]

        #Toss out the first prefix MEX from the prefix [x]
        cost -= pre_MEX_com[0][0]   #Update cost from removal
        if pre_MEX_com[0][1] == 1:
            pre_MEX_com.popleft()
        else:
            pre_MEX_com[0][1] -= 1
        
        #Nuke elements >x and replace them with x
        #Will always nuke at least one since the last element is always n
        c = 0   #Count of nuked elements
        #Nuke until empty or <=
        while len(pre_MEX_com) != 0 and pre_MEX_com[-1][0] > x:
            nuke = pre_MEX_com.pop()
            c += nuke[1]
            cost -= nuke[0]*nuke[1]   #Update cost from removal
        #Toss in newly formed x's
        if len(pre_MEX_com) != 0 and pre_MEX_com[-1][0] == x:
            pre_MEX_com[-1][1] += c
        else:
            pre_MEX_com.append([x,c])
        cost += x*c   #Update cost from addition
        
        #Append n to the end
        #Will always be alone since you need everything for MEX = n
        pre_MEX_com.append([n,1])
        cost += n   #Update cost from addition

        #Update ans if this is better
        ans = max(ans,cost)
    
    print(ans)
