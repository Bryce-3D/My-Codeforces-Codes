#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    str_n = input()
    digits = len(str_n)

    #If there's at least 3 digits at the start, 
    #you can always force the smallest digit to stay
    if digits >= 3:
        print(min(str_n))
    elif digits == 2:
        print(str_n[1])
    elif digits == 1:
        print(str_n)
