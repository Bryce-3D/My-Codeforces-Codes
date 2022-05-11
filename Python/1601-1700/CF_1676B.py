#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    smol = min(l)
    eat = [i-smol for i in l]
    print(sum(eat))
