#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = input()

    seen = {}
    possible = True
    for i in range(n):
        num = a[i]
        let = s[i]

        if num in seen and seen[num] != let:
            possible = False
            break
        else:
            seen[num] = let
    
    if possible:
        print('YeS')
    else:
        print('nO')
