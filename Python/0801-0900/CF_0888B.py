#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = input()

u = s.count('U')
d = s.count('D')
l = s.count('L')
r = s.count('R')

print(n - abs(u-d) - abs(l-r))
