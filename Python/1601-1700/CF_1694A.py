#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n0, n1 = [int(i) for i in input().split()]

    if n0 >= n1:
        ans = '01' * n1 + '0' * (n0-n1)
    else:
        ans = '10' * n0 + '1' * (n1-n0)
    
    print(ans)
