#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
l = [int(i) for i in input().split()]
print(max(l))
