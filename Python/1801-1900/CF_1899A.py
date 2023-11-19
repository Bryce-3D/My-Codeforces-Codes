#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    if n%3 == 0:
        print("Second")
    else:
        print("First")
