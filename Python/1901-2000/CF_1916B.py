from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Either n/p, n/p^2, or n/p, n/q
'''

def gcd(a,b):
    #Make a>=b
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

for Homu in range(int(input())):
    a,b = [int(i) for i in input().split()]

    if b%a == 0:
        p = b//a
        print(b*p)
    else:
        k = gcd(a,b)
        p = a//k
        q = b//k
        print(k*p*q)
