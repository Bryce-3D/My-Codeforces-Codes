#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Linearly trace from left to right all substrings of length k
Track the number of black and number of white while scanning
To go to next substring, remove front color and add rear color (O(1) update)

There will be n-k+1 substrings to check (start at index 0 to n-k)

NOTE: MISREAD IT SAID BLACK LENGTH K NOT MONOCHROMATIC LENGTH K
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]

    s = input()

    #black = 0
    white = 0
    ans = 0

    #Check the first substring
    for i in range(k):
        if s[i] == 'W':
            white += 1
    ans = white

    #Check the remaining n-k substrings
    for i in range(n-k):
        #Remove head
        if s[i] == 'W':
            white -= 1
        #Extend tail
        if s[i+k] == 'W':
            white += 1
        #Update ans if better
        ans = min(ans, white)
    
    print(ans)
