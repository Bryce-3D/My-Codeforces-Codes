#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    R,C = [int(i) for i in input().split()]
    print(max(R,C))
