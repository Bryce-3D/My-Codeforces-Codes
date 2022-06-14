#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
basically number of contiguous block of "k borders" where
the left number is less than twice the right number at the border

Wait a min how to check intervals??? Segtrees??????

Wait I can just find the length of each contiguous blocks of True 
in `borders` and count in each block
'''

for Homu in range(int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    #borders[i] = True if a[i] < 2*a[i+1] and False otherwise
    borders = []
    for i in range(n-1):
        if a[i] < 2*a[i+1]:
            borders.append(True)
        else:
            borders.append(False)
    

    #The length of every contiguous block of Trues in borders
    block_lengths = []
    #i is in block_borders iff borders[i] != borders[i+1]
    block_borders = []
    if borders[0]:
        block_borders.append(-1)
    for i in range(n-2):
        if borders[i] != borders[i+1]:
            block_borders.append(i)
    if borders[n-2]:
        block_borders.append(n-2)
    
    for i in range(len(block_borders)//2):
        next_len = block_borders[2*i+1] - block_borders[2*i]
        block_lengths.append(next_len)
    

    #Count the number of valid blocks and print the ans
    ans = 0
    for length in block_lengths:
        if length >= k:
            ans += length - k + 1
    print(ans)
