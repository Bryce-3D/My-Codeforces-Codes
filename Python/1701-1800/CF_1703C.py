#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    lock = [int(i) for i in input().split()]

    for i in range(n):
        l,s = input().split()
        for move in s:
            if move == 'U':
                lock[i] -= 1
            else:
                lock[i] += 1
            lock[i] %= 10
    
    lock = [str(i) for i in lock]
    ans = ' '.join(lock)
    print(ans)
