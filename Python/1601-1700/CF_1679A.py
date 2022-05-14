#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    if n == 2 or n%2 == 1:
        print(-1)
    else:
        #Get the max
        if n%4 == 0:
            Max = n//4
        else:
            Max = 1 + (n-6)//4
        
        #Get the min
        if n%6 == 0:
            Min = n//6
        elif n%6 == 2:
            Min = 2 + (n-8)//6
        else:
            Min = 1 + (n-4)//6
        
        print(Min, Max)
