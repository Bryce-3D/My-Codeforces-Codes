for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    r = n%3
    x = n//3

    if r == 0:
        print( str(x)+' '+str(x) )
        
    elif r == 1:
        print( str(x+1)+' '+str(x) )

    else:
        print( str(x)+' '+str(x+1) )
