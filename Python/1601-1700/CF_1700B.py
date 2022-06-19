#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
We just need to find one, not the max or min.
n digits
10^n + 1 is a palindrome

Corner case:
Number has first digit 9
Then make the sum
10^n + 10^(n-1) + 11
'''

for Homu in range(int(input())):
    n = int(input())
    s_num = input()
    num = int(s_num)
    
    if s_num[0] == '9':
        ans = 10**n + 10**(n-1) + 11 - num
        print(ans)
    else:
        ans = 10**n + 1 - num
        print(ans)
