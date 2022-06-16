#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
You can always pair a move right with a move left.
+a -a
   +b -b
      +c -c
         +d -d
            ...

Basically prefix_sum >= 0 all the time 
and total sum = 0

Wait 1 -1 1 -1 test case
Need to have prefix_sum > 0 to continue forward.

Need prefix_sum > 0 until the last nonzero square where it 
should become prefix_sum = 0 then end.

basically prefix sum is:
    0 >0 >0 ... >0 0 0 ... 0
    0, all positive, all 0s
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #pre_sum[i] returns he sum of the first i elements
    pre_sum = [0]
    for i in range(n):
        next = pre_sum[-1] + a[i]
        pre_sum.append(next)
    
    if pre_sum[-1] != 0:   #If total != 0
        print('nO')
    else:
        #sign[i] = 1,0,-1 is pre_sum[i+1] is pos, 0, or neg
        sign = []  
        for i in range(1,n+1):
            if pre_sum[i] > 0:
                sign.append(1)
            elif pre_sum[i] == 0:
                sign.append(0)
            else:
                sign.append(-1)
        
        if -1 in sign:   #If there's a negative
            print('nO')
        else:
            #Find the first 0 in sign
            first_zero = 0
            while first_zero < n and sign[first_zero] != 0:
                first_zero += 1
            
            #Check if the rest are all 0s
            if sum(sign[first_zero::]) == 0:
                print('YeS')
            else:
                print('nO')
