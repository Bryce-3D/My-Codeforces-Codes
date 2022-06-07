#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())

    k = n//3

    if n%3 == 0:
        print(k,k+1,k-1)
    elif n%3 == 1:
        print(k,k+2,k-1)
    else:
        print(k+1,k+2,k-1)
