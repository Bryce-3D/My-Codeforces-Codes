#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    total = 0
    for Kumi in range(2):
        total += sum([int(i) for i in input().split()])
    
    if total == 0:
        print(0)
    elif total == 4:
        print(2)
    else:
        print(1)
