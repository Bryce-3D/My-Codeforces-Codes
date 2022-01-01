for dlhjk in range( int(input()) ):
    Homu = [ int(i) for i in input().split() ]
    n = Homu[0]
    m = Homu[1]
    k = Homu[2]
 
    if m%2 == 0 and n%2 == 0:
        if k%2 == 0:
            print('YeS')
        else:
            print('nO')
 
    elif n%2 == 0:
        if k%2 == 0 and 2*k <= (m-1)*n:
            print('YeS')
        else:
            print('nO')
 
    else:
        if (k - m*n//2)%2 == 0 and 2*k >= m:
            print('YeS')
        else:
            print('nO')
