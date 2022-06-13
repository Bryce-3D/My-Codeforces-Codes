#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Relative position of a and c are fixed.
Therefore, the strings when b's are deleted need to be identical.
Also there's the obvious part of equal counts of a,b,c but this 
is guaranteed by the above condition.

Basically b's can either move to the left of a's or to the right of c's.
a's and c's count as 1 way gates kinda

Another way to look at it:
a and c in a sea of b's
a's can go right, c's can go left
'''

for Homu in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()

    while True:
        #Check if possible
        possible = True

        #a's and c's of s1 and s2 in order
        s1_non_b_char = []
        s2_non_b_char = []
        #Indices of non b chars in s1 and s2
        s1_non_b_ind = []
        s2_non_b_ind = []
        for i in range(n):
            if s1[i] != 'b':
                s1_non_b_char.append(s1[i])
                s1_non_b_ind.append(i)
            if s2[i] != 'b':
                s2_non_b_char.append(s2[i])
                s2_non_b_ind.append(i)


        #If a's and c's not same order, stop
        if s1_non_b_char != s2_non_b_char:
            print('NO')
            break


        #Number of non b chars
        l = len(s1_non_b_char)
        #If any pair of a's or c's are in the wrong order, stop
        #a of s2 must be to the right of a of s1
        #c of s2 must be to the left of c of s1
        for i in range(l):
            if s1_non_b_char[i] == 'a':
                if s1_non_b_ind[i] > s2_non_b_ind[i]:   #If a in s1 to right of s2
                    possible = False
                    break
            else: #s1_non_b_char[i] == 'c'
                if s1_non_b_ind[i] < s2_non_b_ind[i]:   #If c in s1 to left of s2
                    possible = False
                    break
        
        #Check if indices satisfied the order
        if not possible:
            print('NO')
            break
        
        print('YES')
        break
        
