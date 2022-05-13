#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    
    #r1 has the smaller lower bound
    if Kumi[0] <= Kumi[2]:
        r1 = [Kumi[0], Kumi[1]]
        r2 = [Kumi[2], Kumi[3]]
    else:
        r1 = [Kumi[2], Kumi[3]]
        r2 = [Kumi[0], Kumi[1]]
    
    if r1[1] >= r2[0]:
        print(r2[0])
    else:
        print(r1[0] + r2[0])
