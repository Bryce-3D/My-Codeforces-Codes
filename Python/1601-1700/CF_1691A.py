#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    odd = 0
    even = 0
    l = [int(i) for i in input().split()]
    for i in l:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    
    print(min(even,odd))
