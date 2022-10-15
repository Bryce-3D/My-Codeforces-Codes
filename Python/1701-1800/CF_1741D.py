#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Ideas
262144 = 2^18

To be possible, 1 must be with 2
                3 must be with 4
                5 must be with 6
                ...
        (1,2) with (3,4)
        (5,6) with (7,8)
        ...
Similar for groups of 2^k for any k

Satisfy first group: Max each pairs forms 2,4,...,n
Satisfy second group: Max each pairs from above forms 4,8,12,...,n
...


'''

#Returns the answer
#Checks for a which contains elements in range(L,R) 
def ans(a,L,R):
    n = R-L
    if n == 1:
        return 0
    
    M = (L+R)//2
    k = n//2

    a_L = a[0:k]   #Left half
    a_R = a[k:n]   #Right half

    if max(a_L) == M-1 and min(a_R) == M:
        ans_L = ans(a_L, L, M)
        ans_R = ans(a_R, M, R)
        if ans_L != -1 and ans_R != -1:
            return ans_L + ans_R
        else:
            return -1
    elif min(a_L) == M and max(a_R) == M-1:
        ans_L = ans(a_L, M, R)
        ans_R = ans(a_R, L, M)
        if ans_L != -1 and ans_R != -1:
            return ans_L + ans_R + 1
        else:
            return -1
    else:
        return -1

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    print(ans(a, 1, n+1))
