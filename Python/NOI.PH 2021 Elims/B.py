homura = int(input())

for i in range(homura):
    madoka = [int(i) for i in input().split()]
    d = madoka[1]-madoka[0]
    s = madoka[2]-madoka[3]
    if s<=0:
        print(-1)
    else:
        print(d/s)
    
