#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Do you just greedy each maximal sorted substring of the desired output?

Note that one you sort a substring, that area remains sorted even after 
you remove stuff from inside it.

Ok no my hypothesis seems to fail for the 4th example

15 7
anavolimilovana
aamanan

How is this a YES-instance wtf?

wait YOU CAN BRING THE `n` TO THE END HOLY HELL

    anavolimilovana
    anamilovana       (delete some characters)
    aanmilovana       (sort [1:3])
    aamnilovana       (sort [2:4])
    aamnana           (delete some characters)
    aamnaan           (sort [5:7])
    aamanan           (sort [3:5])

The "sort contiguous substring" operation can be represented as a series of 
"swap adjacent letters that are arranged wrongly"
Example:
    abc -> cba
    abc -> acb -> cab -> cba

In general we want to pick the leftmost possible one for larger letters and 
the rightmost one for smaller letters, since this gives the most flexibility 
in how to rearrange them.

Consider a smallest letter in the target string.
It cannot move to the right of any other character in the target string.
Therefore, everything after this smallest letter in the target string must 
come from after the current one.

Recursively divide along 'a', then 'b', then 'c', and so on until 'z'?



UPSOLVING

WAIT PROBLEM
You could potentially borrow only a limited part of the earlier component...
Perhaps this idea could be implemented on a per character basis instead?


After some discussion with someone else

Greedily find first instance of first character in target string.
Delete anything smaller than it in front from the original string (they are 
stuck there and cannot move forward).
It can be shown that this will work because it satisfies the greedy property.
Just repeat until target string is satisfied or you run out of stuff in the 
original string.

WAIT doing this naively would be O(n^2)...

From a friend
> can consider a queue of (indexes of) available characters (for each letter)
Ok I see, this would reduce it from O(n^2) to O(26n).
This is because you've kinda "precomputed where the characters are" and don't 
need to repeatedly go over the string every time.
'''

A = ord('a')

for Homu in range(int(input())):
    l0,l1 = [int(i) for i in input().split()]
    s0 = input()
    s1 = input()
    
    #d_s0[c] = list of indices remaining where char c is available
    d_s0 = {}
    for i in range(26):
        d_s0[chr(A+i)] = []
    #Store in reverse to easily pop smaller values from the end instead
    for i in range(l0-1,-1,-1):
        d_s0[s0[i]].append(i)



    possible = True
    #For each character in s1
    for C in s1:
        #Stop if no longer possible
        if len(d_s0[C]) == 0:
            possible = False
            break

        #Characters left after greedily getting the first C
        ind = d_s0[C].pop()   #Index from which C is taken
        for i in range(26):   #For each letter
            c = chr(A+i)
            #Stop once we reach C since they can pass
            if c >= C:
                break
            #For smaller chars, nuke all smaller indices
            while len(d_s0[c]) != 0 and d_s0[c][-1] < ind:
                d_s0[c].pop()
    
    if possible:
        print('YeS')
    else:
        print('nO')










#RECYCLING BIN ----------------------------------------------------------------
# a = ord('a')

# #Returns True if s0 can be changed into s1 and False otherwise
# def possible(s0,s1):
#     #Trivial cases
#     if len(s1) == 0:
#         return True
#     if len(s0) < len(s1):
#         return False
    
#     #countX[i] = number of instances of the ith letter in sX
#     count0 = {}
#     count1 = {}
#     for i in range(26):
#         count0[i] = 0
#         count1[i] = 0
#     for c in s0:
#         count0[ord(c)-a] += 1
#     for c in s1:
#         count1[ord(c)-a] += 1
    
#     #Trivial case
#     for i in range(26):
#         if count0[i] < count1[i]:
#             return False
    
#     #Find the "smallest letter" in s1
#     ind = 0
#     while count1[ind] == 0:
#         ind += 1
    
#     #Remove all smaller letters from s0 since they don't matter
#     s0_ = []
#     for c in s0:
#         if ord(c)-a >= ind:
#             s0_.append(c)
#     s0 = ''.join(s0_)

#     #Split s0 and s1 along the smallest letter
#     a_s0 = s0.split(chr(a+ind))
#     a_s1 = s1.split(chr(a+ind))

#     a_s0_ = []
#     for s in a_s0:
#         if s != '':
#             a_s0_.append(s)
#     a_s1_ = []
#     for s in a_s1:
#         if s != '':
#             a_s1_.append(s)
#     a_s0 = a_s0_
#     a_s1 = a_s1_

#     while len(a_s1) != 0 and len(a_s0) >= len(a_s1):
#         #s0's last component can nuke s1's last component
#         if possible(a_s0[-1],a_s1[-1]):
#             a_s0.pop()
#             a_s1.pop()
        
#         #s0's last component cannot nuke s1's last component and need backup
#         else:
#             if len(a_s0) < 2:
#                 return False
#             a_s0[-2] = a_s0[-2] + a_s0[-1]
#             a_s0.pop()
    
#     #Works iff every component of s1 was nuked successfully
#     if len(a_s1) != 0:
#         return False
#     return True





# for Homu in range(int(input())):
#     l0,l1 = [int(i) for i in input().split()]
#     s0 = input()
#     s1 = input()

#     if possible(s0,s1):
#         print('YeS')
#     else:
#         print('nO')
