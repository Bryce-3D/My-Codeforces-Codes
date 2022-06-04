#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    x = int(input())

    if x%2 == 1:   #If x is odd
        if x ^ 1 > 0:
            print(1)
        else:
            print(3)
    else:          #If x is even
        ans = 1
        x_copy = x
        while x_copy%2 == 0:
            ans *= 2
            x_copy //= 2
        if x ^ ans > 0:
            print(ans)
        else:
            print(ans+1)
