#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Basically find longest contiguous subarray with sum s.
Can do with 2 pointers and linearly tracing while tracking the sum.

Actually why not just get the indices of the 1s???
'''

for Homu in range(int(input())):
    n,s = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    #ones[i] returns the index of the ith 1, 1-indexed
    ones = [-1]
    for i in range(n):
        if a[i] == 1:
            ones.append(i)
    ones.append(n)
    #Number of 1s in a
    n1 = sum(a)

    #If not possible/trivial case
    if n1 < s:
        print(-1)
    elif n1 == s:
        print(0)
    
    #Main case: Possible and need to remove at least one
    else:
        max_len = 0

        #(L,R) means you include from the Lth 1 to the Rth 1, 1-indexed
        for L in range(1, n1-s+2):
            R = L+s-1

            left_end = ones[L-1] + 1
            right_end = ones[R+1] - 1
            length = right_end - left_end + 1

            #DEBUG ~~~~~~~~~~~~~~~~~~
            #print(left_end, right_end)

            max_len = max(max_len, length)
    
        ans = n - max_len
        print(ans)
