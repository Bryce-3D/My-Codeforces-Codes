#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    a = int(input())
    Alice = [int(i) for i in input().split()]
    b = int(input())
    Bob = [int(i) for i in input().split()]
    max_a = max(Alice)
    max_b = max(Bob)

    if max_a > max_b:
        print('Alice')
        print('Alice')
    elif max_a < max_b:
        print('Bob')
        print('Bob')
    else:
        print('Alice')
        print('Bob')
