#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Get the count of each mod 10 first, actual value is irrelevant.
'''

for Homu in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]

    #c[i] returns the number of numbers that are i mod 10
    c = {}
    for i in range(10):
        c[i] = 0
    for num in nums:
        mod = num%10
        c[mod] += 1
    
    #BASH
    #Sum = 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if c[0] > 1 and c[3] > 0:                  #003
        print('YeS')
    elif c[0] > 0 and c[1] > 0 and c[2] > 0:   #012
        print('YeS')
    elif c[1] > 2:                             #111
        print('YeS')
    #Sum = 13 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif c[0] > 0 and c[4] > 0 and c[9] > 0:   #049
        print('YeS')
    elif c[0] > 0 and c[5] > 0 and c[8] > 0:   #058
        print('YeS')
    elif c[0] > 0 and c[6] > 0 and c[7] > 0:   #067
        print('YeS')
    elif c[1] > 0 and c[3] > 0 and c[9] > 0:   #139
        print('YeS')
    elif c[1] > 0 and c[4] > 0 and c[8] > 0:   #148
        print('YeS')
    elif c[1] > 0 and c[5] > 0 and c[7] > 0:   #157
        print('YeS')
    elif c[1] > 0 and c[6] > 1:                #166
        print('YeS')
    elif c[2] > 1 and c[9] > 0:                #229
        print('YeS')
    elif c[2] > 0 and c[3] > 0 and c[8] > 0:   #238
        print('YeS')
    elif c[2] > 0 and c[4] > 0 and c[7] > 0:   #247
        print('YeS')
    elif c[2] > 0 and c[5] > 0 and c[6] > 0:   #256
        print('YeS')
    elif c[3] > 1 and c[7] > 0:                #337
        print('YeS')
    elif c[3] > 0 and c[4] > 0 and c[6] > 0:   #346
        print('YeS')
    elif c[3] > 0 and c[5] > 1:                #355
        print('YeS')
    elif c[4] > 1 and c[5] > 0:                #445
        print('YeS')
    #Sum = 23 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif c[5] > 0 and c[9] > 1:                #599
        print('YeS')
    elif c[6] > 0 and c[8] > 0 and c[9] > 0:   #689
        print('YeS')
    elif c[7] > 1 and c[9] > 0:                #779
        print('YeS')
    elif c[7] > 0 and c[8] > 1:                #788
        print('YeS')

    else:                                      #Fails
        print('nO')
