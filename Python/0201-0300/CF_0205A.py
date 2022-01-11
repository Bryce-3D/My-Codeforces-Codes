#For fast I/O
import sys
input = sys.stdin.readline

n = int(input())
l = [int(i) for i in input().split()]

smol = min(l)
if l.count(smol) == 1:
	print(l.index(smol)+1)
else:
	print("Still Rozdil")
