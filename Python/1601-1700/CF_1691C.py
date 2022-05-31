#For fast I/O
from email.mime import base
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Basically the value is
    11 * (sum of digits of s) - (first dig of s) - 10 * (last dig of s)
Therefore we want to ideally have 1s at the end


Code flow:

If s has 0 1s:
    Nothing to do, print ans
elif s has 1 1s:
    If can move 1 to the end:
        ans
    elif can move 1 to front:
        ans
    elif can't reach the ends:
        ans
elif s has 2 1s:
    If can move back/frontmost to back/front:
        ans
    elif backmost 1 can reach back:
        ans
    elif frontmost 1 can reach front:
        ans
    elif neither can reach the ends:
        ans
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]
    s = input()

    #Calculate base score first
    digits = [int(i) for i in s]
    base_score = 11*sum(digits) - digits[0] - 10*digits[-1]

    n1 = s.count('1')

    #If 0 1s
    if n1 == 0:
        print(base_score)
    
    #If 1 1s
    elif n1 == 1:
        ind = s.index('1')
        if ind == n-1:       #If 1 is already at the back
            print(base_score)
        elif n-1 <= k and ind == 0:   #SPECIAL CASE!!! If 1 can move from front to back
            print(base_score - 9)
        elif n-ind-1 <= k:   #If 1 can move to back from middle
            print(base_score - 10)
        elif ind == 0:       #If 1 is already at the front
            print(base_score)
        elif ind <= k:       #If 1 can move to the front
            print(base_score - 1)
        else:
            print(base_score)
    
    #If >1 1s
    else:
        i_L = 0     #Index of leftmost 1
        while s[i_L] != '1':
            i_L += 1
        i_R = n-1   #Index of rightmost 1
        while s[i_R] != '1':
            i_R -= 1
        
        #If already ideal
        if i_L == 0 and i_R == n-1:
            print(base_score)
        #If only back is already ideal
        elif i_R == n-1:
            if i_L <= k:       #If left 1 can move to front
                print(base_score - 1)
            else:              #If left 1 cannot move to front
                print(base_score)
        #If only front is already ideal
        elif i_L == 0:
            if n-i_R-1 <= k:   #If right 1 can move to back
                print(base_score - 10)
            else:              #If right 1 cannot move to back
                print(base_score)
        #If neither ends are ideal
        else:
            if (n-i_R-1) + i_L <= k:   #If both ends can be optimized
                print(base_score - 11)
            elif n-i_R-1 <= k:         #If only back can be optimized
                print(base_score - 10)
            elif i_L <= k:             #If only front can be optimized
                print(base_score - 1)
            else:                      #If neither end can be optimized
                print(base_score)
