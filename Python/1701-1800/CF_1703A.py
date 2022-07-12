#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    s = input().capitalize()
    if s == 'Yes':
        print('YeS')
    else:
        print('nO')
