#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    a = Kumi[0]
    b = Kumi[1]
    c = Kumi[2]

    x = a + b * c
    y = b
    z = c

    print(x,y,z)
