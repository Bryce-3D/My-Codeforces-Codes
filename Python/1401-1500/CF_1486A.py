for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    Madoka = int(input())
    Homura = [ int(i) for i in input().split() ]
    total = 0
    req = 0
    check = 0
    
    for i in range(Madoka):
        total += Homura[i]
        req += i
        if total < req:
            check = 1
            break

    if check == 0:
        print('YES')
    else:
        print('NO')
