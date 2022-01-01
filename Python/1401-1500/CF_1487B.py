for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    Homura = [ int(i) for i in input().split() ]
    n = Homura[0]
    t = Homura[1]
    
    if n%2 == 1:
        k = (n-1)//2
        cycles = t//k
        excess = t%k
        if excess != 0:
            move = (k+1)*cycles + excess
        else:
            move = (k+1)*cycles - 1
        print( (move-1)%n + 1 )
    else:
        print( (t-1)%n + 1 )
