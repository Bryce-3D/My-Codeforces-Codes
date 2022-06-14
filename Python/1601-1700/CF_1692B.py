#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    seen = set()
    to_remove = 0

    for num in a:
        if num in seen:   #Need to remove
            to_remove += 1
        else:   #Don't need to remove
            seen.add(num)
    
    if to_remove%2 == 1:
        to_remove += 1
    
    print(n - to_remove)
