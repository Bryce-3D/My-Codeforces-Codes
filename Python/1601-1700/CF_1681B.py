#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    cards = [int(i) for i in input().split()]
    m = int(input())
    shuffles = [int(i) for i in input().split()]

    total_shuffle = sum(shuffles)
    pos = total_shuffle % n
    print(cards[pos])
