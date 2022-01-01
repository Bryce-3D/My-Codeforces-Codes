for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    Homura = [ int(i) for i in input().split() ]
    count = 0
    for Soul_Gem in range(2*n):
        if Homura[Soul_Gem]%2 == 0:
            count += 1
    
    if count == n:
        print('YES')
    else:
        print('NO')
