#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    l = [int(i) for i in input().split()]
    l.sort()
    print(l[1])
