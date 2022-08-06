#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
They must form "chains"
Find a way to quickly check if 2 belong to the same chain -> win

1 -> 2 -> 4 -> 8 -> 16 -> 22 -> 24 -> 28 -> 36
3 -> 6 -> 12 -> ... (units digit is 2 again)
7 -> 14 -> 18 -> 26 -> 32 -> ... (units digit is 2 again)
9 -> 18 -> 26 -> 32 -> ... (units digit is 2 again)

2 -> ...
4 -> 8 -> 16 -> 22 -> ...
6 -> 12 -> ...
8 -> 16 -> 22 -> ...

5 -> 0 -> ... (stuck)
0 -> 0 -> ... (stuck)

Pattern once you hit a units digit of 2 (take the number mod 20)
Possibility 1:     Possibility 2:
    2                  12
    4                  14
    8                  18
    16                 26

    22                 32
    24                 34
    28                 38
    36                 46
    ...                ...
Basically need to check if they same mod 20 to see if same chain
Otherwise they'll never meet



Code flow:

if multiple of 5 exists:
    if everything is a multiple of 5 and max-min <5:
        print yes
    else:
        print no
else:
    for each term:
        iterate till you reach a multiple of 2
'''

def process(n):
    if n%5 == 0:
        return -1
    else:
        #Spam till units digit is 2
        while n%10 != 2:
            n += n%10
        #Check the mod 20
        if n%20 == 2:
            return 0
        else:
            return 1

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    processed = [process(i) for i in a]

    if -1 in processed:
        if max(processed) != -1:
            print('nO')
        else:
            M = max(a)
            m = min(a)

            if M-m > 5:
                print('nO')
            elif M != m and m%10 != 5:
                print('nO')
            else:
                print('YeS')

    else:
        if max(processed) == min(processed):
            print('YeS')
        else:
            print('nO')
