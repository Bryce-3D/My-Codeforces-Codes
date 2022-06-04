#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA IDEA IDEA
SEEMS TOO MESSY SO MAYBE IT"S MEAN TTO BE CHEESED PARITY
CONsider the parity of the number of times a character c appears

c appears in t_i k times.
Contributes k to number of c's in total in list of t's
Contributes +- k to number of c's in the manipulated string
THEREFORE PARITY MOVES TOGETHER EXCEPT FOR EXTRA INIT CHARACTER
Count all
The one with odd parity overall is it
'''

#ord('a') = 97
letter = [chr(i+97) for i in range(26)]

for Homu in range(int(input())):
    n = int(input())
    
    counts = [0 for i in range(26)]

    #For each given string
    for Kumi in range(2*n+1):
        s = input()                            #Next string
        for i in range(26):                    #For each letter
            counts[i] += s.count(letter[i])   #Add the tally
    
    #Find the odd one
    for i in range(26):
        if counts[i] % 2 == 1:
            print(letter[i])
