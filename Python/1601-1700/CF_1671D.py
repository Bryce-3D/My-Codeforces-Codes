#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
1.) Inserting cannot decrease the score, it can only increase
2.) If the range of the values contains the thing to be inserted, there will
    always be a place where it can be inserted without increasing the score
3.) The question is equivalent to finding the minimum score after inserting 
    1 and n (max to be inserted) only
4.) If only one of 1,n is not in the range, simple linear search for the best
    place to insert it

TODO Handle the case where both 1 and n are not in range TODO
 - If 1 and n's optimal insertion spots are distinct, then it does not matter.
 - If 1 and n's optimal insertion spot are the same and not at an endpoint.
   WLOG insert 1 and n between a and b with 1 < a <= b < n.
     Then just insert them as a, 1, n, b.
     The score increase will equal the sum of the score increase of 
     a,1,b and a,n,b.
 - If 1 and n's optimal insertion spot are at the same endpoint
     This actually implies that the 2 endpoints are equal.
     Otherwise, the other endpoint MUST be a better choice for 1 (if smaller)
     or n (if larger).
     Therefore, just put 1 and n at opposite end, and the score increase will
     equal the sum of the score increase of inserting only 1 and only n

MAIN GIST OF THE ALG
if both 1 and n are in the range:
    just compute the score ignoring 1 and n
elif only 1 is in the range:
    linear search to find the best place to insert n
    - inserting n between a and b (where n > a,b since n > max(l))
      will increase the score by 2 * min(n-a, n-b)
    - inserting n before the first term/after the last term k (n > k)
      will increase the score by n-k
elif only n is in the range:
    linear search to find the best place to insert 1
    - inserting 1 between a and b (where 1 < a,b since n < min(l))
      will increase the score by 2 * min(a-1, b-1)
    - inserting 1 before the first term/after the last term k (1 < k)
      will increase the score by k-1
elif neither 1 nor n are in the range:
    perform both of the above and add them

OPTIMIZATION
The min score increase from inserting 1 is
    min(insert at end, insert at middle)
But then
    min(insert at middle) = 2 * [min(l) - 1]
Therefore the min used to check if 1 is in the range can be reused
An analogous argument holds for inserting n
'''

for Homu in range(int(input())):
    #Getting the inputs
    Kumiko = [int(i) for i in input().split()]
    length = Kumiko[0]
    n = Kumiko[1]
    l = [int(i) for i in input().split()]

    #Checing the max and min of l
    l_min = min(l)
    l_max = max(l)
    
    #Preparing score variables
    score = 0   #The original score
    inc_1 = 0   #The score increase from inserting 1
    inc_n = 0   #The score increase from inserting n

    #Finding score
    for i in range(length-1):
        score += abs(l[i+1] - l[i])
    
    #Finding inc_1
    if l_min > 1:   #Need min > 1 for 1 to be relevant
        end = min(l[0], l[-1]) - 1   #Min score increase from the ends
        middle = 2*(l_min - 1)       #Min score increase from the middle
        inc_1 = min(end, middle)
    
    #Finding inc_n
    if l_max < n:   #Need max < n for n to be relevant
        end = n - max(l[0], l[-1])   #Min score increase from the ends
        middle = 2*(n - l_max)       #Min score increase from the middle
        inc_n = min(end, middle)
    
    #Adding them up together
    ans = score + inc_1 + inc_n
    print(ans)
