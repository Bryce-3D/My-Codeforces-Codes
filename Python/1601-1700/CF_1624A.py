#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]
	print(max(a)-min(a))
