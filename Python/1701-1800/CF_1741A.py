#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    s0,s1 = input().split()

    if s0[-1] == 'S':
        if s1[-1] != 'S':
            print('<')
        elif len(s0) < len(s1):
            print('>')
        elif len(s0) > len(s1):
            print('<')
        else:
            print('=')
    elif s0[-1] == 'L':
        if s1[-1] != 'L':
            print('>')
        elif len(s0) < len(s1):
            print('<')
        elif len(s0) > len(s1):
            print('>')
        else:
            print('=')
    else:
        if s1[-1] == 'M':
            print('=')
        elif s1[-1] == 'S':
            print('>')
        else:
            print('<')
