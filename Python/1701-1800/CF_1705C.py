#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea

    lengths[i] = length of s after the first i operations
Change of plans, use a prefix array for this?
And have a separate actl array

    copy_len[i] = length of the ith copy paste (set [0] = -1)
    actl_len[i] = length of s after the ith copy paste
    L[i] = left end of ith copy paste (set [0] = -1)
    R[i] = right end of ith copy paste (set [0] = -1)

Can binary search to find out from what copy?

WAIT AT MOST 40 COPIES
BACKTRACKING IS PRACTICALLY O(1)

for each query:
    0.) MAKE THE INDEX 0-INDEXED, -=1
    1.) Find which copy operation it came from 
        (can just linearly scan, O(40) is O(1) no need bsearch)
    2.) Check which character it copied from in the prev one 
        (check where in [L:R] it lies)
    3.) Backtrack until you reach an index < n

'''

for Homu in range(int(input())):
    n,c,q = [int(i) for i in input().split()]
    s = input()

    copy_len = [-1]
    actl_len = [n]
    left_ends = [-1]    #0-INDEXED
    right_ends = [-1]   #0-INDEXED

    for Kumi in range(c):
        L_next, R_next = [int(i)-1 for i in input().split()]   #0-INDEXED
        copy_len.append(R_next - L_next + 1)
        actl_len.append(actl_len[-1] + copy_len[-1])
        left_ends.append(L_next)
        right_ends.append(R_next)
    
    for Kumi in range(q):
        k = int(input())-1   #0-INDEXED

        while k >= n:
            i_copy = 0   #Index of the copy operation that made the kth character, =0 if from og string s
            while k >= actl_len[i_copy]:   #While k not in the length after i_copy copy operations
                i_copy += 1
            
            L = left_ends[i_copy]    #Left end of copied part that made k
            R = right_ends[i_copy]   #Right end of copied part that made k

            depth = k - actl_len[i_copy-1]   #How deep into s[L:R] k is
            k = L + depth   #Find the place where k came from
        
        print(s[k])
