#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Best strat is zigzag
Sketch of proof: kth step must have x+y=k approx
Best is have x and y as close as possible
Therefore zigzag along main diagonal best
Now just find a closed form by math

ans = 1^2 + 2^2 + ... + n^2
      + 1^2 + 2^2 + ... + (n-1)^2 
      + 1   + 2   + ... + (n-1)
'''

p = 10**9 + 7

for Homu in range(int(input())):
    n = int(input())
    k = n//2

    a = n*(n+1)*(2*n+1)//6
    b = (n-1)*(n)*(2*n-1)//6
    c = (n-1)*n//2
    ans = (a+b+c)*2022
    ans %= p
    print(ans)
